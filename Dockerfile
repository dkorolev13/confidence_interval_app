FROM python:3.10-slim

RUN python -m pip install --upgrade pip

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./my_cv /my_cv

WORKDIR /my_cv

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]