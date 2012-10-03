from __recipe__ import recipe

class _install(recipe):
	checktype="sha256"
	checksum="e250d7dcead4e7b0aa22c8b655a0b092d60174676da55994705918fa21bb3a50"
	homepage="http://www.edge-security.com/webslayer.php"
	download="https://github.com/Malphaet/webslayer/tarball/1.0a"
	description="""
WebSlayer is a tool designed for brute forcing Web Applications, it can be used for finding resources not linked (directories, servlets, scripts,files, etc), brute force GET and POST parameters, bruteforce Forms parameters (User/Password), Fuzzing, etc. The tools has a payload generator and an easy and powerful results analyzer.
"""
	tags="bruteforce,pentest,harvester,fuzzing"
	version='1.0a'
	_link_custom_file='WebSlayer.py'
