#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
	"""
	function that read a text file and
	prints stdout
	"""
	with open(filename, encoding="utf-8") as myFile:
		for line in myFile:
			print(line, end:="")
