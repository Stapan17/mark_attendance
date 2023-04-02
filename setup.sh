#!/bin/bash

# vars
current_path=pwd
virtual_environment_name="venv"

# creating virtual environment
virtualenv $virtual_environment_name
echo "Created virtual environment $virtual_environment_name"

# activating virtual environment
source $virtual_environment_name/bin/activate

# installing requirements
pip3 install -r requirements.txt

# deactivating virtual environment
deactivate

# appending alias to .bashrc file
echo "alias hrm='cd `$current_path`'" >> ~/.bashrc
echo "alias act='. $virtual_environment_name/bin/activate'" >> ~/.bashrc
echo "alias dct='deactivate'" >> ~/.bashrc
echo "alias mark_attendance='hrm && act && python3 attendance.py && dct && cd'" >> ~/.bashrc

# reloading bashrc
source ~/.bashrc
