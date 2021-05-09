"""Test dot file
"""
from dot import *

__author__ = "help@castellanidavide.it"
__version__ = "1.0 2021-5-9"

def test():
	"""Tests the dot function in the dot class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert dot.dot() == "dot", "test failed"
	#assert dot.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
