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
- `models.py`
-- This file is where all application models are defined

- `run.py`
-- This is the application entry point

- `database.db`
-- The Actual project SQLite database

**Getting Started**
### Installing Dependencies

- This following programs are required to run this project
- ```Python 3.6 + ```
- ```Pip 19+ ```

If you don't have python and pip installed, follow these instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
and [Pip docs](https://pip.pypa.io/en/stable/installing/) to install the latest version of pip.


#### Requirements.txt
install project dependencies by typing the following command
`pip install -r requirements.txt`

## Setting environment variables
Type the following commands to start the server

***On Bash***

`export FLASK_APP=run.py` //Tell flask the file which contains flask instance
`export FLASK_ENV=development` //To run the app in debugging mode

***On Windows Default Command-Line***

`SET FLASK_APP=run.py`
`SET FLASK_ENV=development`

 #### Running Server

 `flask run`

 #### Accessing the Store

 After running the server, access the store home page using any browser
 through the following url:
 http://127.0.0.1:5000/store/



 
