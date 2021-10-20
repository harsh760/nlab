

# Synopsis
This consists of few ReST api endpoints that are to be created using django. List of api endpoints are given at the end of the file. 
Some API endpoints need the authentication token which can be applied by registering user or using existing login details.

### Deployed on heroku -
[https://nlab-internship.herokuapp.com](https://nlab-internship.herokuapp.com)

### How to run project on local host -
- Clone the repository
`git clone https://github.com/harsh760/nlab.git`

- Install all the required library and dependencies
`pip3 install -r requirements.txt`

- To migrate database
`python3 manage.py makemigrations`
`python3 manage.py migrate`
**Note** : change the database section in settings.py to access the database

- To run the project
`python3 manage.py runserver`


### API endpoints
- User Registration: `user/register`
- User Login: `user/login`
- Add Advisor: `admin/advisor`
- Get all advisors: `user/<user_id>/advisor`[*authentication required*]
- Book advisor: `user/<user_id>/advisor/<advisor_id>`[*authentication required*]
- Get bookings of user : `user/<user_id>/advisor/booking`[*authentication required*]


### Postman collection
- Collection can be downloaded from [here](https://drive.google.com/file/d/1IA_BEpYgdmCAFAeYgSodctZm94TTN2uC/view?usp=sharing)
