FROM python:3.9

LABEL MAINTAINER="resturant | https://resturant.com"
LABEL VERSION="1.0a"

ENV PYTHONUNBUFFERED 1
ENV HOME=/opt/resturant/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
ADD requirements.txt $HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY configs $HOME/configs
COPY manage.py $HOME
COPY resturant $HOME/resturant

COPY docker.conf.d/resturant/entrypoint.sh $HOME

ENTRYPOINT ["sh", "./entrypoint.sh"]