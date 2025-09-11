FROM python:3.12.7
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements.txt /app/ .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . /app/
CMD ["gunicorn", "manage.py", "--bind", "runserver"]
