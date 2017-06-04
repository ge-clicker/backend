FROM gcr.io/google_appengine/python
LABEL python_version=python3.5
RUN virtualenv --no-download /env -p python3.5

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Fixes wheel issues
RUN pip install -U wheel

# Install requirements
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app/


RUN bash ./deployment/scripts/run_collectstatic.sh

CMD bash ./deployment/scripts/run_production.sh
