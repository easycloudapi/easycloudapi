# Developer Guide


## Ref:
1. How to create python package:
    1. https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/
    2. setup.cfg documents: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
2. ReadTheDocs Documentation:
    1. https://docs.readthedocs.io/en/stable/tutorial/index.html
    2. sphinx: https://sphinx-tutorial.readthedocs.io/
    3. https://docs.readthedocs.io/en/stable/config-file/v2.html
    4. https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.html.DirectoryHTMLBuilder


## Pre-requisite:
1. Account Setup:
    1. Github Account - https://github.com
    2. TestPypi Account setup - https://test.pypi.org
    3. Pypi Account Setup - https://pypi.org
    4. ReadTheDocs Account Setup - https://readthedocs.org/accounts/signup/
2. Softwares/Tools in your machine:
    1. setup ".pypirc" file inside $Home folder 
    2. VS code
3. Knowledge:
    1. Python
    2. SQL
    3. Git
    4. Google Cloud Project (*optional*)
    5. Azure Cloud (*optional*)
    6. Amazon Web Service (*optional*)


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
4. Git clone the repository
    ```shell
    git clone https://github.com/easycloudapi/python_utility.git
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

7. Locally install the package for testing (run from root dir where setup.py or setup.cfg available):
    ```shell
    pip install -e .
    pip uninstall easycloudapi
    ```

8. Install twine which will copy the code to `testpypi` and `pypi`:
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

9. Setup ReadtheDocs Setup:
    ```shell
    pip install sphinx

    cd docs
    sphinx-quickstart  # follow instruction as per cli guide

    # will create html files inside build/html
    .\make html

    # test the html file
    cd build/html
    explorer index.html
    # or
    explorer .\build\html\index.html

    # to remove everything from build
    cd docs
    .\make clean  
    ```
