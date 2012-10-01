# -*- coding:utf8 -*-

###########################################
# errors.py
# Nom: yourScpt
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of yourScpt.
#
# yourScpt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# yourScpt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with yourScpt. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

import sys
# Functions

def ExistsError(recipe=''):
	if recipe!='': recipe="for "+recipe
	print "The program doesn't have an available recipe %s."%recipe
	print "Maybe you should check if the name you entered is correct."
	print "If so, contribute by adding it to the database !"
	sys.exit()
	
def AvailableError(path=''):
	print "The program",path,"isnt installed."
	sys.exit()
