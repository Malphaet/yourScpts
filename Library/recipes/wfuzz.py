from __recipe__ import recipe
import os,stat

class _install(recipe):
	checktype="sha1"
	checksum="8b82a2796579626267ba7bf59230eecfaf38f08a"
	homepage="http://code.google.com/p/wfuzz/"
	download="http://wfuzz.googlecode.com/files/wfuzz-2.0.tgz"
	description="""
Wfuzz is a tool designed for bruteforcing Web Applications, it can be used for finding resources not linked (directories, servlets, scripts, etc), bruteforce GET and POST parameters for checking different kind of injections (SQL, XSS, LDAP,etc), bruteforce Forms parameters (User/Password), Fuzzing,etc.
	"""
	tags="pentest,injection,XSS,Sql,Fuzzing"
	version='2.0'
	_link_custom_file='wfuzz.py'
	
	def f_chmod(self,f,mode):
		os.chmod(f,os.stat(f).st_mode|mode)
	
	def post_install(self):
		self.f_chmod(os.path.join(self.extractname,self._link_custom_file),stat.S_IXUSR)
