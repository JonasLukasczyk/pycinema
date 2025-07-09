r"""
Installation requirements:
    pip install trame trame-vuetify pandas
"""

from trame.app import get_server
from trame.ui.vuetify import SinglePageLayout
from trame.widgets import vuetify, trame, html, plotly
import json

import numpy as np

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

import pycinema
import pycinema.filters

server = get_server(client_type="vue2")
state, ctrl = server.state, server.controller

state.sql = 'SELECT * FROM input LIMIT 10'
state.selected_rows = []

# PYCINEMA
CinemaDatabaseReader_0 = pycinema.filters.CinemaDatabaseReader()
TableQuery_0 = pycinema.filters.TableQuery()
ImageReader_0 = pycinema.filters.ImageReader()

# properties
CinemaDatabaseReader_0.inputs.path.set("data/sphere.cdb", False)
CinemaDatabaseReader_0.inputs.file_column.set("FILE", False)
TableQuery_0.inputs.table.set(CinemaDatabaseReader_0.outputs.table, False)

ImageReader_0.inputs.table.set(TableQuery_0.outputs.table, False)
ImageReader_0.inputs.file_column.set("FILE", False)
ImageReader_0.inputs.cache.set(True, False)

def update_table():
  ImageReader_0.update()

  table = TableQuery_0.outputs.table.get()
  headers = table[0]

  header_options = {}
  for j in range(0,len(headers)):
    header_options[headers[j]] = {"text":headers[j]}

  data_dict = []
  for i in range(1,len(table)):
    row = table[i]
    data = {}
    for j in range(0,len(row)):
      data[headers[j]] = row[j]
    data_dict.append(data)

  table_data_frame = pd.DataFrame.from_dict(data_dict)
  state.headers, state.rows = vuetify.dataframe_to_grid(table_data_frame, header_options)

  # rgba_image = np.random.rand(100, 100, 4)

  # except :
  #   print('eh', e)

# init table
headers, rows = vuetify.dataframe_to_grid(pd.DataFrame.from_dict({}), {})
table = {
    "v_model": ('selected_rows',''),
    "headers": ("headers", headers),
    "items": ("rows", rows),
    "classes": "elevation-1 ma-4",
    "multi_sort": True,
    "dense": True,
    "items_per_page": 5,
    "single_select":True,
    "show_select": True
}


@state.change("sql")
def sql_value_change(sql, **kwargs):
  TableQuery_0.inputs.sql.set(sql)
  update_table()

@state.change("selected_rows")
def selected_rows_value_change(**kwargs):
  print(state.selected_rows)
  if not len(state.selected_rows): return
  selection = state.selected_rows[0]

  for i in ImageReader_0.outputs.images.get():
    if i.meta['FILE']==selection['FILE']:
      rgba = i.channels['rgba']
      fig = go.Figure(data=go.Image(z=rgba))
      fig.update_layout(
          title="RGBA Image Plot",
          xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
          yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
          dragmode=False  # Disable dragging/zooming
          # staticPlot=True   # Disable interactivity (pan/zoom)
      )
      ctrl.figure_update(fig)
      return






selection = ["2"]
tree = [
    {"id": "1", "parent": "0", "visible": 0, "name": "Wavelet"},
    {"id": "2", "parent": "1", "visible": 0, "name": "Clip"},
    {"id": "3", "parent": "1", "visible": 1, "name": "Slice"},
    {"id": "4", "parent": "2", "visible": 1, "name": "Slice 2"},
]

# Plot using Plotly
# fig = px.imshow(rgba_image)
# fig.update_layout(title="RGBA Image Plot", coloraxis_showscale=False)


# --------------------------------------------------------------------------------
# GUI
# --------------------------------------------------------------------------------

with SinglePageLayout(server) as layout:
    layout.title.set_text("PyCinema Trame Example")
    with layout.toolbar:
        vuetify.VSpacer()
        vuetify.VTextField(
            v_model=("sql", ""),
            placeholder="Search",
            dense=True,
            hide_details=True,
        )

    with layout.content:
       with vuetify.VContainer(fluid=True):
          with vuetify.VRow(dense=True):
            with vuetify.VCol(dense=True):
                trame.GitTree(
                    sources=("tree", tree),
                    actives=("selection", selection),
                )
            with vuetify.VCol(dense=True):
                vuetify.VDataTable(**table)
            with vuetify.VCol(dense=True,classes='fill-height'):
                figure = plotly.Figure(
                    display_logo=False,
                    display_mode_bar="true",
                    # selected=(on_event, "['selected', utils.safe($event)]"),
                    # hover=(on_event, "['hover', utils.safe($event)]"),
                    # selecting=(on_event, "['selecting', $event]"),
                    # unhover=(on_event, "['unhover', $event]"),
                )
                ctrl.figure_update = figure.update
        # html.Img(src=state.image_base64, style="width: 200px;")

update_table()

if __name__ == "__main__":
    server.start()
