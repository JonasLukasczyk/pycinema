#!/usr/bin/env python

# import asyncio
# from websockets.asyncio.server import serve

# async def echo(websocket):
#     async for message in websocket:
#         await websocket.send(message)

# async def main():
#     async with serve(echo, "localhost", 8765) as server:
#         await server.serve_forever()

import json
import os
import asyncio
from aiohttp import web
import websockets
from websockets.asyncio.server import serve

import pycinema
import pycinema.filters

# pycinema settings
PYCINEMA = { 'VERSION' : '2.1.0'}

# this application settings
VIEW = { 'VERSION' : '1.0'}

# reporting
print("view v" + VIEW["VERSION"])

# WebSocket echo handler

filter_list = dict([(name, cls) for name, cls in pycinema.filters.__dict__.items() if isinstance(cls,type) and issubclass(cls,pycinema.Core.Filter) and len(cls.__subclasses__())<1])

websocket_list = []
async def echo(websocket):
  print('connected')

  websocket_list.append(websocket)

  i = 0
  async for message_raw in websocket:
    message = json.loads(message_raw)
    print(i,message)
    i+=1
    if message['header'] == 'get_filter_list':
      await send_message('filter_list',[*filter_list],message['id'])

    elif message['header'] == 'create_filter':
      f = filter_list[message['payload']]()
    elif message['header'] == 'connect_ports':
      f0_id = message['payload'][0]['parent']
      f1_id = message['payload'][1]['parent']
      f0 = next(f for f in pycinema.filters.Filter._filters.values() if f.id == f0_id)
      f1 = next(f for f in pycinema.filters.Filter._filters.values() if f.id == f1_id)

      if message['payload'][0]['is_input']:
        p0 = f0.inputs.get(message['payload'][0]['name'])
      else:
        p0 = f0.outputs.get(message['payload'][0]['name'])

      if message['payload'][1]['is_input']:
        p1 = f1.inputs.get(message['payload'][1]['name'])
      else:
        p1 = f1.outputs.get(message['payload'][1]['name'])
      if p1.is_input:
        p0,p1 = p1,p0

      p0.set(p1)
    elif message['header'] == 'port_set_value':
      port = message['payload'][0]
      value = message['payload'][1]
      f = next(f for f in pycinema.filters.Filter._filters.values() if f.id == port['parent'])
      p = f.inputs.get(port['name']) if port['is_input'] else f.outputs.get(port['name'])
      p.set(value)
      print(value)

    # if message.header == 'create_filter':
    #   f = pycinema.filters.CinemaDatabaseReader()


# Static file handler for serving the 'dist' folder
async def static_file_handler(request):
    # Return the index.html when any URL is accessed
    return web.FileResponse(os.path.join('pycinema/web/client/dist', 'index.html'))

# WebSocket connection setup
async def start_websocket_server():
    # Start WebSocket server on localhost:8765
    return await websockets.serve(echo, "localhost", 8765)

async def send_message(header,payload,id=-1):
  msg = json.dumps({
    'id': id,
    'header': header,
    'payload': payload
  })
  to_remove = []
  for socket in websocket_list:
    try:
      await socket.send(msg)
    except:
      to_remove.append(socket)

  for socket in to_remove:
    websocket_list.remove(socket)

async def filter_created(filter):
  await send_message('filter_created',filter.toJSON())

async def filter_removed():
  return

async def connection_added(ports):
  await send_message('connection_added',[p.toJSON() for p in ports])

# /home/jones/projects/cinema-lib/pycinema/data/sphere.cdb/

async def value_set(data):
  await send_message('value_set',data[0].toJSON())

async def connection_removed():
  return

async def init():
    app = web.Application()

    # Serve static files from the 'dist' folder
    app.router.add_static('/assets', path='pycinema/web/client/dist/assets', name='assets')

    app.router.add_get('/', static_file_handler)

    websocket_server = await start_websocket_server()

    # Run the aiohttp web server on port 8000
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8000)
    await site.start()

    print("Serving static files and WebSocket server on ws://localhost:8765 and http://localhost:8000")

    pycinema.Filter.on('filter_created', filter_created)
    pycinema.Filter.on('filter_deleted', filter_removed)
    pycinema.Filter.on('value_set', value_set)
    pycinema.Filter.on('connection_added', connection_added)
    pycinema.Filter.on('connection_removed', connection_removed)

    # CinemaDatabaseReader_0.inputs.path.set("/home/jones/projects/cinema-lib/pycinema/data/scalar-images.cdb", False)
    # CinemaDatabaseReader_0.update()

    # Keep the event loop running for the WebSocket server
    await websocket_server.wait_closed()

# Run the app
if __name__ == "__main__":
    asyncio.run(init())

