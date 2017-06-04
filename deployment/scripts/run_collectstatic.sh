(export $(cat .env.dev | xargs) && python backend/manage.py collectstatic --noinput)
