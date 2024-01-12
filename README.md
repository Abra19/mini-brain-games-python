### Hexlet tests and linter status, Maintainability:
[![Actions Status](https://github.com/Abra19/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abra19/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/f9b2728037c913a8c25c/maintainability)](https://codeclimate.com/github/Abra19/python-project-49/maintainability)


### Descriptions
This project implemented a set of mini-games launched from the console:
  * check is the number even
  * make calculation
  * find great common divisor
  * find hidden element of the progression
  * check is the number prime
  
### Requirements
1. Python >=3.8.1
2. pip >= 19
3. poetry >= 1.2.0

### To get started
1. Clone git repo:
  `git clone git@github.com:Abra19/mini-brain-games-python.git`
2. Go to directory mini-brain-games-python:
  `cd mini-brain-games-python`
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

### To Run
Install package and run `brain-games` for welcome message:

[![asciicast](https://asciinema.org/a/4YrcE5Nbsc3i7gNtZzAlJ7YRZ.svg)](https://asciinema.org/a/4YrcE5Nbsc3i7gNtZzAlJ7YRZ)

Run `brain-even` for check is the number even:

[![asciicast](https://asciinema.org/a/UBf9qlfEAsyu7HymqeVDfIBp7.svg)](https://asciinema.org/a/UBf9qlfEAsyu7HymqeVDfIBp7)

Run `brain-calc` for calculations:

[![asciicast](https://asciinema.org/a/pKNBygPkjJcvsDwaWMu6CpRTI.svg)](https://asciinema.org/a/pKNBygPkjJcvsDwaWMu6CpRTI)

Run `brain-gcd` to find great common divisor:

[![asciicast](https://asciinema.org/a/8LPsUDcVlgkNjZhpQP36dnF3r.svg)](https://asciinema.org/a/8LPsUDcVlgkNjZhpQP36dnF3r)

Run `brain-progression` to find hidden progression's element:

[![asciicast](https://asciinema.org/a/5dE0giEiPky7linHbrJptGDER.svg)](https://asciinema.org/a/5dE0giEiPky7linHbrJptGDER)

Run `brain-prime` for check is the number prime:

[![asciicast](https://asciinema.org/a/e5TMRm4iDH6ro01CbjDrINfnF.svg)](https://asciinema.org/a/e5TMRm4iDH6ro01CbjDrINfnF)
