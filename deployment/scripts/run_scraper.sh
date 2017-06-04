(REMAP_SIGTERM=SIGQUIT PYTHONPATH="gather" celery -A gather worker -Q scraper -E --loglevel=INFO)
