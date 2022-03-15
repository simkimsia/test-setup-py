# Demo Public Python Project

Warning! This is not a real Python project.

This Demo Public Python Project is meant to demonstrate the following:

1. setup a generic Python project,
2. how to version it,
3. how to have layered requirements using setup.py and setup.cfg,
4. and finally have it up on PyPi as a public package


## How to version using scmtools

```

source ~/.venv/test-setup-py-py3812/bin/activate

python -m pip install --upgrade "pip ~= 21.3"

pip install pip-tools "pip-tools ~= 6.5"

git init .

git add .
git commit -m '🎉 Initial commit'
git tag -a v0.0.0 -m '🔖 First tag v0.0.0'

pip-compile

pip-sync

pip install -e .
```

Now run

```
python -m {{ cookiecutter.project_slug }}
```

## Expected Output

Using [Gherkin language](https://behave.readthedocs.io/en/stable/philosophy.html#the-gherkin-language)

Scenario: In commandline
```
    GIVEN commandline
    AND inside python 3.10 venv
    AND all the dependencies under requirements.txt are installed
    WHEN i run `python -m demopublicpythonproject` in commandline
    THEN i expect this output
```

Scenario: Calling this in python shell
```
    GIVEN commandline
    AND inside python 3.10 venv
    AND all the dependencies under requirements.txt are installed
    AND i run `python`
    WHEN i run `from demopublicpythonproject.framework import hello_world_output
    AND i call `hello_world_output`
    THEN i expect this output as string
```
