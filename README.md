[![](https://img.shields.io/badge/allure-passed-green)](https://karbolinivan.github.io/infotecs/)
# infotecs
Automated testing of the API for the webcalculator application
## Tools
<img src="https://img.shields.io/badge/python-0d1117?style=for-the-badge&logo=python"><img src="https://img.shields.io/badge/pytest-0d1117?style=for-the-badge&logo=pytest"><img src="https://img.shields.io/badge/pydantic-0d1117?style=for-the-badge&logo=pydantic"><img src="https://img.shields.io/badge/postman-0d1117?style=for-the-badge&logo=postman"><img src="https://img.shields.io/badge/Actions-0d1117?style=for-the-badge&logo=githubactions"><img src="https://img.shields.io/badge/pycharm-0d1117?style=for-the-badge&logo=pycharm&logoColor=0"><img src="https://img.shields.io/badge/git-0d1117?style=for-the-badge&logo=git&logoColor=0"><img src="https://img.shields.io/badge/github-0d1117?style=for-the-badge&logo=github">

## Start project

1. Installing environments for Windows:
```
python3 -m venv venv 
venv/Scripts/activate
```

2. Installing requirements:
```
pip3 install -r requirements.txt
```

3. Generate Allure report:
```
pytest -s -v --alluredir=allure-results
```

4. Start allure report
```
allure serve allure-results
```

## Commands
### Allure
Windows install Allure:
```
scoop install allure
```
