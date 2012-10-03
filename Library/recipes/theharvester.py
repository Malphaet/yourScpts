from __recipe__ import recipe
import os,stat

class theHarvester(recipe):
	checktype="sha1"
	checksum="2ac89541aeb6207d3dc84ba161dd2742a6afdd34"
	homepage="http://code.google.com/p/theharvester/"
	download="http://theharvester.googlecode.com/files/theHarvester-2.2.tar"
	description="""
The objective of this program is to gather emails, subdomains, hosts,
employee names, open ports and banners from different public sources like search engines,
PGP key servers and SHODAN computer database.

This tool is intended to help Penetration testers in the early stages of the penetration test\
in order to understand the customer footprint on the Internet.\
It is also useful for anyone that wants to know what an attacker can see about their organization.
	"""
	tags="information gatherer,harvester,pentest"
	version='2.2'
	_link_custom_file='theHarvester.py'
	
	def f_chmod(self,f,mode):
		os.chmod(f,os.stat(f).st_mode|mode)
	
	def post_install(self):
		self.f_chmod(os.path.join(self.extractname,'theHarvester.py'),stat.S_IXUSR)
		
_install=theHarvester
