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

import os,sys
from .. import *
from ..extend import ENV

# Classes

class recipe():
	# All these fieds are MANDATORY and should be strings
	checktype=""
	checksum=""
	homepage=""
	download=""
	description="""
	"""
	tags=""
	version="none"
	_deploy_name=""
	_stop_on_checksum_error=True
	
	def __init__(self,deploy):
		self.deploypath,self.name=os.path.split(deploy)  # Path to the deploy location (unused), name of recipe
		self.deployname=deploy # Where to deploy the archive (extention free)
		self.extractname=os.path.join(ENV.MODULE_PATH,self.name+'_'+self.version)  # Where to extact the file (ENV.DEBUG dependant)
		self.tmppath=os.tmpnam() # Where to download the file, yes it's a security hole
		
	def fetch(self):
		try:
			download.fetch(self.download,self.tmppath)
		except:
			print "\nDownload failed !"
			print sys.exc_info()[1]
			sys.exit()
	
	def check(self):
		"The do_not_stop_on_error will print the checksum and continue"
		if not checksum.integrity(self.tmppath,self.checksum,self.checktype,self._stop_on_checksum_error):
			self.clean()
			print ("Hash of fetched file and given one don't match.")
			sys.exit()
			
	def extract(self):
		try:
			archive.extract(self.tmppath,self.extractname,self._deploy_name)
		except IOError:
			self.clean()
			print ("The extraction failed.")
			sys.exit()
			
	def clean(self):
		os.remove(self.tmppath)
		
	def link(self):
		syslink.link(self.name,self.extractname,self.deployname) # Totally unsure about that
	
	def test(self):
		"Pre install/fetch test. Meant for debug purposes"
		for attr in self.__dict__:
			print attr,':',self.__dict__[attr]

	def install(self):
		self.fetch()
		self.check() # You should ALWAYS check, yet you're the boss
		self.extract()
		self.clean()
		self.link()
		#self.test() # DEBUG

