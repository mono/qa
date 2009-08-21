#!/bin/bash

NONUNIQUE=$(find . -iname \*.py|grep -v .svn|xargs grep -hi "class "|sort|uniq -d|tr '(' ' '|awk '{print $2}')

if [ "$NONUNIQUE" != "" ]
then
	for CURNU in $NONUNIQUE
	do
		echo "--------------------------------------------------------------------"
		find . -iname \*.py|grep -v .svn|xargs grep -i "class "|sort|grep "$CURNU"
	done
fi
