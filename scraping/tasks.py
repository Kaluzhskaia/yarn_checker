from yarn_checker.celery import app
from .web_sites.scrapers.woolplatz import scrape_woolplatz


@app.task
def scrape_recourse():
    scrape_woolplatz()
