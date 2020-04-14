## [iloveyoumatthew.com](https://Iloveyoumatthew.com)

My [girlfriend](https://caitlyndang.com) made me this love-letter website for Valentines day. I love it! :heart: (I hope I'm not embarrassing myself too much here.)

---

## A little experiment

Does $\LaTeX$ work in the browser? 
$$
\sum_{i\in[m]} \ell(h, (\mathbf{x}_i, y_i))
$$
Looks like it does with a little tweaking to the `pandoc` (namely changing `gfm` to `markdown+tex_dollar_signs --mathjax` and adding [these scripts](https://www.mathjax.org/#gettingstarted) to the header.)

---

## Creating this website

In creating this website I tried to set things up such that it would be quick to edit and extend while being made 99% from scratch. I ended up using [Marx](https://github.com/mblode/marx) to bootstrap the css, and a modified method from [this blog](https://medium.com/craftycode/how-to-create-a-simple-web-page-using-markdown-95e462e43e01) using [Pandoc](https://pandoc.org/) and a makefile to streamline the process. 

The idea is that to edit the site simply open the associated markdown file, make the edits, save, and run `$ make` to push the changes to the Github where my site is hosted. Check out [the repository](https://github.com/mattf1n/mattf1n.github.io) for all the files. In particular, take a look at `makefile` which looks like 

```makefile
make:
	pandoc -f gfm -t html -o index-content.html index.md 
	pandoc -f gfm -t html -o nav.html nav.md
	pandoc -f gfm -t html -o posts-content.html posts.md
	cat header.html nav.html sep.html index-content.html footer.html > index.html
	cat header.html nav.html sep.html posts-content.html footer.html > posts.html
	git commit -am
	git push
```

To break this down, there is a `header.html`,  `sep.html`, and `footer.html` that make up the HTML skeleton of the site. For each page, (`index` and `posts`) the content of the `nav.md` and `PAGE.md` files are converted using `pandoc` to HTML and inserted into the  skeleton using `cat`. Lastly, everything is pushed to Github. This last step I think is a little shady because the file pushes itself to Github. 