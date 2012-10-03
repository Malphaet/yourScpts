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

import os,sys#,shutil
import tarfile,zipfile
import stat

# Functions

## Path treatement
def clear_forbidden(files,get=lambda x:x):
	ret=[]
	for f in files:
		n=os.path.normpath(get(f))
		if (n[0]!='/' and n[:2]!='..'):
			ret.append(f)
	return ret
	
## Main function
def extract(path,dest,name=''):	
	if tarfile.is_tarfile(path):
		tmpf=tarfile.open(path,'r')
		files=tmpf.getmembers()
		get=lambda x:x.name
		extract=tmpf.extractall
	else:
		if zipfile.is_zipfile(path):
			tmpf=zipfile.ZipFile(path)
			get=lambda x:x
			files=tmpf.namelist()
			extract=tmpf.extractall
		else:
			if name!='':
				os.mkdir(dest)
				dest=os.path.join(dest,name)
			try:
				f,d=open(path,'r'),open(dest,'w')
				d.write(f.read())
				d.close(),f.close()
				os.chmod(dest,os.stat(dest).st_mode | stat.S_IXUSR)
#				shutil.copy(path,dest)
#				os.remove(f)
				return True
			except:
				os.rmdir(dest)
				print sys.exc_info()
				raise IOError("Failed to copy file")
	
	t_dest=dest+"_temp_"
	os.mkdir(t_dest)
	try:
		extract(path=t_dest,members=clear_forbidden(files,get))
		extracted_files=os.listdir(t_dest)
	except:
		os.rmdir(t_dest)
		print sys.exc_info()
		raise IOError("Extraction Failed")
	
	if len(extracted_files)==1:
		os.rename(os.path.join(t_dest,extracted_files[0]),dest)
		os.rmdir(t_dest)
	else:
		os.rename(t_dest,dest)
	
	tmpf.close()
	return True
