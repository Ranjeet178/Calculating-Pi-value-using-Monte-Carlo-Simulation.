# Calculating-Pi-value-using-Monte-Carlo-Simulation.
## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on GAE](#deployement-on-gae)
  * [To Do](#to-do)
  * [Technologies Used](#technologies-used)



## Demo
[![]()]()

## Overview
It is a multi-cloud project which aims to calculate the value of "pi" using the monte Carlo simulation method. The AWS services like EC2 instance and lambda function are used to calculate 'pi' values. A flask app is developed for a user interface that connects to both EC2 and lambda and based on the user choice, it calls the AWS services and calculates the value of 'pi'. The entire application  is then deployed in the google app engine(GAE)

## Motivation
It is a cloud computing assignment which I have done during my first semester. The main object here was to developed multi cloud application and calculate pi values. 

## Technical Aspect
This project is divided into two part:
1. Developing a flask app which will be connected to AWS services like lambda and EC2.
2. Deploying the entire application in google app engine.
    - The user has to specify the number of shots, number of resources.
    - Based on the user input it will call the services to calculate the pi-values.
    - After the values has been retrun from AWS to the flask a graph can be seen with the set of pi values and a history which shows the all transcations.

## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
bash
pip install -r requirements.txt


## Run
> STEP 1
#### Windows User
> Install python 3.7 from (https://www.python.org/downloads/)
> For IDE install visual code studio.
> To insatll all the requirements write pip install -r requirements.txt
> For AWS servises we need to get the aws_access_key_id and aws_secret_access_key which you can generate from you AWS account. 

_Attention: Please perform the steps given in these tutorials at your own risk. Please don't mess up with the System Variables. It can potentially damage your PC. __You should know what you're doing_. 
- https://www.tenforums.com/tutorials/121855-edit-user-system-environment-variables-windows.html
- https://www.onmsft.com/how-to/how-to-set-an-environment-variable-in-windows-10

> STEP 2

To run the app in a local machine, shoot this command in the project directory:
bash
gunicorn wsgi:app


## Deployement on GAE
Deploy the entrire application in Google app engine. [[Reference](https://lamda11050.ew.r.appspot.com/)]

![]()

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.




## To Do
1. Add a better UI for the application.

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/Ranjeet178/Calculating-Pi-value-using-Monte-Carlo-Simulation/issues/new) by including your search query and the expected result.

## Technologies Used
- Python 3.7
- Flask
- AWS and GAE
- Javascript, HTML and CSS
- Google charts

## Authors
- LinkedIn - [Ranjeet Singh Yadav](https://www.linkedin.com/in/ranjeet-singh-yadav-b5183b118/)

## Acknowledgements
This project is completed by me from scratch.
