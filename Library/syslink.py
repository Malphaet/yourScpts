# -*- coding:utf8 -*-

###########################################
# syslink.py
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
import extend.ENV as ENV

# Functions

def symlink(a,b):
	if sys.platform=='win32':
		import ctypes
		kdll = ctypes.windll.LoadLibrary("kernel32.dll")
		kdll.CreateSymbolicLinkA(a, b, 0)
	else:
		os.symlink(a,b)	

def link(program,extract_path,deploy_path):
	f=open(os.path.join(ENV.INFO_PATH,program),'a')
	f.write(deploy_path+','+extract_path+os.linesep)
	f.close()
	if os.path.exists(deploy_path): os.remove(deploy_path) # Update the symlink
	symlink(extract_path,deploy_path)
