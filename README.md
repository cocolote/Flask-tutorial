# Flaskr
---

Flask tutorial app. Basic to learn how to create a login page, connect an
application with a DB on Sqlite and basic interaction

---

### Installation:

* Clone the repo

* Create a virtual enviroment `mkvirtualenv flaskr`

* Iside the app directory run `pip install requirements.txt this will install all
the required libraries into the virtualenv 

* To create the DB, enter in python shell command line `python`

* Inside the shell execute this commands:
```
 >>>> from flaskr import init_db
 >>>> init_db()
```

* If everithin went right, now you are ready to execute the app `python flaskr.py`

* Also you could run the test like `python flaskr_test.py`
