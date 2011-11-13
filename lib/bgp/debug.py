#!/usr/bin/env python
# encoding: utf-8
"""
configuration.py

Created by Thomas Mangin on 2011-03-29.
Copyright (c) 2011-2011 Exa Networks. All rights reserved.
"""

import os
import sys

debug = os.environ.get('PDB',None)

def intercept_logs (type, value, trace):
	import traceback
	from bgp.log import Logger
	logger = Logger()

	print
	print
	print "-"*80
	print "-- Please provide the information below on :"
	print "-- http://code.google.com/p/exabgp/issues/list"
	print "-"*80
	print
	print
	print "-- Configuration"
	print
	print
	print logger.config()
	print
	print
	print "-- Logging History"
	print
	print
	print logger.history()
	print
	print
	print "-- Traceback"
	print
	print
	traceback.print_exception(type,value,trace)
	print
	print
	print "-"*80
	print "-- Please provide the information above on :"
	print "-- http://code.google.com/p/exabgp/issues/list"
	print "-"*80
	print
	print
	
	#print >> sys.stderr, 'the program failed with message :', value

if debug is None:
	def intercept (type, value, trace):
		intercept_logs(type, value, trace)
	sys.excepthook = intercept
elif debug not in ['0','']:
	def intercept (type, value, trace):
		intercept_logs(type, value, trace)
		import pdb
		pdb.pm()
	sys.excepthook = intercept

del sys.argv[0]

if sys.argv:
	__file__ = os.path.abspath(sys.argv[0])
	__name__ = '__main__'
	execfile(sys.argv[0])
