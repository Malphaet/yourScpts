# -*- coding:utf8 -*-

###########################################
# __receipe__.py
# Nom: yourScpt.py
# Copyright 2012: Maximilien Rigaut
###########################################
# This file is part of yourScpt.py.
#
# yourScpt.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# yourScpt.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with yourScpt.py. If not, see <http://www.gnu.org/licenses/>.
########################################################
# LICENCE                                              #
########################################################

# Include

import os
from .. import *

# Classes

class recipe():
	# All these fieds are MANDATORY and should be strings
	checktype=""
	checksum=""
	homepage=""
	download=""
	version="0.1a"
	
	def __init__(self,deploy):
		self.deploypath,self.name=os.path.split(deploy)
		
		self.deployname=deploy
		self.extractname=self.deployname+'_'+self.version
		self.tmppath=os.tmpnam()
		
	def fetch(self):
		download.fetch(self.download,self.tmppath)
	
	def check(self,do_not_stop_on_error=True):
		"The do_not_stop_on_error will print the checksum and continue"
		if not checksum.integrity(self.tmppath,self.checksum,self.checktype,do_not_stop_on_error):
			raise ValueError("Hash of fetched file and given one don't match.")
			
		
	def extract(self):
		try:
			os.mkdir(self.extractname)
		except:
			raise IOError("The program already exists (you should have tested that moron).")
		if not archive.extract(self.tmppath,self.extractname):
			os.rmdir(self.extractname)
		
	def clean(self):
		os.remove(self.tmppath)
		
	def link(self):
		syslink.link(self.extractname,self.deployname) # Totally unsure about that
	
	def test(self):
		"Pre install/fetch test. Meant for debug purposes"
		for attr in self.__dict__:
			print attr

	def install(self):
		self.fetch()
		self.check() # You should ALWAYS check, yet you're the boss
		self.extract()
		self.test() # DEBUG
		self.clean()
#		self.link()
