FROM python:3.11.0b4-alpine3.16

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
ADD app.py .
# Now the structure looks like this '/usr/app/src/test.py'

COPY requirements.txt .

RUN pip install -U pip 
RUN pip install -r requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
EXPOSE 8000
CMD [ "python", "./app.py"]