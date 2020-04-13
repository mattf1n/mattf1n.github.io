make:
	pandoc -f markdown+emoji -t html -o index-content.html index.md 
	pandoc -f markdown+tex_math_dollars+emoji -t html --mathjax -o posts-content.html posts.md
	pandoc -f markdown -t html -o nav.html nav.md
	cat header.html nav.html sep.html index-content.html footer.html > index.html
	cat header.html nav.html sep.html posts-content.html footer.html > posts.html
	git commit -am "update"
	git push
