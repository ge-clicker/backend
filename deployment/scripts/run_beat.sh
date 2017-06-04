(REMAP_SIGTERM=SIGQUIT PYTHONPATH="gather" celery -A gather beat --loglevel=INFO --scheduler=django)
