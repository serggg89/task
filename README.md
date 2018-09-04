# task
project structure:
/models - package with models. I map all response to JsonObject. It help to validate responses. 
moreover the method __eq__ also added to the model

/constants - constants and test data. 

/api_tests - package with tests

pytest.ini - file with pytest configuration

requirements.txt  - list of used libs



I added checking of status code, because according to the REST spec the server should send 401 (Unauthorized)
after that I map response to the JsonObject. It validate json structure, types of data and required fields.
In the models I create method __eq__ it helps compare two objects
  