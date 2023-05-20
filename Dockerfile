FROM python:3.6
MAINTAINER Danila Bondar 'klieglee@gmail.com'
RUN pip install flask flask_restful
COPY . /app
WORKDIR /app
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
