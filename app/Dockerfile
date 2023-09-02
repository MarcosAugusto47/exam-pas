FROM python:3.11

COPY app/requirements.txt .
COPY app/encodings/encoding_category.pickle /encodings/encoding_category.pickle
#COPY pipelines/features /pipelines/features
#COPY pipelines/models/config.py /pipelines/models/config.py

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "app/app.py", "run", "--host=0.0.0.0"]
