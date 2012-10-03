from __recipe__ import recipe
import os,stat

class metagoofil(recipe):
	checktype="sha1"
	checksum="73259b48016e659a5137dabbd633a603c53a0418"
	homepage="http://code.google.com/p/metagoofil/"
	download="http://metagoofil.googlecode.com/files/metagoofil-2.1_BH2011_Arsenal.tar.gz"
	description="""\
	Metagoofil is an information gathering tool designed for extracting metadata of public documents (pdf,doc,xls,ppt,docx,pptx,xlsx) belonging to a target company.
	"""
	tags="information gathering,harvesting"
	version='2.1'
	_link_custom_file='metagoofil.py'
	
	def f_chmod(self,f,mode):
		os.chmod(f,os.stat(f).st_mode|mode)
	
	def post_install(self):
		self.f_chmod(os.path.join(self.extractname,self._link_custom_file),stat.S_IXUSR)


_install=metagoofil
