**ROJECT FOLDERS**

- `/app` 
-- This folder contains the main application files 
- `/app/templates`
-- This contains all the html files for this project
- `/app/static`
-- This folder contains all static files such as (.css) files and javascript(.js) files
- `/app/routes`
-- This folder contains application views such as `cart` , `categories`, `orders`, `users`, `products`
- `config.py`
-- This file contains application configurations
- `models`
-- This files is where all application models are defined

- `run.py`
-- This is the application entry point

- `database.db`
-- The Actual project database

**Getting Started**
### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
- This following programs are required to run this project
- ```Python 3.6 + ```
- ```Pip 19+ ```


#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Requirements.txt
After the virtual environment setup, install project dependencies by typing the following command
`pip install -r requirements`
*NB* Make sure you are working withing the virtual environment setup above

## Setting environment variables
Type the following commands to start the server
`export FLASK_APP=run.py`
`export FLASK_ENV=development` //To run the app in debugging mode

#### Migrations (If you want to setup a new Database)
 [Flask-Migrate Docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
 - `flask db init`
 - `flask db migrate`
 - `flask db upgrade`
 #### Running Server

 `flask run`



 