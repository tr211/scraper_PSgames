FROM python:3.11
WORKDIR /app
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY . .
EXPOSE 7777
CMD ["fastapi", "run", "fastAPI.py", "--port", "7777"]