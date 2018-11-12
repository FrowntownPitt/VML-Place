# main.py
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash, _app_ctx_stack
import numpy as np
import json

app = Flask(__name__)

active_grid = np.full((15, 15) , fill_value=None)
active_grid[0,0] = np.zeros((32, 32, 3))

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/spimewrangler")
def wrangle():
    return render_template("wrangle.html")

@app.route("/set_shape/<shape>", methods=['POST'])
def set_shape(shape):
    global active_grid
    #shape is a list of tuples, index of each active panel
    #sets shape of data, with all pixels set to default value

    
    #TODO
    for x in range(15):
        for y in range(15):
            if shape[] is None:
                active_grid[index] = np.zeros((32, 32, 3))
            else:
                active_grid[index] = None
    return "Good"
    
@app.route("/set_pixel/<grid_data>/<coordinate>/<rgb>", methods=['POST'])
def set_pixel(grid_data, coordinate, rgb):
    #sets a pixel to a given color
    #coordinate is a tuple of tuples
    grid = tuple([int(x) for x in grid_data.split(",")])
    cord = tuple([int(x) for x in coordinate.split(",")])
    global active_grid
    active_grid[grid][cord] = [int(x) for x in tuple(rgb.split(","))]
    return "Good"

@app.route("/get_grid")
def get_grid():
    #returns the grid config and data
    global active_grid
    grid = [[0 for x in range(15)] for y in range(15)]
    for i, r in enumerate(active_grid):
        for j, c in enumerate(r):
            if c is not None:
                grid[j][i] = c.tolist()
            else:
                grid[j][i] = 0

    return json.dumps(grid)
