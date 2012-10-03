LIBRARY=Library
EXTEND=$(LIBRARY)/extend
RECEIPES=$(LIBRARY)/recipes
PATHS=$(LIBRARY) $(EXTEND) $(RECEIPES)

CLEAN_PATHS=$(PATHS:%=clean-%)

install:
	echo "Not implemented :)"
	echo "SETTING UP ENV"
	echo "PRETENDING TO DO STUFF"
	
deploy:
	echo "Not implemented yet :)"

clean: $(CLEAN_PATHS)

$(CLEAN_PATHS):
	rm -f $(@:clean-%=%)/*.pyc
