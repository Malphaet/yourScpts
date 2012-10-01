# -*- coding:utf8 -*-

###########################################
# download.py
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
import pycurl,sys

# Functions
def fetch(url,tmpfile):
	c = pycurl.Curl()
	c.setopt(pycurl.URL, url)
	c.setopt(pycurl.HTTPHEADER, ["Accept:"])

	b = open(tmpfile,'wb')
	c.setopt(pycurl.WRITEFUNCTION, b.write)
	c.setopt(pycurl.FOLLOWLOCATION, 1)
	c.setopt(pycurl.MAXREDIRS, 5)
	c.setopt(pycurl.NOPROGRESS, 0)
	c.setopt(pycurl.PROGRESSFUNCTION, progress)

	c.perform()
	b.close()
	CODE,PAGE=c.getinfo(pycurl.HTTP_CODE),c.getinfo(pycurl.EFFECTIVE_URL)
	print ""
	
	if CODE>299:
		os.remove(tmpfile)
		raise IOError("URL %s unreachable"%self.download)
	c.close()
	return (CODE,PAGE)

def progress(download_t, download_d, upload_t, upload_d): 
     sys.stdout.write("\rDownloading %i/%i"%(download_d,download_t))
     sys.stdout.flush()
