FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install -r deployment/requirements.txt

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]