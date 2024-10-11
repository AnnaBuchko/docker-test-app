FROM python:3.7-slim
WORKDIR /app
RUN pip install networkx dash plotly
COPY . .
EXPOSE 8080
CMD ["python", "testApp.py", "sample_file.txt"]