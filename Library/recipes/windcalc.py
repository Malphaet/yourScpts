from __recipe__ import recipe


class windcalc(recipe):
	checktype="sha256"
	checksum="13517aaf9ac07af139edb6daa900fb3e798595f7bc0ee73c7c591bbd12347cd0"
	homepage="https://github.com/Malphaet/windCalc"
	download="file:///home/malphaet/Downloads/Malphaet-windCalc-0492603.zip"
	#"https://github.com/Malphaet/windCalc/zipball/master" # Obviously dumb :> no auto redirect with checksum
	version='0.2'

_install=windcalc			
def install(path):
	windcalc(path).install()
