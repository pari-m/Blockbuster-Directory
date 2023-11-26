---
## About
Welcome to my collection of film data

## Features

- [x] ORM with Sqlalchemy
- [x] Simple FastApi server
- [x] API documentation using Swagger UI
- [x] Basic CRUD for Films
- [x] Postman collection with sample requests
- [x] A basic Ansible config for standing up the server this can be found under /ansible/ansible.yaml


## Todo

- [ ] Add auth
- [ ] Setup some from of CD such that pusing to github automatically updates the app
- [ ] Add more tables to the API 
- [ ] Setup SSL on the server, SSL is currrently coming from Cloudflare

<br>

## Sample for intrecration

https://films.133t.net


## Documentation 

You can see the API documentation by going to the /docs/ path

https://films.133t.net/docs/

## Dependencies

- Python 3.11+
- Pip
- Other listed in requirements.txt

## Running the app locally

- Clone the repo


- Create a Virtual Environment using

```bash
sudo pip install virtualenv
virtualenv venv
```

- Activate the virtualenv

```bash
source /venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Set the envoirement variable

| Key     | Value |
| ----------- | ----------- |
| DATABASE_URL   | postgresql://user:password@host:port/db|

- To run the project

```bash
uvicorn app.main:app
```
---