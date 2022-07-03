# django-template

Installation tested on Ubuntu 20.04.1 LTS.

## Table of contents
- [dev enviroments](#dev-env)
  - [docker](#docker)
  - [virtualenv](#virtualenv)
    - [Install pre-installation dependencies](#install-pre-installation-dependencies)
    - [Setup postgreSQL (database)](#setup-postgresql-database)
      - [Create .env file](#create-env)
      - [Setup dev enviroment](#setup-dev-env)
      - [Setup de Database and start the project](#create-a-database-and-database-user-for-development)
      - [Create and activate virtual enviroment and install python dependencies](#create-a-virtual-enviroment)
      - [Test the setup](#test-the-setup)
    - [API documentation](#api-docs)
    - [Testing](#testing)
- [References](#references)

## Dev envcioremtns <a name="dev-env"></a>

We offer two main ways to develop in the backend

### Docker (easiest) <a name="docker"></a>

You can opt to use a simple command with docker and docker-compose, that instanciate every resource in a private network, it will let you develop the easiest and will work in every OS.

Make sure you have installed python, docker and docker-compose, and then.

Run this script in the root of this repo (it will download, install and start every component, and will show you the url you can visit to see the results of your page).

```shell
python3 dev
```
Run this, if you want to terminate all instance for dev.

```shell
python3 dev --stop
```

This form of developing is a little bit slow and error prone (you will be doing reset of the enviroments when the is a fatal error), so take that into account.

### Virtual env (prefered) <a name="virtualenv"></a>

This method is tested to work on linux, and is the most confortable for developing, because is faster in dev time, but need some pre working to start the enviroments

### Install pre-installation dependencies <a name="install-pre-installation-dependencies"></a>

- Python3
  Should come preinstalled with Ubuntu

- Pip3 and NodeJs
  Installation on Ubuntu
  `sudo apt install python3-venv python3-pip nodejs`

**Install yarn the package manager for nodejs**

`npm install --global yarn`

### Setup postgreSQL (database) <a name="setup-postgresql-database"></a>

`sudo apt-get install libpq-dev postgresql-12`

### Create .env file <a name="create-env"></a>

Edit `.env.example` with your own settings and rename it `.env`

### Setup dev enviroment <a name="setup-dev-env"></a>

```bash
source ./scripts/start.sh
```

#### Create and activate virtual enviroment and install python dependencies <a name="create-a-virtual-enviroment"></a>

```bash
setup_venv
```

#### Setup de Database and start the project <a name="create-a-database-and-database-user-for-development"></a>

```bash
setup_db
```

#### Test the setup <a name="test-the-setup"></a>

Test the setup by running the development server

```bash
runserver
```

### API documentation <a name="api-docs"></a>

Documentation can be found in the url `api/schema/swagger-ui/` and `schema/redoc/`. You'll be to need authenticated as admin.

### Autodocumentation <a name="autodocumentation"></a>

#### Visualize Dependencies Graph

Generate a special django model digram and it's relations with other apps.
[Follow this tutorial for ubuntu install](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

Run this command to generate diagram

```bash
python manage.py graph_models
```

Config settings are in the file `project/project/settings/development.py`

[Find out more about graph_models][graph-models]


## Testing <a name="testing"></a>

For testing, the project use `PyLint` and `PyTest`, and once you sourced the `dev/script.sh`, you can run your test as:

```bash
pylint
```

```bash
pytest
```

## References <a name="references"></a>

- [Steps followed to install oscar][oscar-install]
- [Steps followed to setup django with postgreSQL][postgre]
- [Steps followed to install oscar-api][oscar-api-install]
- [Directory structure explanation](https://stackoverflow.com/questions/22841764/best-practice-for-django-project-working-directory-structure)
- [Graph models][graph-models]
- [Fork Oscar App][fork-oscar-app]

[oscar-install]: https://django-oscar.readthedocs.io/en/2.1.0/internals/getting_started.html
[postgre]: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
[oscar-api-install]: https://github.com/django-oscar/django-oscar-api
[graph-models]: https://django-extensions.readthedocs.io/en/latest/graph_models.html
[fork-oscar-app]: https://django-oscar.readthedocs.io/en/2.1.0/topics/customisation.html#fork-oscar-app
[sphinx]: https://www.sphinx-doc.org/en/master/
