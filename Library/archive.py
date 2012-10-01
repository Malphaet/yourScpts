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

import os
import tarfile,zipfile,mimetypes

# Functions

## Path treatement
def	prefix(files):
	pref=files[0]
	size=len(pref)
	for f in files:
		if pref!=f[size:]:
			return '' 
	return pref
	
def clear_forbidden(files):
	ret=[]
	for f in files:
		n=os.path.normpath(f)
		if (n[0]!='/' and n[:2]!='..'):
			ret.append(f)
	return f
	
## Main function
def extract(path,dest):
	mime=mimetypes.guess_type(path,False)[0]
	if mime!=None and "text/" in mime :
		f,d=open(path),open(dest)
		d.write(f.read())
		d.close(),f.close()
		return True
	
	if tarfile.is_tarfile(path):
		tmpf=tarfile.open(path,'r')
		files=tmpf.getnames()
		extract=tmpf.extractall
	else:
		if zipfile.is_zipfile(path):
			tmpf=zipfile.ZipFile(path)
			files=tmpf.namelist()
			extract=tmpf.extractall
		else: 
			raise IOError("The given file is impossible to extract.")
	
	p_size=len(prefix(files))
	print p_size,prefix(files)
	extract(clear_forbidden(files),dest)
	tmpf.close()
	return True
