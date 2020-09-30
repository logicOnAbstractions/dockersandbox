FROM python:3.8-alpine
WORKDIR /project

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN echo "pip install of requirements.txt done"

EXPOSE $WEB_PORT
COPY . /project

RUN echo "dockerfile completed"
CMD ["python", "main.py"]