make: 
	pandoc -f markdown+emoji -t html -o index-content.html content/index.md 
	pandoc -f markdown+tex_math_dollars+emoji -t html --mathjax \
		-o posts-content.html content/posts.md
	pandoc -f markdown -t html -o nav.html content/nav.md
	cat skeleton/header.html nav.html skeleton/sep.html \
		index-content.html skeleton/footer.html > index.html
	cat skeleton/header.html nav.html skeleton/sep.html \
		posts-content.html skeleton/footer.html > posts.html
	rm nav.html posts-content.html index-content.html
	
push:
	git commit -am "update"
	git push
