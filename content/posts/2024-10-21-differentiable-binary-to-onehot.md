---
title: A differentiable function from binary integer to one-hot representations
date: 2024-10-21
author: "[Matthew Finlayson](/index.html)"
html-math-method: mathml
---

I would like to define a differentiable function $f:\{0,1\}^{\log v}\to\{0,1\}^{v}$
that converts binary number representations of $\log v$ bits into one-hot vectors.
This can be accomplished by using fuzzy logic operators to convert 
$$f(x)_i=\bm1[i=x]$$
into 
$$f(x)_i = \prod_{j=1}^{\log v}(i_jx_j)+((1-i_j)(1-x_j))-(i_jx_j)((1-i_j)(1-x_j))$$
using definitions of [product $\top$-norms and $\top$-conorms](https://arxiv.org/pdf/2002.06100.pdf) and the fact that 
$$\bm1[a=b]=(a\land b)\lor(\lnot a\land\lnot b).$$

Why did I ask this? 
[My previous post](/deep-ba-sampling.html) explored a generalized version 
of the cross-entropy minimization assumption from [my recent paper](http://arxiv.org/abs/2310.01693).
This function could be used to make that assumption about the input IDs $h$ to a language model
while keeping the dimension of $\nabla\texttt{logits}(h)$ small.
