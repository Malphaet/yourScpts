from __recipe__ import recipe

class _install(recipe):
	checktype="sha1"
	checksum="1bb3e2a49f91f5f26dbc9d036f78107865692331"
	homepage="http://code.google.com/p/proxystrike/"
	download="http://proxystrike.googlecode.com/files/proxystrike-2.2.tar.bz2"
	description="""
ProxyStrike is an active Web Application Proxy. It's a tool designed to find vulnerabilities while browsing an application. It was created because the problems we faced in the pentests of web applications that depends heavily on Javascript, not many web scanners did it good in this stage, so we came with this proxy.

Right now it has available Sql injection and XSS plugins. Both plugins are designed to catch as many vulnerabilities as we can, it's that why the SQL Injection plugin is a Python port of the great DarkRaver "Sqlibf".

The process is very simple, ProxyStrike runs like a proxy listening in port 8008 by default, so you have to browse the desired web site setting your browser to use ProxyStrike as a proxy, and ProxyStrike will analyze all the paremeters in background mode. For the user is a passive proxy because you won't see any different in the behaviour of the application, but in the background is very active. :)
	"""
	tags="pentest,sql injection,XSS,pentest,sqlibf,false proxy,proxy,analysing"
	version='2.2'
	_link_custom_file='proxystrike'
