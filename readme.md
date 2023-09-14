# REST API Project with a Database Interface

## Description
This project provides an implementation of a simple REST API that allows managing users in a database. Users can add, update, retrieve, and delete users. When attempting to add a user with an ID that already exists in the database, the system automatically assigns the next available ID.

**Key features of the project:**
- CRUD (Create, Read, Update, Delete) implementation for users.
- Use of Flask library to handle HTTP requests.
- Integration with the database using `pymysql` and secured database queries.
- Automatic ID assignment in case of conflict.
- API configuration via the database.

## Installation and Setup
Before starting, ensure you have the required libraries installed:
<pre>pip install Flask pymysql</pre>

Then, run the main project file:
<pre>python rest_app.py</pre>

## Documentation
For more details and comprehensive documentation, refer to the `docs` directory.

## Requirements
- Python 3.8+
- Flask
- pymysql

## Installation
1. Clone the repository:
First, clone the repository to your local machine:
<pre>git clone https://github.com/janq79/WebRESTApp.git</pre>

2. Set up a virtual environment:
In the project's root directory, create a virtual environment and activate it:
<pre>
python -m venv venv
source venv/bin/activate  # On Unix/Linux systems
venv\Scripts\activate     # On Windows
</pre>

3. Install the required libraries:
Install the necessary libraries from the `requirements.txt` file:
<pre>pip install -r requirements.txt</pre>

## Usage
1. Running the application:
To start the app, navigate to the project's main directory and use the following command:
<pre>python rest_app.py</pre>

2. Interacting with the application:
The application operates on a local server at http://127.0.0.1:5000/. To add a user, you can use tools like Postman or a browser to send the appropriate requests to the server.

Example request to add a user:
<pre>POST http://127.0.0.1:5000/users/1</pre>
With a request body in JSON format:
<pre>
{
  "user_name": "Jan Kowalski"
}
</pre>

3. Stopping the application:
To stop the app, press Ctrl+C in the terminal where it's running.

## Author
Jan Grabowski