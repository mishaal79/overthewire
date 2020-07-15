#!/bin/bash
if [ -z "$1" ] 
then
	echo "Please call setup with challenge name as argument";
	exit;
fi
LEVEL=$1
TEMPLATE_FILE='writeup_template.md'
CTF='natas'
mkdir 'natas'$LEVEL
cp -r $TEMPLATE_FILE $CTF$LEVEL/$CTF$LEVEL.md
