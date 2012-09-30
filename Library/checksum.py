# -*- coding:utf8 -*-

###########################################
# checksum.py
# Nom: yourScript
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of yourScript.
#
# yourScript is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# yourScript is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with yourScript. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

# Imports
import hashlib

# Functions
def integrity(path_to_check,checksum_file,checksum_type=hashlib.sha256):
	return checksum()==checksum_type
	
def checksum(path_to_check,checksum_type=hashlib.sha256):
#	if checksum_type not in hashlib.algorithms:
#		raise ValueError
	return checksum_type(open(path_to_check,'r').read()).hexdigest()
# Main
if __name__ == '__main__':
	sys.exit()


