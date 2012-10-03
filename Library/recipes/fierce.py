from __recipe__ import recipe

class _install(recipe):
	checktype="sha256"
	checksum="513cb69952cf66de44daf7ebb9d18ebd5d8b43838cffa8920ea2e5ef1c646015"
	homepage="http://ha.ckers.org/fierce"
	download="http://ha.ckers.org/fierce/fierce.pl"
	description="""
Fierce domain scan was born out of personal frustration after performing a web application security audit. It is traditionally very difficult to discover large swaths of a corporate network that is non-contiguous. It's terribly easy to run a scanner against an IP range, but if the IP ranges are nowhere near one another you can miss huge chunks of networks.
	"""
	tags="DNS"
	version='0.9.9'
	_deploy_name='fierce.pl'
	_link_custom_file='fierce.pl'

