from __recipe__ import recipe

class dnsenum(recipe):
	checktype="sha1"
	checksum="c69b811c7a6d117a43e2b93c5e9a34677f991001"
	homepage="http://code.google.com/p/dnsenum/"
	download="http://dnsenum.googlecode.com/files/dnsenum-1.2.2.tar.gz"
	description="""\
	The purpose of Dnsenum is to gather as much information as possible about a domain.
	"""
	tags="information gathering,dns"
	version='2.2'
	_link_custom_file='dnsenum.pl'

_install=dnsenum
