# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:44:19 2022

@author: Shubhi Tiwari
"""


def isComment(line):

	
	if (line[0] == '/' and line[1] == '/' and line[2] != '/'):
		print("It is a single-line comment")
		return

	if (line[len(line) - 2] == '*' and line[len(line) - 1] == '/' and line[0] == '/' and line[1] == '*'):
		print("It is a multi-line comment")
		return

	print("It is not a comment")


if __name__ == '__main__':

	
	line = "//computer network"
	
	
	isComment(line)
	
	
