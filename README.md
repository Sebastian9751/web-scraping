# Web scraping API with Selenium and PostgreSQL.




#### This api returns a list of motorcycle types, after obtaining them by web scraping .

## Configuration

#### Before running the application, ensure that you configure the following environment variables:

```bash
#These variables are necessary to connect to PostgreSQL

DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=root
DB_PASSWORD=root
DB_NAME=mydb

```
#### Install the dependencies using pip:

```bash
$ pip install -r requirements.txt
```

## Docker 

#### Using docker-compose.yml

#### Ensure that Docker is installed on your machine.

#### Execute the following command to create a Docker container for SQL server:

```bash
# This will create a Docker container for the PostgreSQL server.

$ docker-compose up
```

## Running the Server


```bash
# Launch application

$ uvicorn main:app 
 
```

## Swagger

#### Swagger is a tool used for API documentation and testing

#### Once the application is running, you can access Swagger at the following URL:

```bash
http://127.0.0.1:8000/docs
```

