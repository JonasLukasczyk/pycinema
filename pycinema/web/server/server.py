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

# filters
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
# ParametersView_0 = pycinema.filters.ParametersView()
# ImageReader_0 = pycinema.filters.ImageReader()
# DepthCompositing_0 = pycinema.filters.DepthCompositing()
# ColorMapping_0 = pycinema.filters.ColorMapping()
# ShaderSSAO_0 = pycinema.filters.ShaderSSAO()
# TableView_0 = pycinema.filters.TableView()
# ImageView_0 = pycinema.filters.ImageView()
# ImageAnnotation_0 = pycinema.filters.ImageAnnotation()

# properties
CinemaDatabaseReader_0.inputs.path.set("/home/jones/projects/cinema-lib/pycinema/data/scalar-images.cdb", False)
# ParametersView_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
# ImageReader_0.inputs.table.set(ParametersView_0.outputs.table, False)
# DepthCompositing_0.inputs.images_a.set(ImageReader_0.outputs.images, False)
# DepthCompositing_0.inputs.compose.set(ParametersView_0.outputs.compose, False)
# ColorMapping_0.inputs.images.set(DepthCompositing_0.outputs.images, False)
# ShaderSSAO_0.inputs.images.set(ColorMapping_0.outputs.images, False)
# ImageAnnotation_0.inputs.images.set(ShaderSSAO_0.outputs.images, False)
# TableView_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)
# ImageView_0.inputs.images.set(ImageAnnotation_0.outputs.images, False)

# execute pipeline
CinemaDatabaseReader_0.update()

# WebSocket echo handler
async def echo(websocket):
  async for message in websocket:
    # print(json.dumps(CinemaDatabaseReader_0.outputs.table.get()))
    await websocket.send(json.dumps(CinemaDatabaseReader_0.outputs.table.get()))
    # await websocket.send(str(CinemaDatabaseReader_0.outputs.table.get()))

# Static file handler for serving the 'dist' folder
async def static_file_handler(request):
    # Return the index.html when any URL is accessed
    return web.FileResponse(os.path.join('dist', 'index.html'))

# WebSocket connection setup
async def start_websocket_server():
    # Start WebSocket server on localhost:8765
    return await websockets.serve(echo, "localhost", 8765)

# Setup aiohttp web server
async def init():
    # Create the aiohttp application
    app = web.Application()

    # Serve static files from the 'dist' folder
    app.router.add_static('/assets', path='dist/assets', name='assets')

    # Handle requests for any route (they will all get the index.html for SPA)
    app.router.add_get('/', static_file_handler)

    # Start the WebSocket server
    websocket_server = await start_websocket_server()

    # Run the aiohttp web server on port 8000
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8000)
    await site.start()

    print("Serving static files and WebSocket server on ws://localhost:8765 and http://localhost:8000")

    # Keep the event loop running for the WebSocket server
    await websocket_server.wait_closed()

# Run the app
if __name__ == "__main__":
    asyncio.run(init())
