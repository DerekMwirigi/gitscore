# gitscore

[![Build Status](https://travis-ci.com/DerekMwirigi/gitscore.svg?branch=main)](https://travis-ci.com/DerekMwirigi/gitscore)


# 1 Service description with all made assumptions
    Here is simple way to check github repositories score, We calculate popularity by score = (num_stars * 1 + num_forks * 2) <strong> >= 500
    1. Need to have a github account
# 2 Tech stack used (runtime environment, frameworks, key libraries)
    1. Runtime environment
        a. Docker
        b. python:3.7
    2. Frameworks
        a. Django, Djangorestframework
    3. Libraries
        a. django-allauth (Social authentiction - Github)
        b. coverage (unit testing)
# a. Build / Run the service
    1. Clone the service
    2. Ensure you are running docker on your environment
    3. cd to the service directory using terminal
    4. Run docker-compose -f local.yml up --build (launches @ http://127.0.0.1:8099)
    5. N.B Super admin user account will be creates, credentails are uname: admin pword: brickmode
    6. Social Auth app will be setup (Github)

# b. Run automatic tests
    1. Travis CI https://travis-ci.com/DerekMwirigi/gitscore

# c. What improvements would you make if I had more time
    1. Extensive useage of the github apis 
    3. Add more analytics 
