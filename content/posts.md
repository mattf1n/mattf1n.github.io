## Notice anything new?

I overhauled the look of this site by ditching [Marx](https://github.com/mblode/marx) and making my own custom CSS file. :nail_care: I wanted an academic look for the site so I found [Latin Modern](https://github.com/slashfoo/lmweb) for web (LM is the $\LaTeX$ default font.) Also, inspired by [Butterick's Practical Typography](https://practicaltypography.com/) which is an amazing online book, I decided to go with more subtle links. They are now all [small caps](). The downside of this is that links do not pop out so much. Upside is that the focus is now more on the text!

---

## [iloveyoumatthew.com](https://Iloveyoumatthew.com)

My [girlfriend](https://caitlyndang.com) made me this love-letter website for :heart: day. I love it! (I hope I'm not embarrassing myself too much here.)

---

## A little experiment

Does $\LaTeX$ work in the browser? 
$$
\sum_{i\in[m]} \ell(h, (\mathbf{x}_i, y_i))
$$
Looks like it does with a little tweaking to the `makefile` (namely changing `gfm` to `markdown+tex_dollar_signs --mathjax` and adding [these scripts](https://www.mathjax.org/#gettingstarted) to the header.)

---

## Creating this website

In creating this website I tried to set things up such that it would be quick to edit and extend while being made 99% from scratch. I ended up using [Marx](https://github.com/mblode/marx) to bootstrap the css, and a modified method from [this blog](https://medium.com/craftycode/how-to-create-a-simple-web-page-using-markdown-95e462e43e01) using [Pandoc](https://pandoc.org/) and a makefile to streamline the process. 

The idea is that to edit the site simply open the associated markdown file, make the edits, save, and run `$ make` to push the changes to the Github where my site is hosted. Check out [the repository](https://github.com/mattf1n/mattf1n.github.io) for all the files. In particular, take a look at `makefile` which looks like 

```makefile
make: 
	pandoc -f markdown+emoji -t html -o index-content.html \
    content/index.md 
	pandoc -f markdown+tex_math_dollars+emoji -t html --mathjax \
		-o posts-content.html content/posts.md
	pandoc -f markdown -t html -o nav.html nav.md
	cat skeleton/header.html nav.html skeleton/sep.html \
		index-content.html skeleton/footer.html > index.html
	cat skeleton/header.html nav.html skeleton/sep.html \
		posts-content.html skeleton/footer.html > posts.html
	rm nav.html posts-content.html index-content.html
	
push:
	git commit -am "update"
	git push
```

To break this down, there is a `header.html`,  `sep.html`, and `footer.html` that make up the HTML skeleton of the site. For each page, (`index` and `posts`) the content of the `nav.md` and `PAGE.md` files are converted using `pandoc` to HTML and inserted into the  skeleton using `cat`. Lastly, everything is pushed to Github. This last step I think is a little shady because the file pushes itself to Github. 
