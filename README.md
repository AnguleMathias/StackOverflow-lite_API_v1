# StackOverflow-lite_API_v1
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Badges

[![Build Status](https://travis-ci.org/AnguleMathias/StackOverflow-lite_API_v1.svg?branch=develop)](https://travis-ci.org/AnguleMathias/StackOverflow-lite_API_v1)
[![Coverage Status](https://coveralls.io/repos/github/AnguleMathias/StackOverflow-lite_API_v1/badge.svg?branch=develop)](https://coveralls.io/github/AnguleMathias/StackOverflow-lite_API_v1?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/9a5fcbd2a03a937ee335/maintainability)](https://codeclimate.com/github/AnguleMathias/StackOverflow-lite_API_v1/maintainability)


## Features

* Post a question
* Fetch a single question
* Fetch all questions
* Post an answer

## Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|/api/v1/questions|Add a question
GET|/api/v1/questions/<question_id>|Fetch a specific question
GET|/api/v1/questions|Fetch all questions
POST|/api/v1/questions/<question_id>/answer|Add an answer to a specific question
GET|/api/v1/answers|Fetch all questions with the answers

## Deployment

Click to access [hosted app](https://stackoverflow-lite-mathias.herokuapp.com/api/v1/questions)

## Tools Used

* [Flask](http://flask.pocoo.org/) - Framework for Python
* [Virtual environment](https://virtualenv.pypa.io/en/stable/) - tool used to create isolated python environments
* [pip](https://pip.pypa.io/en/stable/) - package installer for Python


## Getting Started


* Clone the project into your local repository using this command:

            `git clone https://github.com/AnguleMathias/StackOverflow-lite_API_v1.git`

* Change directory to the cloned folder using the following command for Windows, Linux and MacOS

            `cd StackOverflow-lite`

* If you do not have a virtual environment installed run the following command, else follow the next steps.

            `pip install virtualenv`
            
* Create a virtual environment(for Windows, Linux and MacOS)

            `virtualenv venv`

* Activate the virtual environment(Windows only)

            `source venv/Scripts/activate`

     and for Linux and MacOS

            `source venv/bin/activate`

* Install the app dependencies.(for Windows, Linux and MacOS)

            `pip install -r requirements.txt`

* Run the app(for Windows, Linux and MacOS)

            `python run.py`


## Running the tests

* Install pytest while the virtual environment is active

            `pip install pytest`

* Run the tests.

            `pytest`
