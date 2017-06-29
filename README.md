# Simple python package example

## Build instructions
Run from project directory:
    
    python setup.py bdist_wheel

### Adding local package server to pip conf
* Add serer IP address to global option to pip configuration file. 
If using virtualenvwrapper this file is located at ~/.virtualenvs/packaging/pip.conf.
Add line

## Install via local webserver
Copy or symlink .whl package file to server (e.g. /var/www).
Can be placed inside a directory (must be all lowercase).

Use pip install as normal to install the package:
    
    pip install packagesimple
Note: Use -vvv for full debug output

## Uninstall

    pip uninstall packagesimple

# Use with packagewdependency


