FROM python:3.10.6
WORKDIR /app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./src ./
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
