yourScpts
====

The goal is quite simple, use git and recipes to manage esoteric softwares (.py .pl .rb).

This project was heavily inspired by homebrew's ideas.


Install
----
### The coder way

	git clone git@github.com:Malphaet/yourScpts.git

Use git to be always up to date and add your own recipes.

### The user way

+ Download and extract last version.
+ Run the install script (soon)
+ Add an alias to your .bashrc (like `alias your-get='python /opt/yourScpts/yourScpts.py'`) so you can use `your-get` like `apt-get`
  + Bonus, `your-get update yourScpts` will work :)

Configure
----

A lot of environement variables are available in Library/extend/ENV.py you should consider customizing them.
By default, scripts are deployed in /opt/yourScpts, please be sure the directory is writable (`make install` will do the trick)


Usage
----

    python yourScpts.py -h
    python yourScpts.py install <package>
    python yourScpts.py locate <package>
    python yourScpts.py update <package>
    python yourScpts.py remove <package>
    python yourScpts.py create <package>
    python yourScpts.py edit <package>
    python yourScpts.py upgrade

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

Interesting attributes are the following:
+ description : Unused for now, might be in short future
+ tags : Unused for now, might be in short future
+ \_deploy_name : if you are only deploying a file, give a custom name to it
+ \_link\_custom_file : Link a custom file not the packet itself
+ \_stop\_on\_checksum_error : Only show the checksum, do not check it (Useful for configuring the recipe)

You can override some inner methods:

	class yourRecipe(recipe):
		def install(self,path):
			self.fetch()
			self.check()
			self.stuff(...)
			...
			self.extract()
			self.link()
			self.clean()

The most interresting one being of course `install(self,path)` witch allows actually to do all the install stuff.

You should look at Library/\_\_recipe__.py for all methods. 
It's not very documented for now, but easy enought for average programmer to understand.

> It should usualy not be considered as a very clever idea to override the basic method (except for the install method of course).
> Most of them only perform error handling, and pretty printing.
> However, YOU are the boss.

#### Important

Recipes ARE python classes, witch means you can add conditions, variables, import other recipes, depends on other recipes to be installed, perform weird install things (./configure --prefix=ENV.MODULE_PATH, make, make install).


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

+ (commands) add a deploy method, allow to specify multiple paths for deploying


Important
----

+ install script
+ (commands) linking, relinking as a command
+ (commands) remove more efficient, error messages better handled
+ (\_\_recipe__ )\_\_recipe__.check() isn't really clever, error handling would be more appropriate


Cosmetic
----

+ (errors) REAL error handling, not vodoo random catching
+ Debug/Verbose REAL handling
+ (commands) update --remove (--version)
+ (commands) remove --version
+ messages more apt-get-like
+ integrity check is uber-odd
+ (commands) upgrade,edit,create
+ (commands) update: prune all old symlinks (laaaaame)
+ show description if available
+ show by tags
+ reinstall command

Fixed (In theory)
----
+ (syslink) Symlink for windows
+ (archive) extract should raise error
+ commands
  + locate
  + versions
  + remove
