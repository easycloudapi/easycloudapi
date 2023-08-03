# Developer Guide


## Ref:
1. How to create python package:
    1. https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/
    2. setup.cfg documents: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
    

## Steps to follow in windows machine:
1. Create and Activate Python Virtual Environment
    ```shell
    python -m virtualenv .venv
    .venv\Scripts\activate
    ```
2. Set the python interpreter, press "ctrl + shift + p", then choose "python interpreter" and select venv python version.

3. *(optional)* if any error while activate the virtual env, follow below steps-
    ```shell 
    get-ExecutionPolicy
    Set-ExecutionPolicy Unrestricted -Scope Process  # if its restricted, then execute this command
    ```

4. Install the python dependencies
    ```shell
    python -m pip install --upgrade pip 
    pip install -r .\requirments.txt
    ```

5. Exceute the codes from IDE (VS code):
    ```shell
    cd python_utility
    python .\src\easycloudapi\gcp\bigquery\bigquery_schema.py
    python .\src\easycloudapi\generic\datetime\generate_date_dimention.py
    ```

6. Configure to build the package locally:
    ```shell
    py -m pip install --upgrade build
    py -m build  # will create the dist folder with source archive & built archive
    ```

7. locally install the package for testing (run from root dir where setup.py or setup.cfg available):
    ```shell
    pip install -e .
    pip uninstall easycloudapi
    ```

8. install twine which will copy the code to testpypi and pypi:
    ```shell
    py -m pip install --upgrade twine  # will upload distribution archive into testpypi or pypi

    # testPyPi - https://test.pypi.org/project/easycloudapi/0.0.1/
    # create testpypi account (https://test.pypi.org/), activate testPyPi account, 
    # create api token, store it under ".pypirc" as documented or generated.
    cd $Home
    touch .pypirc  # store the token

    # upload the package from local dist to testPyPi
    py -m twine upload --repository testpypi dist/*
    # or 
    py -m twine upload --skip-existing --repository testpypi dist/*

    # PyPi - https://pypi.org/project/easycloudapi/0.0.1/
    # create pypi account (https://pypi.org/), activate PyPi account, 
    # create api token, store it under ".pypirc" as documented or generated.

    # upload the package from local dist to PyPi
    twine upload dist/*  # --repository pypi 
    ```
