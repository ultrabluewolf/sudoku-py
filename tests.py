#!/usr/bin/env python

import engine, checker, grid, grid_gen, utils
from grid import *

if False:
	grids=utils.readGridInput('input')
	for i in range(len(grids)-1):
		print str(grids[i])
		print checker.is_valid(grids[i])

if True:
	grids=GridGen(1).create()
	