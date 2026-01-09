---
title: Obtaining logprobs from an LLM API
date: 2024-10-21
author: "Matthew Finlayson"
html-math-method: mathjax
---

# Introduction

Many LLM APIs give top-$k$ logprobs in their outputs. What if we want to obtain *all* the logprobs? Here I present two algorithms for obtaining logprobs from an LLM API. Both of these depend on the API allowing us to add a logit bias to any token. The second is a generalization of the first.

# Full logprobs in $v$ API calls

Suppose for every call to the API we add a bias term $b\in\mathbb{R}$ to a token $i\in\mathbb{N}$. This means that the model’s logits $\boldsymbol\ell$ are modified to
$$
\boldsymbol\ell'=(\ell_1,\ell_2,\ldots,\ell_i+b,\ldots,\ell_v).
$$
If we collect the biased output $\log p_i'=\log\mathrm{softmax}(\boldsymbol\ell')_i$ for each token $i$, we now have
$$
\begin{aligned}
\log p_i'
&=\log\frac{\exp(\ell_i+b)}{\exp(\ell_i+b)+\sum_{j\neq i}\exp \ell_j} \\
&= \log\frac{\exp\ell_i}{\exp\ell_i+\exp(-b)\sum_{j\neq i}\exp \ell_j},
\end{aligned}
$$
which we can exponentiate and rearrange to get
$$
\begin{aligned}
\frac{\exp(-b) p'_i}{1-p'_i} &= \frac{\exp\ell_i}{\sum_{j\neq i}\exp\ell_j}.
\end{aligned}
$$
Note that the righthand side is the *odds* of the token, therefore we can solve for the unbiased probability $p_i$ of the token
$$
\begin{aligned}
\frac{p_i}{1-p_i} &=
\frac{\exp(-b) p'_i}{1-p'_i} \\
p_i &= \frac{\exp(-b) p'_i}{1-p'_i+\exp(-b) p'_i} \\
\log p_i &= \log p'_i + \log \frac{\exp(-b)}{1-p'_i+\exp(-b) p'_i} \\
\log p_i &= \log p'_i - \log\left(\exp b -\exp(b + \log p'_i)+p'_i\right) \label{eq:prob}
\end{aligned}
$$
Thus, it is possible to obtain unbiased logprobs for any token with exactly 1 API call.

# Full logprobs in $v/k$ API calls

We can adapt this algorithm to solve for $k$ logprobs at a time simultaneously. Without loss of generality, let us solve for tokens 1-$k$ and assume that $\exp\ell_1=1$ (since logprobs are invariant to uniform logit translation). Setting $\lambda=\exp(-b)$ for convenience, we can solve for each $\exp\ell_i$
$$
\begin{aligned}
p_i'
&=\frac{\exp\ell_i}{\sum_{j\in[k]}\exp\ell_j+\lambda\sum_{j\not\in[k]}\exp\ell_j} \\
\frac{\exp\ell_i}{p'_i} &= \sum_{j\in[k]}\exp\ell_j + \lambda\sum_{j\not\in[k]}\exp\ell_j \\
\exp\ell_i &= \frac{p'_i}{p'_1}
\end{aligned}
$$
which in turn allows us to solve for $p_i$
$$
\begin{aligned}
\frac{\exp\ell_i}{p_i'}
&= \sum_{j\in[k]}\exp\ell_j + \lambda\sum_{j\not\in[k]}\exp\ell_j \\
\frac{\exp\ell_i}{\lambda p_i'} - \frac1\lambda\sum_{j\in[k]}\exp\ell_j &=
\sum_{j\not\in[k]}\exp\ell_j \\
\frac{\exp\ell_i}{\lambda p_i'} - \frac1\lambda\sum_{j\in[k]}\exp\ell_j &= \frac{\exp\ell_i}{p_i} - \sum_{j\in[k]}\exp\ell_j \\
p_i &= \frac{\lambda p'_i\exp\ell_i}{\exp\ell_i + p'_i(\lambda -1)
\sum_{j\in[k]}\exp\ell_j} \\
p_i &= \frac{\lambda p'_i}{1 - \sum_{j\in[k]}p'_j + \lambda\sum_{j\in[k]}p'_j}
\end{aligned}
$$
which we can take the log of and obtain
$$
\begin{aligned}
\log p_i &= \log p'_i - \log\left(\left(1 - \sum_{j\in[k]}p'_j\right)\exp b + \sum_{j\in[k]}p'_j\right). \label{eq:parallel}
\end{aligned}
$$

# Top-$n$ logprobs

Since most of the probability is often concentrated in the top-$n$ tokens, one may wish to gather logprobs for only these top tokens and skip lower-probability tokens. This can be done by adding a penalty bias $-b$ to tokens that have known logprob to surface the next-highest-probability batch of $k$ tokens. We can then solve for the unbiased probability of new batch as follows. First, solve the biased softmax for $\exp\ell_i$
$$
\begin{aligned}
p'_i &=
\frac{\exp\ell_i}{\sum_{j=i}^v\exp\ell_j +
\exp(-b)\sum_{j=1}^{i-1}\exp\ell_j} & \text{Biased softmax} \\
\exp\ell_i &= p'_i\left(\sum_{j=i}^v\exp\ell_j +
\exp(-b)\sum_{j=1}^{i-1}\exp\ell_j\right) \label{eq:bs}
\end{aligned}
$$
as well as the unbiased softmax
$$
\begin{aligned}
p_i &=
\frac{\exp\ell_i}{\sum_{j=1}^v\exp\ell_j} & \text{Unbiased softmax} \\
\exp\ell_i &= p_i\left(\sum_{j=1}^v\exp\ell_j\right) \label{eq:ubs}
\end{aligned}
$$
which we can combine and simplify using the arbitrary assumption that
$$
\sum_{j=1}^{i-1}\exp\ell_j=1
$$
$$
\begin{aligned}
p_i\left(\sum_{j=1}^v\exp\ell_j\right) &=
p'_i\left(\sum_{j=i}^v\exp\ell_j + \exp(-b)\sum_{j=1}^{i-1}\exp\ell_j\right) \\
p_i\left(1 + \sum_{j=i}^v\exp\ell_j\right) &= p'_i\left(\sum_{j=i}^v\exp\ell_j + \exp(-b)\right) & \text{Assume $\sum_{j=1}^{i-1}\exp\ell_j=1$}
\label{eq:pi}.
\end{aligned}
$$
We can now use the fact that we know the sum of the first $i-1$ probabilities to solve for
$$
\sum_{j=i}^v\exp\ell_j
$$
$$
\begin{aligned}
\sum_{j=1}^{i-1}p_j&=\frac{\sum_{j=1}^{i-1}\exp\ell_j}{\sum_{j=1}^v\exp\ell_j}
& \text{Softmax defn.} \\
&= \frac1{1+\sum_{j=i}^v\exp\ell_j} & \text{Recall $\sum_{j=1}^{i-1}\exp\ell_j=1$} \\
\sum_{j=i}^v\exp\ell_j &= \frac1{\sum_{j=1}^{i-1}p_j} - 1
\label{eq:sump}
\end{aligned}
$$
and substitute this into our result from earlier to solve for $p_i$
$$
\begin{aligned}
\frac{p_i}{\sum_{j=1}^{i-1}p_j} &=
p'_i\left(\frac1{\sum_{j=1}^{i-1}p_j} - 1 + \exp(-b)\right) \\
p_i &= p'_i\left(1 + (\exp(-b)-1) \sum_{j=1}^{i-1}p_j\right).
\end{aligned}
$$
