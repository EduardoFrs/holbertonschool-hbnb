FROM python:3.10.12-alpine
RUN apk add --no-cache curl
WORKDIR /holbertonschool-hbnb
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
ENV ip=0.0.0.0 port=5000
VOLUME /holbertonschool-hbnb/data
CMD ["ash", "-c", "usr/local/bin/gunicorn -b $ip:$port main:app"]