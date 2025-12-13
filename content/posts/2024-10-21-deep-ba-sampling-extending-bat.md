---
title: Deep BA Sampling
date: 2024-10-21
author: "[Matthew Finlayson](/index.html)"
html-math-method: mathml
---

TL;DR: we can use *any* intermediate LM representation to prove that a subset of next-token candidates have non-zero probability.

In my paper ["Closing the Curious Case of Neural Text Degeneration"](https://openreview.net/forum?id=dONpC9GL1o),
we show that when a LM outputs the embedding $h$, 
and we assume that the model outputs the distribution $\hat{p}$ 
that minimizes cross entropy with the true distribution $p\ast$,
we get the resulting relationship
$$\nabla\texttt{crossentropy}(h)=0 \quad \Rightarrow \quad W^\top p\ast=W^\top\hat{p}.$$
This is useful because we can use it as a linear constraint in order to tell whether a particualar token has nonzero true probability, i.e.,
if there is no solution $p$ such that
$$W^\top p = W^\top\hat{p},\quad p_i=0,\quad 0\leq p\leq 1$$
then $p_i>0$.

We were able to get this linear set of constraints by considering the gradient with respect to the final embedding $h$, but what about earlier representations in the model?
For instance, what if we consider the representation $h'$ from before the final layer norm?
As part of the derivation in the paper, we obtain the equality
$$\nabla(h\mapsto Wh)^\top p\ast=\nabla(h\mapsto Wh)^\top\hat{p},$$
which is simply the first chain rule expansion of the model gradient with respect to $h$.
Importantly, $\nabla(h\mapsto Wh)$ is the Jacobian of the vector function $h\mapsto Wh$.
If we swap out the final embedding $h$ for the pre-layernorm representation $h'$,
we can obtain the relation 
$$\nabla(h'\mapsto W\texttt{layernorm}(h'))^\top p\ast=\nabla(h'\mapsto W\texttt{layernorm}(h'))^\top\hat{p}.$$
More generally, with a slight abuse of notation, 
let $\texttt{logits}:\mathbb{R}^?\to\mathbb{R}^v$ 
be the mapping from any intermediate model representation to the model logits.
For every intermediate representation $h$ we will have
$$\nabla\texttt{logits}(h)^\top p\ast=\nabla\texttt{logits}(h)^\top\hat{p}.$$

What does this mean?
It means we have LOTS of linear constraints that we can add to our program.
I am curious which ones will be useful, and whether we could use this to make our program more efficient.
If we used ALL of the constraints, we would have an over-constained program, 
potentially meaning fewer or no token rejections.
If there is some specific structure to the constraints we could perhaps find efficient approximations. 
Instead of approximating the Jacobian with SVD, could we take the Jacobian w.r.t. a subset of the representations?
