### Hexlet tests and linter status, Maintainability:
[![Actions Status](https://github.com/Abra19/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abra19/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f9b2728037c913a8c25c/maintainability)](https://codeclimate.com/github/Abra19/python-project-49/maintainability)


### Requirements
1. Python >=3.8.1
2. pip >= 19
3. poetry >= 1.2.0

### To get started
1. Clone git repo:
  `git clone git@github.com:Abra19/python-project-49.git`
2. Go to directory python-project-49:
  `cd python-project-49`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virual environment and Install dependencies
  `make install`
5. Build package
  `make build`
6. Publish package:
  `make publish`
7. Installing the package in the user's environment:
  `make package-install`
8. If you receive a tracking warning at step 7:
  `WARNING: The script brain-games is installed in 'path/to/your/executable' which is not on PATH.`
  Add this directory to PATH:
  `export PATH=$PATH:'path/to/your/executable'`
9.  Run the programme:
  `brain-games`