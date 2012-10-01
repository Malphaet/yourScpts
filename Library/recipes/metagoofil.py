from __recipe__ import recipe

class metagoofil(recipe):
	checktype="sha256"
	checksum="73259b48016e659a5137dabbd633a603c53a0418"
	homepage="http://code.google.com/p/metagoofil/"
	download="http://metagoofil.googlecode.com/files/metagoofil-2.1_BH2011_Arsenal.tar.gz"
	version='2.1'

_install=metagoofil
def install(path):
	_install(path).install()
