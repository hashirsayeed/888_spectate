FROM python:3-alpine3.18
WORKDIR /
COPY . /api/
RUN pip install -r ./api/requirement.txt 
EXPOSE 5000


CMD python -m api.app