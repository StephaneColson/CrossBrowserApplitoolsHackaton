# Applitools Cross Browser Testing Hackathon
This project is my work for the 2020 Applitools Cross Browser Testing hackaton.
See overview and instructions on this [page](https://applitools.com/cross-browser-testing-hackathon-v20-1-instructions/).

## Framework used
I used [Pylenium](https://github.com/ElSnoMan/pyleniumio) from [Carlos Kidman](https://github.com/ElSnoMan).
You will find the full documentation [here](https://elsnoman.gitbook.io/pylenium/).

## Environment needed
- python 3: if not yet installed, follow [this](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/) which is the Python package installer 
- A virtual environment (virtualenv): instructions [here](https://elsnoman.gitbook.io/pylenium/getting-started/virtual-environments)
- Browser drivers like [Chrome Driver](http://chromedriver.chromium.org/downloads) (must be in your `PATH)`

For Applitools you must have an account to use Eyes. See [Applitools](https://applitools.com/) website.

You must set you APPLITOOLS_API_KEY environment key:
```bash
$ export APPLITOOLS_API_KEY='<your_key>'
``
where your_key is available in your Applitools Eyes Dashboard.
For more information see the [doc](https://applitools.com/docs/) or follow courses on
[Test Automation University](https://testautomationu.applitools.com/)

## Quick Setup
- Clone the project
```bash
$ git clone https://github.com/StephaneColson/CrossBrowserApplitoolsHackaton.git
```
- Check Python version or [install it](https://www.python.org/downloads/)
```bash
$ python --version
$ Python 3.7.6
```

- pip3 install
```bash
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
pip install pyleniumio
```

- Run the Modern Applitools Tests using Ultra Fast Grid
```bash
python -m pytest tests/ModernTestsV1.py
```
Results are retrieved in your Applitools Eyes Dashboard page.

- Run the Traditional Selenium Tests
```bash
python -m pytest tests/TraditionalTestsV1.py
```
Results are retrieved in `Traditional-V1-TestResults.txt` and `Traditional-V2-TestResults.txt`
depending on version used: Resp. https://demo.applitools.com/gridHackathonV1.html or 
https://demo.applitools.com/gridHackathonV2.html

Enjoy!



