#!/bin/bash

echo -n 'Get Pip? y/Y or n/N'
read get_pip
if [[ get_pip == 'y' || get_pip == 'Y' ]]
then
    curl https://bootstrap.pypa.io/get-pip.py | python
fi

python -m virtualenv venv
echo -n 'Use Linux? y/Y or n/N'
read is_linux
if [[ is_linux == 'y' || is_linux == 'Y' ]]
then
    source venv/bin/activate
else
    source venv/Scripts/activate
fi

pip install -r requirements.txt