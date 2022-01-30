# APIwithDDOS
Simple Login API with a 1 minute Session. Upload API has A simple DDOS Protection Implemented


#What I did

All the developed APIs should be testable via Postman
1. Create a basic back-end with Django and Django Rest Framework for APIs
2. Create following API endpoints
- Login (url = /mylogin). Accept email and password as input. Return 200 status on
login. Each login should start a 1 min session for that user.
- Upload (url - /upload). Should accept any le type and upload to server. Save le in
media folder, return an upload ID. The ID can be incremental. Upload API should
work only after a login. Should return 403 if user is not logged in.
3. Implement a kind of DDoS protection. If the Upload API is called more than 5 times
in a minute, the response should return 429 - Unauthorized , with message “Too many
attempts”. This functionality should preferably be implemented in a middleware


# Installation and Setting Up

1. Download the zip file and extract.
2. Now create a virtual environment through - python3 -m venv /path/to/new/virtual/environment For Reference - https://docs.python.org/3/library/venv.html
3. Now activate it through - source envname/bin/activate
4. Now cd into the project folder and do pip install -r requirements.txt -- this will install all the required packages.
5. Run the server - python3 manage.py runserver
6. Now head over to postman and try the first API - http://127.0.0.1:8000/mylogin through POST method and in the body use - the dummy superuser account I already created - email - ekaanshsahni@gmail.com password - kt6uqn0kss
7. Now run the second api immediately as session expires after 1 minute - http://127.0.0.1:8000/upload 
Note - In postman, by default CSRF Token is not passed in header but passed inside cookiesm, So follow steps - 
a. Search for the Cookie header
b. Separate the csrftoken from the sessionid
c. Add the X-CSRFToken={..the csrftoken that you extracted in step 2..}
Reference = https://stackoverflow.com/questions/26639169/csrf-failed-csrf-token-missing-or-incorrect

8. Now run the api with body parameter files <file> and file will be uploaded.
  if you run it more than 5 times in a minute then there will be a error for too many attempts.
  
 # Happy Coding :)

