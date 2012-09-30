#!/bin/sh

TO_EDIT="*.md *.py Library/*.py"
EDITOR="gedit"
FLAGS=` 2> /dev/null `

if [ $# -eq "1" ]
then
	if [ $1 -eq 'all' ]
	then
		TO_EDIT=$TO_EDIT "*.sh Library/receipes/*"
	fi
fi
#if [$1=='']

$EDITOR $FLAGS $TO_EDIT &
