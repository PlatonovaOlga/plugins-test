# README

## Install

    git clone https://github.com/PlatonovaOlga/plugins-test.git
    create and activate your favourite virtual env, example:
        python -m virtualenv venv
        .venv\bin\activate
    pip install -r requirements.txt

## Run

Package contains all necessery files, include ffmpeg binaries

App help can be started like:

    python main.py

or:

    python main.py -h
    python main.py --help


It returns info about existing modules in '/plugins' directory.

To run plugin:

    python main.py -p=plugin_name -o=option

