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

    python ys.py install <package>
    python ys.py create <package>
    python ys.py edit <package>

HOW-TO
----

### Writing a new recipe

The mandatory basecode is:
	from \__recipe__ import recipe
		
	class yourRecipe(recipe):
		checktype="sha1"
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
You should look at Library/\__recipe__.py for all methods. 
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
Having the contact of a person wich uses an old version of or deleted program.
The world would be a better place without all that "cleanup/deleting" on internet.

TO-DO
====

Urgent
----
+ (commands) : update
+ \__recipe__ : upgrade install

Important
----
+ (archive) : expand correctly when only one item is present
+ (errors) : REAL error handling, not vodoo random catching
+ Concurent versions (install/update handling)
+ Symlink for windows
+ add a deploy method, allow to specify multiple paths for deploying
+ \__recipe__.check() isn't really clever, error handling would be more appropriate
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
