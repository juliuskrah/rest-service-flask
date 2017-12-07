# REST Application using Flask
This is a simple `CRUD` application for a RESTful webservice using Flask.

## Getting Started
To setup this service locally, you require
- Python 3.5
- Pip

```bash
> pip install virtualenv
> virtualenv venv
> venv\Scripts\activate   # source etc\bin && activate -- on Unix Systems.
(venv) > pip install -r requirements.txt
> set FLASK_APP=app.py    # export FLASK_APP=app.py -- on Unix
> flask run
```