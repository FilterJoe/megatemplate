Django and Zurb on DotCloud
===========================

Template requires:

Django 1.4.3
Python 2.7
Zurb Foundation 3

Template bundle includes support for:

dotcloud
postgreSQL db: on server: "happydb"
postgreSQL db: on local bitnami development environment: "djangostack"

Still left to do:

admin.py (with a sample commented out)
model.py (a sample commented out)

This template is mostly pulled from the DotCloud tutorial, but updated for Django 1.4.3.
I also changed the name to megatemplate and the app to app1.

Once I've refined this, it will serve as a template for all of my projects.
The things I will need to change when starting a project (assumes you're using
PyCharm as your editor. If you aren't you'll have to substitute with the equivalent
from your editor or using command line.

1) git clone this template.
2) Copy to another directory with your new project name (cp -r megatemplate yourprojectname)
3) Open in PyCharm
4) Rename the projects subdirectory to the name of your project. Then tell Pycharm where the settings.py file is:
   file/settings/Django Support
5) Create an app (startapp in manage.py) with an appropriate name
6) change project and app names as follows:
    * any reference to project/app names in the settings.py file
    * project name in manage.py
    * change import statement in urls.py file to your app name
    * change 2 hardcoded app names in wsgi.py file
    * change app name in postinstall file
7) manage.py syncdb
8) South:
   schemamigration --initial
   migration yourappname --fake
   it will not work unless you do --fake, because I already used south on this once when setting it up.  --fake allows
   South to work on a new system even after it's already been run before on a different system.
9) use git to share your project on github. In Pycharm: VCS/Import into Version Control/Share project on GitHub
   check your github account to make sure the entire project is there.
10) Open up a command line. Type: compass watch
11) Open up a new command line window:
    dotcloud setup (to connect to your dotcloud account)
    dotcloud create --git yourprojectname (yourprojectname will be part of url)
    dotcloud push
    NOTE: the --git is there to insure that only changes you committed to git will ever be pushed
    to your deployed project at dotcloud. You could do this manually with each push but if you want
    to use git consistently throughout your project, this is a better way to do it - every use of
    the "dotcloud push" command thereafter will automatically assume --git.

    Your template should be live!





Notes to self:

At first I mostly ignored bitnami stack and created all new virtualenv. However, I found the bitnami
stack useful as it handled the complexity of getting postgre server going. So I eneded up using bitnami
stack exclusively in the end, because to not do so was causing issues of UCS-2 vs UCS-4 (incompatible
compilations).

Once I go beyond the first project, I'll need to create new postgres databases. Here's the manual way:
(but I think bitnami provided an easier way which I can access according to these docs:
http://wiki.bitnami.org/Virtual_Appliances_Quick_Start_Guide#How_to_access_the_BitNami_Virtual_Appliance.3f)



psql -U postgres  # gets me into postgres shell

password: bitnami

\password postgres   # to change password of postgres user

\l # lists databases
\q # quit

and here's how to create a new user/db/pwd:

(the next command below has a -d to give database create privilege)
(see http://www.postgresql.org/docs/8.4/static/app-createuser.html)

    $ createuser yournewuser -d -P
    Enter password for new role:
    Enter it again:
    Password: [enter my superuser password here]

Once you have created your new database user and set a password,
you can now create your database and tell this new database that it is used by your new user.

    $ createdb -U yournewuser -E utf8 -O yournewuser yournewdb -T template0

and use dropdb command to remove db.



See text below for the text that was included by the dotcloud folks:

This code shows how to run a very simple Django application on DotCloud.
It is fully functional, in the sense that you don't have any hand-editing
to do to deploy it: it automatically deploys a PostgreSQL database,
includes it in ``settings.py``, creates a superuser for you, and uses
Django 1.3 ``collectstatic``. *Batteries Included!*

To run this code on DotCloud, you need a `DotCloud account
<https://www.dotcloud.com/accounts/register/>`_ (free tier available).
Then clone this repository, and push it to DotCloud::

  $ git clone git://github.com/dotcloud/django-on-dotcloud.git
  $ cd django
  $ dotcloud push hellodjango

Happy hacking! Remember: each time you modify something, you need to
git add + git commit your changes before doing ``dotcloud push``.

This repository is also a step-by-step tutorial: each commit corresponds
to one step, with the commit message providing explanations.

You can view the whole tutorial, and the modified files at each step,
with at least three different methods:

* by using GitHub's awesome `compare view
  <https://github.com/dotcloud/django-on-dotcloud/compare/start...finish>`_:
  you will see the list of commits involved in the tutorial, and by
  clicking on each individual commit, you will see the file modifications
  for this step;
* by running ``git log --patch --reverse begin..end`` in your local
  repository, for a text-mode equivalent (with the added benefit of being
  available offline!);
* by browsing a more `traditional version
  <http://docs.dotcloud.com/tutorials/python/django/>`_ on DotCloud's
  documentation website.

You can also learn more by diving into `DotCloud documentations
<http://docs.dotcloud.com/>`_, especially the one for the `Python service
<http://docs.dotcloud.com/services/python/>`_ which is used by this app.



