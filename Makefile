all: gallery.html smislinear.html deep-ba-sampling.html differentiable-binary-to-onehot.html ensemble.html entropy.html interest-demo.html apologies.html colm2024.html sidescroll.html pils.html

gallery.html: content/gallery.md
	pandoc -f markdown+implicit_figures --mathjax --standalone $< > $@

sidescroll.html: content/sidescroll.md
	pandoc -f markdown --mathml --standalone $< > $@ --css style/volume.css

smislinear.html: content/smislinear.md
	pandoc --mathjax --standalone $< > $@

deep-ba-sampling.html: content/deep-ba-sampling.md
	pandoc --mathml --standalone $< > $@

differentiable-binary-to-onehot.html: content/differentiable-binary-to-onehot.md
	pandoc --mathml --standalone $< > $@

ensemble.html: content/ensemble.md
	pandoc --mathjax --standalone $< > $@

entropy.html: content/entropy.md style/main.css
	pandoc --mathjax --standalone $< > $@ --css style/main.css

interest-demo.html: content/interest-demo.md style/main.css
	pandoc --mathjax --standalone $< > $@ --css style/main.css

apologies.html: content/apologies.md style/main.css
	pandoc --mathjax --standalone $< > $@ --css style/main.css

seq_level_temp.html: content/seq_level_temp.md
	pandoc --mathjax --standalone $< > $@ --css style/main.css

colm2024.html: content/colm2024.md
	pandoc --mathjax --standalone $< > $@ --css style/main.css

pils.html: content/pils.md style/blog.css gradio.html
	pandoc --mathjax --standalone $< > $@ --css style/blog.css --include-in-header gradio.html
