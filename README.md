# rest_api_ml_model
Api that allows you to interact with the machine learning model.


## build
```bash
docker build -t rest_api_ml_model .
```

## start
```bash
docker run -p 5000:5000 rest_api_ml_model
```

## stop
```bash
ctrl + c 
```

### Contain: 
- app.py - Flask api
- class_perceptron.py - perceptron model definition
- model.pkl - ML model
- requirements.txt - environmental requirement
- Dockerfile - environment
- api_test.ipynb - Verification that the api is working properly
