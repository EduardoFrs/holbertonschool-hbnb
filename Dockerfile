FROM python:3.10.12-alpine
RUN apk add --no-cache curl
WORKDIR /holbertonschool-hbnb
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
ENV PORT=5000
VOLUME /holbertonschool-hbnb/data
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app" ]