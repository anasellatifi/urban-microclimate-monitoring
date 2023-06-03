from flask import render_template, request
from . import app
from .database import fetch_microclimate_analysis_results

@app.route('/microclimate_analysis')
def microclimate_analysis():
    analysis_results = fetch_microclimate_analysis_results()
    return render_template('microclimate_analysis.html', results=analysis_results)


@app.route('/')
def index():
    return render_template('index.html')
