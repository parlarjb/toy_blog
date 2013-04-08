# Description #

This is an incredibly simple blogging platform, written to re-introduce myself to Django.

# Installation #

I took a few hints from the excellent [Two Scoops of Django](https://django.2scoops.org) book. The most 
important being the separation of `settings.py` into `base.py`, `local.py` and `production.py`. The intent of this is to avoid the old `local_settings.py` pattern that so many people use, and allow us to keep *all*
configuration files in source control.

This does bring up the old question of "Where do you keep your passwords and secret keys?" The suggestion
from Two Scoops is that you create environment variables for those on your development and production 
machines. This requires that you have some process in place for storing and tracking these values, but
it ends up working out really nicely in the end.

I assume that you have `virtualenv` and `virtualenvwrapper` installed. I'm going to show the install process
for a production deployment, as it's a bit more complicated than a local one.

### Create/configure virtualenv ###

    mkvirtualenv production --no-site-packages

We then need to put a few environment variables into `bin/activate` of the virtualenv, to ensure
that they're always present when running in the virtualenv. Add the three following lines to the
end of `bin/activate`:

    export DATABASE_PASSWORD="ENTER_YOUR_PASSWORD_HERE"
    export SECRET_KEY="SOME_DJANGO_SECRET_KEY"
    export DJANGO_SETTINGS_MODULE="toy_blog.settings.production"

The first two are self explanatory. The third is a variable you might be familiar with, but don't often 
use. When we have multiple possible settings files in the source code, it's easier to just specify
the one we want as an environment variable, rather than pass `--settings=toy_blog.settings.production`
around all over the place.

Finally, activate your virtualenv

    workon production

### Checkout the code ###

    it clone git://github.com/parlarjb/toy_blog.git

### Install requirements ###

    pip install -r requirements.txt


### Create the Postgres user and database ###

I'm assuming here that you already have Postgres installed. This is mostly documentation for myself
so I don't forget what to do. We're going to create a Postgres user called `django_login`, and then
create a database with that user as the owner. I'm assuming you already have a user called `postgres`
on your system, and that you have the password for that user (so you can `su`)

    sudo -u postgres createuser -P django_login
    su postgres
    psql template1
    CREATE DATABASE django_db OWNER django_login ENCODING 'UTF8';


### Insert our tables into the database ###

Since we used South for migrations, this is a two-step process.

    python manage.py syncdb
    python manage.py migrate

### Collect static files ###

The location on your server for the static files is stored in `settings/production.py` as the `STATIC_ROOT`
variable. Change this to whatever is appropriate for you. Then, run:

    python manage.py collectstatic


### Run gunicorn ###

I'm using gunicorn to run the app, because it seems to be the recommended method these days. I've included
a super-simple config file, so you should be able to do:

    python manage.py run_gunicorn -c gunicorn.conf.py

If you want that to daemonize, then make sure to add `--daemon` to the end of the command
    

### nginx ###

I'm also using nginx, for the same reason I'm using gunicorn. I included a `nginx.conf` file that I used.
You'll definitely need to change the `server_name` directive, but otherwise I believe it's fairly standard.

Put it into whatever location nginx is expecting, start it up, and you should be good to go!

