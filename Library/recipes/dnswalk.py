from __recipe__ import recipe

class _install(recipe):
	checktype="sha256"
	checksum="b49ea147a00e95e80330534d43f8737c2367ae862050e9a8009a607c49f0ea6b"
	homepage="http://sourceforge.net/projects/dnswalk/"
	download="http://downloads.sourceforge.net/project/dnswalk/dnswalk/2.0.2/dnswalk-2.0.2.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fdnswalk%2F&ts=1349222251&use_mirror=switch"
	description="""
dnswalk is a DNS debugger. It performs zone transfers of specifieddomains, and checks the database in numerous ways for internalconsistency, as well as accuracy.
	"""
	tags="DNS debugger,DNS"
	version='2.0.2'

	_link_custom_file='dnswalk'
