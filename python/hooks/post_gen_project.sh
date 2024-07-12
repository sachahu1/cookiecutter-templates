#!/bin/bash

git init

poetry install --with=dev,test,documentation

poetry run pre-commit install
