from __recipe__ import recipe

class _install(recipe):
	checktype=""
	checksum=""
	homepage=""
	download=""
	description="""
	"""
	tags=""
	version=''
	_deploy_name='' # Specify a custom file name (Only used for single file scripts though)
	_stop_on_checksum_error=False # False will only show the checksum and continue, True will stop if checksums doesn't match
	_link_custom_file='' # If you want to link a custom file instead of the whole folder
