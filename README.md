# simple_spell_checker

A simple spell checker written in python 3. 

## Packages
The application is using pyspellchecker 0.4.0. To install, 

```
git clone https://github.com/barrust/pyspellchecker.git
cd pyspellchecker
python setup.py install
```

## Usage
```
python checker.py [-h] [-m MODE] [-o OUTPUT] input
```
Two modes are supported for now:  
Error:  printing out the lines with misspelled words  
Correct: writing out the corrected text to a new file (./corrected.txt by default)  
