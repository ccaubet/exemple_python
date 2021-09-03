FROM python:3.9

LABEL auteur ="camille"
LABEL type="dev" 

#équivalent de : mkdir application puis d'un cd application
WORKDIR /application

COPY ./requirements.txt .
COPY ./src .

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python3", "app.py" ]

#ou ENTRYPOINT [ "python3"] et CMD [ "app.py" ]