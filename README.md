yourScpts
====

The goal is quite simple, use git and recipes to manage esoteric softwares (.py .pl .rb).
This project was heavily inspired by homebrew's ideas.


Install
----
Download and extract last version.

If you would rather use the last (unstable version)
     git clone git@github.com:Malphaet/YAPM.git

Usage
----

    python yourScpts.py install <package>
    python yourScpts.py create <package>
    python yourScpts.py edit <package>

HOW-TO
----

### Writing a new recipe

The mandatory basecode is:

	from __recipe__ import recipe
		
	class yourRecipe(recipe):
		checktype="" # Check hashlib for available algorithms
		checksum=""
		homepage=""
		download=""
		version=""
	
	_install=yourRecipe
	
You can provide an install method:

	def install(path):
		_install(path).install()

And override some inner methods:

	class yourRecipe(recipe):
		def install(self,path):
			self.fetch()
			self.check()
			self.stuff(...)
			...
			self.extract()
			self.link()
		def stuff(self):
			print "Program installing now"
			...

You should look at Library/\_\_recipe__.py for all methods. 
It's not very documented for now, but easy enought for average programmer to understand.

#### Commiting
The commit policy is not that high, and for now, there's a 99% chance your pull request passes.
However, for further functionallities sake, please separate recipe commits and core commit.
Moreover, when you commit a recipe take care of the following formating:

	Recipe Name + Version
	
	Commit message & stuff
	tags: A subset of the following tags (implemented,tested,fixed)
	optional tags: A subset of the following tags (using,developping)

The optionall tag "using" is for the following purpose:
Having the contact of a person wich uses an old version/deleted version of program.
The world would be a better place without all that "cleanup/deleting" on internet.

TO-DO
====

Urgent
----
+ (commands) : update
+ \_\_recipe__ : install (auto discover method)

Important
----
+ (archive) : expand correctly when only one item is present, check bad files
+ (errors) : REAL error handling, not vodoo random catching
+ Concurent versions (install/update handling)
+ Symlink for windows
+ add a deploy method, allow to specify multiple paths for deploying
+ \_\_recipe__.check() isn't really clever, error handling would be more appropriate
+ extract should raise error
+ extract, clear_forbidden

Cosmetic
----
+ Debug/Verbose REAL handling

Fixed (In theory)
----
+ commands
  + locate
  + versions
  + install
  + remove
