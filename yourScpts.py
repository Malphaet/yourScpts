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

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=("""\
Scripts managing program.
-------------------------
    Install, update, manage your scripts.
    This program is made to handle custom scripts,
    and is heavily git based to keep track of 
    versions and recipes."""))

subparsers = parser.add_subparsers(title='action to perform',dest='command', help='for more help, try [command] -h')

parser_install=subparsers.add_parser('install',help='install the given recipe')
parser_install.add_argument('recipe', metavar='recipe', type=str, help='the program to fetch')
parser_install.add_argument('path', nargs='?', help='custom path to install the program',default=ENV.MODULE_PATH)

parser_locate=subparsers.add_parser('locate',help='locate the given recipe')
parser_locate.add_argument('recipe', metavar='recipe', type=str, help='the program to locate')

parser_update=subparsers.add_parser('update',help='update the given recipe')
parser_update.add_argument('recipe', metavar='recipe', type=str, help='the program to update')
parser_update.add_argument('--check','-c',action='store_true',help='only check if uptades exists')

parser_version=subparsers.add_parser('version',help='give the version of the given recipe')
parser_version.add_argument('recipe', metavar='recipe', type=str, help='the program to analyse')
parser_version.add_argument('--all',action='store_true',help='show all versions')

parser_remove=subparsers.add_parser('remove',help='remove the given recipe')
parser_remove.add_argument('recipe', metavar='recipe', type=str, help='the program to remove')
parser_remove.add_argument('path', nargs='?', help='custom path to remove the program',default=ENV.MODULE_PATH)

parser_upgrade=subparsers.add_parser('upgrade',help='upgrade the program and/or recipes')
parser_upgrade.add_argument('--recipes',action='store_true',help='only update the recipes')

parser.add_argument('-v','--verbose', dest='debug', action='store_true', default=False, help='be verbose')

args = parser.parse_args()

# Main program

commands.__getattribute__(args.command)(args)
