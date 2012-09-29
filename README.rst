py-system-status
================

Simple Sytem Status Web Front for Linux Servers

requirements:

* `flask-peewee <https://github.com/coleifer/flask-peewee>`_
* python 2.5 or greater

.. image:: http://i.imgur.com/suBE0.png


installing
----------

I recommend installing in a virtualenv.  to get started::

    # create a new virtualenv
    virtualenv --no-site-packages project
    cd project/
    source bin/activate

    # install this project (will install dependencies as well)
    pip install git+https://github.com/dahool/py-system-status.git


initial setup
-------------

Create the database (by default, a sqlite db is used, it doesn't need a greatest db engine)

    python syncdb.py
    python createsuperuser.py
    
running
--------
    
    python run.py

Navigate to:

http://127.0.0.1:5000/
