
## VimMarp.vim

*2020.6.17*. I created a plugin for my current favorite text editor
[Vim](https://www.vim.org) to allow me to write presentations in markdown and
render them as I go using the [Marp CLI](https://marp.app). This was my first
time writing a Vim plugin and my first time using Vim script. [This online
guide](https://learnvimscriptthehardway.stevelosh.com) was very helpful. Check
out the [VimMarp repository](https://github.com/mattf1n/VimMarp) on my GitHub!
:keyboard:

## Camping in Cottonwood Wash

*2020.5.14*. This last weekend, [Caitlyn](http://caitlyndang.com) and I
backpacked up Cottonwood Wash in Utah's San Rafael Swell. There was not a soul
to be seen and it was a truly beautiful canyon all to ourselves. We even
spotted some petroglyphs. It reminded me that there are so many places in the
world that you can't find on Google. We were told about this canyon by my uncle
and found our way there using two outdated maps and some help from the locals.
:mountain:

![1983 USGS map of Mexican Mountain](img/UT_Mexican Mountain_250561_1983_24000.jpg)

---

## Course notes from CS183

*2020.4.20*. [These are my notes](files/lecture.pdf) from the course CS183:
Foundations of Machine Learning. They are imperfect and incomplete but I really
enjoyed making them. If you would like to make edits [email
me](mailto:matthewbfinlayson@gmail.com) and I can send you the source code.
:notebook: 

---

## The TNT game 

*2020.4.18*. While taking a class on theoretical computer science last semester
someone showed me [the NAND game](http://nandgame.com/). The idea of the game
is to start from a [NAND gate](https://en.wikipedia.org/wiki/NAND_gate) and
build a series of [boolean
circuits](https://en.wikipedia.org/wiki/Boolean_circuit) of increasing
complexity until you build a computer in a surprisingly few number of rounds.
While reading the book *[Gödel, Escher,
Bach](https://en.wikipedia.org/wiki/Gödel,_Escher,_Bach)* by Douglas
Hofstadter, I began imagining a similar 'game' where the user begins with a
small set of axioms and rules from  which they build theorems of increasing
complexity. The axioms and rules could come from Hofstadter's [TNT
system](https://en.wikipedia.org/wiki/Typographical_Number_Theory).  The game
would begin by establishing basic properties of addition, multiplication, and
so on, eventually proving profound mathematical concepts like Fermat's last
theorem (about which I would recommend reading [this book by Simon
Singh](https://www.goodreads.com/book/show/38412.Fermat_s_Enigma).) 

I'm not sure exactly how something like [Gödel's incompleteness
theorems](https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems)
could be incorporated into the game. It's something I will have to keep
thinking about. :space_invader: 

---

## Notice anything new?

*2020.4.17*. I overhauled the look of this site by ditching
[Marx](https://github.com/mblode/marx) and making my own custom CSS file. I
wanted an academic look for the site so I found [Latin
Modern](https://github.com/slashfoo/lmweb) for web (LM is the $\LaTeX$ default
font.) Also, inspired by [Butterick's Practical
Typography](https://practicaltypography.com/) which is an amazing online book,
I decided to go with more subtle links. They are now all [small caps](). The
downside of this is that links do not pop out so much. Upside is that the focus
is now more on the text!

Oh, and I added a [favicon](https://favicon.io/). :nail_care: 

---

## [iloveyoumatthew.com](https://Iloveyoumatthew.com)

*2020.4.16*. My [girlfriend](https://caitlyndang.com) made me this love-letter
website for Valentines day. I love it! (I hope I'm not embarrassing myself too
much here.) :heart: 

---

## Little experiments

*2020.4.15*. Does $\LaTeX$ work in the browser? 

$$
\sum_{i\in[m]} \ell(h, (\mathbf{x}_i, y_i))
$$

Looks like it does with a little tweaking to the `makefile` (namely changing
`gfm` to `markdown+tex_dollar_signs --mathjax` and adding [these
scripts](https://www.mathjax.org/#gettingstarted) to the header.) 

Now what about TikZ?

<script type="text/tikz">
\begin{tikzpicture}
	\draw (0,0) circle (1in);
\end{tikzpicture}
</script>

I'll take that as a no, though it looks possible through [TikZJax](http://tikzjax.com). :book: 

---

## Creating this website

*2020.4.13*. In creating this website I tried to set things up such that it
would be quick to edit and extend while being made 99% from scratch. I ended up
using [Marx](https://github.com/mblode/marx) to bootstrap the CSS, and a
modified method from [this
blog](https://medium.com/craftycode/how-to-create-a-simple-web-page-using-markdown-95e462e43e01)
using [Pandoc](https://pandoc.org/) and a makefile to streamline the process. 

The idea is that to edit the site simply open the associated markdown file,
make the edits, save, and run `$ make` to push the changes to the GitHub where
my site is hosted. Check out [the
repository](https://github.com/mattf1n/mattf1n.github.io) for all the files. In
particular, take a look at `makefile` which looks like 

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

To break this down, there is a `header.html`,  `sep.html`, and `footer.html`
that make up the HTML skeleton of the site. For each page, (`index` and
`posts`) the content of the `nav.md` and `PAGE.md` files are converted using
`pandoc` to HTML and inserted into the  skeleton using `cat`. Lastly,
everything is pushed to GitHub. This last step I think is a little shady
because the file pushes itself to GitHub. :desktop_computer: 

