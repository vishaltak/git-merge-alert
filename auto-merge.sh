#!/bin/bash

git checkout <local-branch>							#e.g. git checkout master
git fetch <remote-name>								#e.g. git fetch origin
git merge <remote-name>/<remote-branch>;			#e.g. git fetch origin/master
if [ $? -eq 1 ]; then
	git merge --abort
	python send_mail.py "receiver@example.com" "Auto-Merging failed" "There are some conflicts which could not be resolved. Please resolve the conflicts and merge the code."
	#echo "Merge-conflict"
else
	python send_mail.py "receiver@example.com" "Auto-Merging successful" "Code has been successfully pulled from the remote repository and merged on."
	#echo "Merge Successful"
fi