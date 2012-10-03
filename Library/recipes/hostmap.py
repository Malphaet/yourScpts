from __recipe__ import recipe
import os,stat

class _install(recipe):
	checktype="sha256"
	checksum="90d8416b6b3fdb84dd7dab4bd08fca3a567c1011d60c71db5376afb35f072b1d"
	homepage="http://hostmap.lonerunners.net/"
	download="http://update.lonerunners.net/software/download/847af4f866eed21b1a1398e085eb2c2a"
	description="""
hostmap is a free, automatic, hostnames and virtual hosts discovery tool written in Ruby by Alessandro `jekil` Tanasi and licensed under GNU General Public License version 3 (GPLv3). It's goal is to enumerate all hostnames and configured virtual hosts on an IP address. The primary users of hostmap are professionals performing vulnerability assessments and penetration tests.
	"""
	tags="vulnerability assessment,pentest,host discovery"
	version='0.2.2'

	_link_custom_file='hostmap.rb'
	
	def f_chmod(self,f,mode):
		os.chmod(f,os.stat(f).st_mode|mode)
	
	def post_install(self):
		self.f_chmod(os.path.join(self.extractname,self._link_custom_file),stat.S_IXUSR)
