# Testing instructions

## Unit Tests

- Run the tox.ini file located in the root directory. This will run the integration test as well but it will pass without a JSON sample.

```console
pip install tox
tox
```

## Integration Test

- Create a JSON file called *sample.json* in a different folder.  
- Save the absolute path to *sample.json* in the environment variable 'META_JSON_FILE_PATH'.
- Run the tox.ini file as mentioned above or execute the test manually:

```console
pip install pytest
pytest tests/integration
```

- The test will create three JSON files with every method's result in the selected folder.

