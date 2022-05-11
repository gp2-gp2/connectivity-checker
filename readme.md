# Connectivity checker

## Info

### Installation

1. Create a Python virtual environment

   ```python
   $ python -m venv ./venv
   $ source venv/bin/activate
   (venv) $
   ```

2. Install the requirements

      ```python
      (venv) $ python -m pip install -r requirements.txt
      ```

### Run the project

```python
(venv) $ python -m checker -u python.org
The status of "python.org" is: "Online!" 👍
```

### Features

Checker provides following options:

* ```-u``` or ```--urls``` takes one or more URLs and checks if they're online.

* ```-f``` or ```--input-file``` takes a file containing a list of URLs to check.

* ```-a``` or ```--asynchronous``` runs the check asynchronously.

## About the author

Michał Marciniak - Email: <gp3510@gmail.com> / <marciniak_michal@outlook.com>

## License

Distributed under the MIT license. See LICENSE in the root directory of this repo for more information.

Based on [https://realpython.com/site-connectivity-checker-python/](https://realpython.com/site-connectivity-checker-python/)

## Personal notes

### Setup

Env creation

```python
python3 -m venv venv
```

Env activation

```python
source venv/bin/activate
```

Deactivation

```python
deactivate
```

To delete env it's enough to delete folder

```python
rm -r venv
```

## Required packages

* **aiohttp**

```python
python -m pip install aiohttp
```

or

```python
pip install -r requirements.txt
```

### To verify later

How to write a good readme.md [https://dbader.org/blog/write-a-great-readme-for-your-github-project](https://dbader.org/blog/write-a-great-readme-for-your-github-project%E2%80%B8)

Template [https://github.com/dbader/readme-template](https://github.com/dbader/readme-template%E2%80%B8)

Pip install / freeze [https://note.nkmk.me/en/python-pip-install-requirements/](https://note.nkmk.me/en/python-pip-install-requirements/)

Original source code [https://github.com/realpython/materials/tree/master/python-site-connectivity-checker](https://github.com/realpython/materials/tree/master/python-site-connectivity-checker)

## Docker Dev Environments

I just tested this repo in Docker Desktop app in Windows. Below couple remarks required to succesfuly run the app from such VC code setup.

After opening the project in Visual Studio Code we have to open terminal and update the current linux distro.

```sudo apt update```

```sudo apt upgrade```

Next install

```sudo apt-get install python3-venv```

After those steps are completed we should be aable to proceed and setup venv.

Next step after virtual environment is to install pip requirements. This one is failing in that docker setup.
Package named ```multidict``` is failing to build with below message:
```Failed building wheel for multidict```

Details:
```Command "/com.docker.devenvironments.code/venv/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-install-7r92pke8/multidict/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-record-9ifrw1lh/install-record.txt --single-version-externally-managed --compile --install-headers /com.docker.devenvironments.code/venv/include/site/python3.7/multidict" failed with error code 1 in /tmp/pip-install-7r92pke8/multidict/```

I will verify later what is needed to fix this one.