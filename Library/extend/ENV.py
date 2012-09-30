# -*- coding:utf8 -*-

###########################################
# ENV.py
# Nom: yourScpts
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of yourScpts.
#
# yourScpts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# yourScpts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with yourScpts. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

# Import
import sys,os

# ENV Variables
DEBUG=True
SELF_PATH=os.path.join(os.getcwd(),os.path.split(sys.argv[0])[0])
if DEBUG: MODULE_PATH=os.path.join(SELF_PATH,"false","opt","yourScpts","scpts")
else: MODULE_PATH=os.path.join("opt","yourScpts","scpts")

# Test ENV
if not os.access(MODULE_PATH, os.W_OK):
	raise IOError("%s is not writable, abort !"%MODULE_PATH)


if True:
	print "yourScpts directory:",SELF_PATH
	print "Scripts directory:", MODULE_PATH
	print ""
