# gitscore

# build / run the service
1. Clone the service
2. Ensure you are running docker on your environment
3. cd to the service directory using terminal
4. Run docker-compose -f local.yml up --build
5. N.B Super admin user account will be creates, credentails are uname: admin pword: brickmode
6. Social Auth app will be setup (Github)

# run automatic tests
1. Execute the web docker containter with bash with docker exec -it gitscore_web_1 bash
2. Run coverage run manage.py test apps/repocheck/

# what improvements would you make if I had more time
1. Extensive useage of the github apis 
2. Improving the UI
3. Add more analytics 


