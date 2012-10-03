from __recipe__ import recipe

class _install(recipe):
	checktype="sha256"
	checksum="49282601c4aecd4bd60579ddb443c181fe7e89ad99b075d9c964892c582196e1"
	homepage="http://code.google.com/p/dnsbf/"
	download="http://dnsbf.googlecode.com/svn-history/r2/trunk/dnsbf.py"
	description="""
	This script search for available domain names in an IP range.
	It uses dns to perform the search.
	It is multithreaded.
	"""
	tags=""
	_deploy_name='dnsbf.py'
	version='0.3'
#	_stop_on_checksum_error=False # False will only show the checksum and continue, True will stop if checksums doesn't match

