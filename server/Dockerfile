FROM python:3.8

# Copy Files RUN mkdir /umass_match

RUN mkdir /umass_match

COPY ./ /umass_match/
COPY main.py /

WORKDIR /umass_match

# Install all dependencies from the Pipfile

RUN pip3 install pipenv
RUN pipenv lock
RUN pipenv install --system --deploy
RUN pip3 install psycopg2

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]