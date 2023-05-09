FROM python:3.9

WORKDIR /dev

COPY ./app /dev
COPY ./requirements.txt /dev/requirements.txt
COPY ./.env /dev/.env

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD uvicorn main:app --host=0.0.0.0 --port=9000 --reload
