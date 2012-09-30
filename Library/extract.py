# -*- coding:utf8 -*-

###########################################
# extract.py
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

import tarfile,zipfile,mimetypes

# Functions

def extract(path,dest):
	if "text/" == mimetypes.read_mime_types(path)[:5]:
		f,d=open(path),open(dest)
		d.write(f.read())
		d.close(),f.close()
		return True
	if tarfile.is_tarfile(path): tmpf=tarfile.open(path,'r')
	else:
		if zipfile.is_zipfile(path): tmpf=zipfile.open(path)
		else: 
			print "The given file is impossible to extract."
			return False
	tmpf.extractall(dest)
	tmpf.close()
	return True
