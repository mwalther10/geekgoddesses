# geekgoddesses


In order to see the full demo version of **Shopping Bud** you need to start the backend and then the frontend service.
## shopping bud svelte app

start by installing locally all node modules necessary: 
```bash
npm install
```

run development server:
```bash
npm run dev
```

other scripts to build and start the app:
```
npm run build
npm run start
```
The web-application is meant to prototype an app for smartphones and mobile devices, s.t. the user can carry her/his shopping bud with him/her all the time. 


## shopping bud backend

The backend consists of a Flask API querying data from the [**Open Food Facts API**](https://de.openfoodfacts.org/). We decided to enrich the data which was given from the challenge setters to better match our business case. We think that the same type of data is also available within the infrastructure of Schwarz IT.

Requirements:
- [Flask](https://pypi.org/project/Flask/)
- [Flask Cors](https://pypi.org/project/Flask-Cors/)
- [openfoodfacts python client](https://github.com/openfoodfacts/openfoodfacts-python)
- [gevent](https://pypi.org/project/gevent/)
- python 3.9

All requirement can be installed with PyPI.

How to start the backend:
```
cd shopping-bud/backend
python backend.py

```


