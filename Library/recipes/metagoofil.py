class script(genuineScript):
	self.checktype="sha256"
	self.checksum="73259b48016e659a5137dabbd633a603c53a0418"
	self.homepage="http://code.google.com/p/metagoofil/"
	self.download="http://metagoofil.googlecode.com/files/metagoofil-2.1_BH2011_Arsenal.tar.gz"
	
	def _postDownload(self):
		unzip()
		rename()
		copy()
