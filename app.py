from flask import Flask, render_template
from pathlib import Path 

app = Flask(__name__)

# Define Python functions that will be triggered if we go to defined URL paths
# Anything we `return` is rendered in our browser as HTML by default
@app.route('/') # home page 
def present_map():
    return render_template('main.html')

@app.route('/map')
def map_render():
    return render_template('divvy_trips_q3_2018_map.html')

if __name__ == "__main__":
    print()
    app.run() # allows us to run app via `python app.py`