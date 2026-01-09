---
title: The "Right Way" to Ensemble Language Models
date: 2024-10-21
author: "[Matthew Finlayson](/index.html)"
html-math-method: mathjax
---

Suppose you have $n$ langauge models with embedding size $d$, vocabulary size $v$, and softmax matrices $\boldsymbol W_1, \boldsymbol W_2,\ldots,\boldsymbol W_n\in\mathbb{R}^{v\times d}$ and you want to sample from them as an ensemble.
One naive way to accomplish this would be to average their logits $\boldsymbol\ell_1,\boldsymbol\ell_2,\ldots,\boldsymbol\ell_n$ and sample from
$$\boldsymbol{\hat{p}} = \mathrm{softmax}\left(\sum_{i=1}^n\boldsymbol\ell_i / n\right).$$
This presumably averages out distributional errors from individual models.

But what if we assume that the models' errors only come from the softmax bottleneck?
Using the techniques from [my recent paper](http://arxiv.org/abs/2310.01693)
it is possible to exactly pinpoint the set of possible true distributions 
as the solutions $\boldsymbol{p}$ that satisfy the constraints 
$$\boldsymbol{p}\boldsymbol{W}_i = \boldsymbol{\hat{p}}_i\boldsymbol{W}_i$$
for $i=1,2,\ldots,n$ where $\boldsymbol{\hat{p}}_i$ is model $i$'s next-token distribution.
It appears that sampling from some solution $\boldsymbol p$ to the above equation would be a principled approach to sampling from the union, since both models "agree" that this could be the true distribution.

Note that if $nd=v$ then there is only one such solution,
and if $nd>v$ there will be no such solution, in which case we might opt for the least squares solution.
In the case where $nd < v$ there will be many solutions, 
and it is not clear to me which solution to choose here.
Since the models are trained to minimize cross entropy with the true distribution
we can choose a solution that minimizes the sum of the models' cross entropy
$$\boldsymbol{p}^\ast = \arg\min_\boldsymbol{p} -\sum_{i=1}^n\boldsymbol{p}^\top\log\boldsymbol{\hat{p}}_i,$$
which can be found via linear programming.
If we don't want any one models' cross entropy to be high, 
I believe we can also solve for
$$\boldsymbol{p}^\ast = \arg\min_\boldsymbol{p} \sum_{i=1}^n(\boldsymbol{p}^\top\log\boldsymbol{\hat{p}}_i)^2$$
using quadratic programming.
Note that without the linear constraints,
these solutions would simply be the one-hot vector indicating 
$$\arg\min_i-\sum_{j=1}^n\log\hat{p}_{ij}.$$
Alternative approaches might be to minimize the under-estimation of the token log-probabilities, 
or minimize the true probability distributions cross entropy with the predicted distributions.
It is not clear to me yet whether any of these strategies or assumptions are equivalent or better than one another.
