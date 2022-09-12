#!/usr/bin/python3
raise_exception = __import__('exceptions').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
