find . | grep ".pyc$" | while read i; do \rm "$i"; done
