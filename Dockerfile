FROM python:3.9-slim
WORKDIR  /app
#копирование из текузей директории в наш контейнер
COPY . .
#каманда которая запуститься при старте
CMD ["python" , "main.py"]
#docker build -t  my-python-app . --запуск и инит всего
