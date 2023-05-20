# Test App

## Application URL`s

| **Service**   | **URL**                                     |
|:--------------|:--------------------------------------------|
| Swagger       | http://0.0.0.0:8080/docs                    |
| Send question | http://0.0.0.0:8080/api/send?chunk_size=100 |

## Tech details

|      **Resource**      | **Resource Name** | **Version** |
|:----------------------:|:-----------------:|:-----------:|
|  Programming language  |      python       |    3.10     |
| Back-end web framework |      fastapi      |   0.95.2    |
|       Web server       |      Uvicorn      |   0.22.0    |

## Run command with docker

Run project with docker.
You need install docker

```commandline
docker-compose up --build
```

## Run commands

|**PARTH**|                  **Commands**                  |           **Description**           |
| :-: |:----------------------------------------------:|:-----------------------------------:|
|Requirements|        pip install -r requirements.txt         | this installed dependencies to venv |
|Start server|uvicorn app.main:app --host 0.0.0.0 --port 8080 |       <http://0.0.0.0:8080/>        |
|Stop server|                    ctrl + C                    |   |


## Dev environment deployment

Populate `Environment variables` of your system with the following:

```bash
export API_KEY
export OPENAI_API_KEY
export FILE_PATH
```

Then install all the required packages:

```bash
user@host$ cd TestApp/
user@host$ pip install -r requirements.txt
user@host$ ./manage.py runserver
```

Standard message example
```bash
{
    "msg": "Tell me about Nifty Bridge"
}
```
