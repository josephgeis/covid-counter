#!/usr/bin/env python

"""
covid_count
Joseph Geis (@juniorrubyist)

[description]
"""

import os
from flask import Flask, render_template, url_for, abort

import scrapers

def static(filename):
    """Provides the 'static' function that also appends the file's timestamp to the URL, usable in a template."""
    timestamp = os.path.getmtime(os.path.join(app.static_folder, filename))
    return "%s/%s?%s" % (app.static_url_path, filename, timestamp)

# Flask application
app = Flask(__name__)
app.jinja_env.globals.update(static=static)

# Views
@app.route('/')
def index():
    return render_template('index.html', scrapers=scrapers.available())


@app.route('/<locale_id>')
def locale(locale_id):
    scraper = scrapers.get(locale_id)
    if scraper:
        return render_template('counter.html', scraper=scraper)
    else: abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

# Run dev server
if __name__ == '__main__':
    app.run('localhost', port=8080, debug=True)
