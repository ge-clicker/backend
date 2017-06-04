(REMAP_SIGTERM=SIGQUIT PYTHONPATH="gather" celery -A gather worker -Q celery --concurrency=3 -E --loglevel=INFO)
