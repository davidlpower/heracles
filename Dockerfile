FROM python:3.8.5

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends locales locales-all && locale-gen de_DE && update-locale LANG=de_DE

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["./run.sh"]