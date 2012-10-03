#!/bin/sh

TO_EDIT="*.md *.py Library/*.py Library/extend/*.py"
EDITOR="gedit"
FLAGS=` 2> /dev/null `

if [ $# -eq "1" ]
then
	if [ "$1" = "all" ]
	then
		TO_EDIT="$TO_EDIT *.sh Library/recipes/*.py makefile"
	fi
	if [ "$1" = "scpt" ]
	then
		TO_EDIT="Library/recipes/*.py"
	fi
fi
#if [$1=='']

$EDITOR $FLAGS $TO_EDIT &
