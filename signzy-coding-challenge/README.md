# Signzy's Coding Challenge

## The question:
Given two input files, one containing firstnames and the other containing lastnames, do the following:
1. Insert every combination of a fullname into a MySQL DB.
2. Query the DB through an endpoint with input of min 3-letters from the firstname or lastname

## This was a fun question
It was super silly to implement in Python and why go through the trouble of doing it in languages where it is inconvenient? Since JS, PHP and Python are all allowed? :)

## How to run:
May need to do `pip install PyMySQL` to make this work.

After that, put the _firstnames.out_ and _lastnames.out_ files in the same directory as _main.py_. If not, change the hardcoded paths in _main.py_. You may change the DB configuration as well.

Then simply run `python main.py`

Cheers,
0x23212f
