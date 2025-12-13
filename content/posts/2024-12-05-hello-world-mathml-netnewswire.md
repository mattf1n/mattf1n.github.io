---
title: Hello world, MathML in NetNewsWire
date: 2024-12-05
html-math-method: mathml
css:
  - ../style/main.css
---

I created an RSS feed for my website. I did it by hand, [this template](https://www.w3schools.com/xml/xml_rss.asp). I don't use any frameworks for maintaining my website, I just write everything by hand. I don't change my website often enough for it to be worthwhile to do anything fancier.

I also realized that, at least for [NetNewsWire](netnewswire.com), [MathML](https://mathml.igalia.com) is supported but [MathJax](mathjax.org) is not. I will be doing all my math in MathML from now on (just use the `--mathml` flag when converting to html with `pandoc`).
$$\exp(x)=\sum_{n=0}^\infty \frac{x^n}{n!}$$
