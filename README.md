[![Build Status](https://travis-ci.org/dwyl/esta.svg?branch=master)](https://travis-ci.org/dwyl/esta)

## Django Quiz Web Application ##

Current features
----------------
Features of each quiz:
* Question order randomisation
* Storing of quiz results under each user
* Previous quiz scores can be viewed on category page
* Correct answers can be shown after each question or all at once at the end
* Logged in users can return to an incomplete quiz to finish it and non-logged in users can complete a quiz if their session persists
* The quiz can be limited to one attempt per user
* Questions can be given a category and subcategory
* Success rate for each category can be monitored on a progress page
* Explanation for each question result can be given
* Pass marks can be set
* Multiple choice question type
* Display an image alongside the question
* Custom message displayed for those that pass or fail a quiz
* Custom permission (view_sittings) added, allowing users with that permission to view quiz results from users
* A marking page which lists completed quizzes, can be filtered by quiz or user, and is used to mark essay questions
* After selecting a larger pool of questions, a quiz can be set to show a random subset rather than all within the pool
* Start and end times for sitting exams are recorded


**Getting started**

```
pip install -r requirements.txt

python3 manage.py collectstatic

python3 manage.py makemigrations

python3 namage.py migrate

```


![Image 1](/quiz_github/1.png)
