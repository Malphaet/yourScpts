from __recipe__ import recipe
import os,stat

class _install(recipe):
	checktype="sha256"
	checksum="fb63b2701cecd9ce945e6f777453f2ed443ca4338fa118a35a72844e1022a669"
	homepage="https://github.com/darkoperator/dnsrecon"
	download="https://github.com/darkoperator/dnsrecon/zipball/f545b46d96f17a914020666f95dddead6c0980f4"
	description="DNSrecon is a simple tool writen for target enumeration during authorized penetration test engaments. This tool provides diferent methods for enumerating targets thru DNS service."
	tags="pentest,DNS"
	version='0.7.8'
	_link_custom_file='dnsrecon.py'
	
	def f_chmod(self,f,mode):
		os.chmod(f,os.stat(f).st_mode|mode)
	
	def post_install(self):
		self.f_chmod(os.path.join(self.extractname,self._link_custom_file),stat.S_IXUSR)
