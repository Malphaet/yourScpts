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
def integrity(file_to_check,checksum_value,checksum_type,_stop_on_checksum_error):
	if checksum_type not in hashlib.algorithms: raise NotImplementedError("This is not the hash you are looking for.")
	checksum_type=hashlib.__dict__[checksum_type]
	filechecksum=checksum(file_to_check,checksum_type)
	if _stop_on_checksum_error: return checksum_value==filechecksum
	else: 
		print filechecksum
		return True
	
def checksum(file_to_check,checksum_type=hashlib.sha256):
	"Takes a file descriptor, and applies a checksum to it."
	return checksum_type(open(file_to_check,'r').read()).hexdigest()

