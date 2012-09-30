# -*- coding:utf8 -*-

###########################################
# yourScpts.py
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
import os,sys,warnings
import importlib,argparse

from Library import *
from Library import recipes,extend
from Library.extend import *

warnings.simplefilter("ignore")

# ys install goolib [path][version]
# ys update goolib [samepath !]
# ys remove goolin [samepath !]
# ys locate goolib
# ys -v
# ys version goolib

parser=argparse.ArgumentParser(description="Install a script according to a given recipe.")
parser.add_argument('mode', metavar='mode', type=str,choices=['install','update','locate','version','remove'], help='action to perform') # 
parser.add_argument('recipe', metavar='recipe', type=str, help='the program to fetch')
parser.add_argument('path', nargs='?', help='custom path to install the program',default=ENV.MODULE_PATH)

parser.add_argument('-v','--verbose', dest='debug', action='store_true', default=False, help='be verbose')


args = parser.parse_args()
try:
	mod=importlib.import_module("Library.recipes."+args.recipe)
	mod.install(os.path.join(args.path,args.recipe))
except ImportError:
	print "The program doesn't have an available receipe for %s."%args.recipe
	print "Maybe you should check if the name is correct, or contribute by adding it to the database."
except:
	print sys.exc_info()[:2]
