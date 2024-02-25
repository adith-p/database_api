#  SchemaDB API

This repository provides an API interface to access a database with real-time table creation, updating, and data insertion functionalities.

## Overview

The Realtime Database API allows users to interact with a database through a set of defined endpoints. It offers dynamic table creation on-the-fly, updating existing tables, and inserting new data seamlessly.

## Features

- **Real-time CRUD**: Tables are created dynamically as needed based on user requests.

- **RESTful API**: The API follows REST principles for easy integration and usage.

- **Error Handling**: Comprehensive error handling to provide informative responses.

## Installation

To install and use the Realtime Database API, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/adith-p/database_api.git
    ```

2. Install the necessary dependencies. Ensure you have [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) installed. Then, run:

    ```
    pip install -r requirements.txt
    ```

3. Configure the database connection settings in `database.py` file.

4. Run the API server:

    ```
    uvicorn main:app
    ```

