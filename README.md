<h1 align='center'> LIA: your API to document books read and get book recommendations </h1>

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"/>

LIA (Library In API) is an API created with Python, FastAPI and SQLite to save information about the books you read and get book recommendations. These recommendations are calculated using the cosine similarity. Read more about this metric <a href="https://naomy-gomes.medium.com/the-cosine-similarity-and-its-use-in-recommendation-systems-cb2ebd811ce1">here</a>.

Structure of the project:

<pre>
<code>
├── LIA-FastAPI-SQL
│   ├── crud
│   │    ├── __init__.py
│   │    ├── crud_books.py
│   │    ├── crud_recommendation.py
│   │    ├── crud_stats.py
│   │    └── crud_users.py
│   │        
│   ├── data   
│   │    ├── __init__.py
│   │    ├── data.csv
│   │    └── heart.csv     
│   │    
│   ├── endpoints
│   │    ├── __init__.py
│   │    ├── books.py
│   │    ├── stats.py
│   │    └── users.py   
│   │        
│   ├── routes  
│   │    ├── __init__.py
│   │    └── api.py         
│   │   
│   ├── schemas 
│   │    ├── __init__.py
│   │    ├── books.py
│   │    └── users.py  
│   │
│   │ 
│   ├── __init__.py
│   ├── main.py
│   ├── Dockerfile
│   ├── models.py
│   ├── sqlapp.db
│   ├── README.md
│   └── requirements.txt
</code>
</pre>

- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/tree/main/crud">crud</a>, we have all the functions created to interact with the database, creating, requesting and deleting data about users and books. 
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/tree/main/data">data</a>, is where the SQL database and the corresponding csv file are created.
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/tree/main/endpoints">endpoints</a>, all the endpoints of the API are defined.
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/tree/main/routes">routes</a>, all the API routes are defined.
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/tree/main/schemas">schemas</a>, the structure of the data on users and books accepted by the API is defined. 
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/blob/main/main.py">main</a>, we have the main file where FastAPI is initialized.
- In <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/blob/main/models.py">models</a>, the structure of the databases for users and books is defined. 

## Running the API

1. Clone the repository

```
git@github.com:naomyduarteg/LIA-FastAPI-SQL.git
```
2. Create a virtual environment

```
python3 -m venv <name_of_venv>
```
3. Go to the virtual environment's directory and activate it

For Windows:
```
Scripts/activate
```
For Linux/Mac:
```
bin/activate
```
4. Install the requirements

```
pip install -r requirements.txt
```

6. Run the API with uvicorn

```
uvicorn main:app --reload
```

From this point, one can use the Swagger documentation to test the API. 

## Docker 
We can use the <a href="https://github.com/naomyduarteg/LIA-FastAPI-SQL/blob/main/Dockerfile">Dockerfile</a> to create an image for running our application inside a container. 
First, build the image

```
docker build . -t LIA-FastAPI-SQL
```
Start the Docker container based on the created image

```
docker run -p 8000:8000 LIA-FastAPI-SQL
```

