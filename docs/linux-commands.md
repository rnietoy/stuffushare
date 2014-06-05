Useful Linux Commands
=====================

A list of useful commands here

### Install Python 3
```
sudo apt-get install python3
sudo apt-get install python-pip
```

### Install virtual env ###
sudo pip install virtualenv

Note that virtualenv is a python thing, it is not specific to django. It allows you to have
different virtual environments for different python projects. So, when we install django, we actually
install it while inside a virtual environment (in this case, stuffushare).

pip is python's package management system.

### Create a virtualenv for stuffushare
``` virtualenv -p /usr/bin/python3 stuffushare ```

This will create a directory called stuffushare, and create a virtual environment inside that
directory.

### Activate the virtual env
cd stuffushare
. bin/activate

### Deactivate the virtual env
deactivate

### Checkout files from git (first time)

cd to the local copy where the repository will be

```
git init
git remote add origin https://github.com/rnietoy/stuffushare.git
git pull origin master
```

### Turn off / shutdown linux box

shutdown -h now

### Creating a django project

1. Activate your virtualenv
2. Navigate to where you want to create your project
3. django-admin.py startproject boardgames

Note that virtual envs can be separate from the actual project files. This might be a typical way
of doing things, as this is what is shown in the pluralsight training videos.

This is what I have inside my ~/sandbox/python directory:
envs/boardgames <- this is the boardgames virtual environment. It has django installed.
dev/boardgames <- this is the boardgames django project

### start django server ###
1. activate your virtualenv
2. python manage.py runserver 0.0.0.0:8000

netstat -an | grep "LISTEN "

rafa@rafa-ubuntu:~$ netstat -an | grep "LISTEN "
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN
tcp6       0      0 :::22                   :::*                    LISTEN

### Python package manager
http://www.pip-installer.org/en/latest/index.html

### Resolve a Git merge conflict

Here is the scenario:

1. git pull origin master
    - error is shown as follows: Merge conflict in "linux-commands.md"
2. Open linux-commands.md in text editor, manually fix (look for the conflicts marked by <<<<< lines)
3. git add . <- to add all files that have changed, or
   git add <file name> <- if you want to specify the file specifically
4. git commit -m "resolved conflix so and so"
5. git push origin master

Done!
