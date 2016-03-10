# PPR
* Easy create new *P*ython *PR*oject.

## Install
* Standard pip installation, in folder with setup.py run:
    - pip install .

## Usage
* Create new Python project named HelloProject
    - ppr HelloProject
* The command generates this folder structure:
    - /HelloProject
        + /HelloProject
            * __init__.py
            * hello.py
        + setup.py
* So you can just install your new project:
    - pip install HelloProject\
* .. or development installation:
    - pip install --editable HelloProject\
* And that's all.
