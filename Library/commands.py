# -*- coding:utf8 -*-

###########################################
# install.py
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

# Include
import os,sys,time
import importlib,shutil

import extend.ENV as ENV
from extend.errors import *
import recipes

# Functions

## Path calculations

def installed(program):
	return os.path.lexists(os.path.join(ENV.INFO_PATH,program))

def infos(program):
	try:
		f=open(os.path.join(ENV.INFO_PATH,program),'r')
	except:
		raise ImportError("Last install didn't performed as due")
	existing=f.read().split(os.linesep)
	versions,programs,symlinks=[],set(),[] # Don't add duplicates because of symlinks
	for line in existing:
		try:
			if line!='': # If someone got the strange idea to edit by hand
				sym,prog=line.split(',')
				versions.append(prog.split('_')[-1])
				symlinks.append(sym)
				programs.add(prog) # Don't add duplicates because of symlinks
		except:
			print "The info file",os.path.join(ENV.INFO_PATH,program),"is damaged, reading isn't possible"
	programs=list(programs)
	return {'installed':programs,'versions':versions,'links':symlinks,'all':programs+symlinks}
	
def newest(program,version):
	return max(infos(program)['versions']) >= version

## Tools

def importProgram(recipe):
	try:
		return importlib.import_module("Library.recipes."+recipe,'Library')
	except ImportError:
		ExistsError(recipe)
	except:
		print sys.exc_info()[:2]


## Commands	
def install(args): # Will one day work with gitpython for version management
	program=args.recipe
	mod=importProgram(program)
	if installed(program): 
		if newest(program,mod._install.version): state="and is up to date"
		else: state="but is not up to date"
		print "The program is already installed",state
		return False
	mod.install(os.path.join(args.path,args.recipe))
	
def update(args):
	program=args.recipe
	if not installed(program): AvailableError(program)
	prog=importProgram(program)
	if args.check:
		if newest(program,prog._install.version):
			print "Your program is already up to date"
		else:
			print "Your program is not up to date"
		return
	# Real update
	
def locate(args):
	program=args.recipe
	if not installed(program): AvailableError(program)
	print "The following paths the (known) deployments of the recipe"
	for place in infos(program)['all']:
		if os.path.exists(place): broken='[Valid]'
		else: broken='[Broken]'
		print place,broken

def version(args):
	program=args.recipe
	if not installed(program): AvailableError(program)
	versions=infos(program)['versions']
	if args.all: print versions
	else: print max(versions)
	
def remove(args):
	program=args.recipe
	if not installed(program): AvailableError(program)
	for place in infos(program)['all']:
		try:
			if os.path.isdir(place):shutil.rmtree(place)
			else: os.remove(place)
		except OSError:
			print place, "doesn't exists"
	try:
		os.remove(os.path.join(ENV.INFO_PATH,program))
	except:
		print "Humm. That's odd, info file cannot be removed"
		print "Proceed yourself:",os.path.join(ENV.INFO_PATH,program)
	
def upgrade(args): # Will one day work with gitpython
	print "type commands:"
	if (args.recipes): print "This in generally not a good idea to update only recipes,\ndo it only if you know your stuff"
	print "   git fetch origin updating"
	if (args.recipes):
		print '   git checkout updating Library/scpts/*'
		print "   git commit -m 'updated formulas: %s'"%time.ctime()
	else: print "   git merge updating"
