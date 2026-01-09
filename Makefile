POST_MD := $(wildcard content/posts/*.md)
POST_HTML := $(patsubst content/posts/%.md,posts/%.html,$(POST_MD))
POST_INDEX := posts/index.html
FEED := feed.xml

all: gallery.html smislinear.html deep-ba-sampling.html differentiable-binary-to-onehot.html ensemble.html entropy.html interest-demo.html apologies.html colm2024.html sidescroll.html pils.html neurips2025.html $(POST_HTML) $(POST_INDEX) $(FEED)

PANDOC_DEFAULT_FLAGS := --standalone -f markdown+implicit_figures+emoji --include-in-header favicon_head.html
PANDOC_MATHJAX_FLAGS := --standalone -f markdown+implicit_figures+emoji --include-in-header favicon_head.html --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

posts/%.html: content/posts/%.md
	@mkdir -p $(dir $@)
	pandoc $(if $(PANDOC_FLAGS),$(PANDOC_FLAGS),$(PANDOC_DEFAULT_FLAGS)) $< -o $@

posts/index.html: $(POST_MD) scripts/build_posts_index.py
	python scripts/build_posts_index.py

feed.xml: $(POST_MD) scripts/build_feed.py
	python scripts/build_feed.py

# Post-specific flags
posts/2024-10-21-deep-ba-sampling-extending-bat.html: PANDOC_FLAGS := --standalone -f markdown+implicit_figures+emoji --include-in-header favicon_head.html --mathml
posts/2024-10-21-differentiable-binary-to-onehot.html: PANDOC_FLAGS := --standalone -f markdown+implicit_figures+emoji --include-in-header favicon_head.html --mathml
posts/2024-10-21-right-way-to-ensemble-language-models.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2024-10-21-research-interest-demo.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2024-10-21-obtaining-logprobs-from-llm-api.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2023-10-21-softmax-function-is-linear.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2023-10-21-visualizations-gallery.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2024-12-05-hello-world-mathml-netnewswire.html: PANDOC_FLAGS := --standalone -f markdown+implicit_figures+emoji --mathml
posts/2025-04-03-llm-have-built-in-macs.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)
posts/2025-12-12-heavy-tails-and-diversity-in-model-distributions.html: PANDOC_FLAGS := $(PANDOC_MATHJAX_FLAGS)

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
	pandoc --mathjax --standalone $< > $@ --css style/blog.css --include-in-header gradio.html --citeproc 

neurips2025.html: content/neurips2025.md
	pandoc --standalone --metadata lang=en $< > $@ --css style/blog.css
