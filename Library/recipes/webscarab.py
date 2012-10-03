from __recipe__ import recipe
import os,shutil

class _install(recipe):
	checktype="sha256"
	checksum="490ffe5600511c72e9a8f7625b36e6895f0325f5c21800277bb385944a637d65"
	homepage="https://www.owasp.org/index.php/Category:OWASP_WebScarab_Project"
	download="http://dawes.za.net/rogan/webscarab/webscarab-one-20120422-001828.jar"
	description="""
WebScarab is a framework for analysing applications that communicate using the HTTP and HTTPS protocols. It is written in Java, and is thus portable to many platforms. WebScarab has several modes of operation, implemented by a number of plugins. In its most common usage, WebScarab operates as an intercepting proxy, allowing the operator to review and modify requests created by the browser before they are sent to the server, and to review and modify responses returned from the server before they are received by the browser. WebScarab is able to intercept both HTTP and HTTPS communication. The operator can also review the conversations (requests and responses) that have passed through WebScarab.
	"""
	tags="framwork,analysis,proxy,pentest"
	version='2012-04-22'
	_deploy_name='webscarab.jar' # Specify a custom file name (Only used for single file scripts though)
	_link_custom_file='webscarab.jar' # If you want to link a custom file instead of the whole folder

	def copy(self):
		os.mkdir(self.extractname)
		shutil.copy(self.tmppath,os.path.join(self.extractname,self._deploy_name))
		
	def install(self):
		self.fetch()
		self.check() # You should ALWAYS check, yet you're the boss
		self.copy()
		self.clean()
		self.link()
