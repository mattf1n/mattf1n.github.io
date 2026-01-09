---
title: Heavy tails and diversity in model distributions
date: 2023-12-12
css:
  - ../style/main.css
html-math-method: mathjax
---

## Motivation

Direct sampling from model output distributions often gives incoherent outputs. Some have attributed this to a heavy tail, i.e., the model assigns too much probability to low-probability tokens. My goal is to test this hypothesis.

## Measuring heavy tails

To test the hypothesis we need to define what it means for a distribution to be heavy-tailed.

**Definition (Crossover).** A distribution $\hat p$ is heavy-tailed with respect to a distribution $p$ if $\hat p$ preserves the probability ordering of $p$ and there exists some element $i$ such that for all $j$, $\hat p_j > p(j)$ iff $p(j) < p(i)$. We say that $\hat p$ *crosses over* $p$.

In other words, there is a crossover point in the ordering of $p$ and $\hat p$ (which is identical) where all probabilities in the heavy-tailed distribution go from being less than original, to being greater than. The assumption of probability ordering is consistent with assumptions in previous work, where the output distribution is assumed to be the true distribution plus some smoothing.

We can use Hill numbers, a measure of diversity (see Section [Hill numbers](#hill-numbers)), to test whether one distribution crosses over another.

**Proposition (Crossover distributions have lower Hill numbers).**  
If $\hat p$ crosses over $p$, then
$$
{}^{q}D(\hat p) < {}^{q}D(p).
$$

*Proof sketch.* $\left(\sum_i\hat p_i^q\right)^\frac{1}{1-q} \leq \left(\sum_ip_i^q\right)^\frac{1}{1-q}$ because the sum is dominated by its largest components. ◻

More generally, we can define heavy-tailedness in terms of diversity. Intuitively, a more heavy-tailed distribution will give more diversity when sampled from. We can choose any Hill number as our metric. This relaxes the assumptions about crossover.

Another measure I am interested in is *kurtosis*. Kurtosis is interpreted as “the propensity of a distribution to produce outliers”. Is kurtosis defined for a categorical distribution?

Lastly, we might also try measuring distance from the uniform or the one-hot distribution.

## Hill numbers {#hill-numbers}

Both entropy and Simpson’s index are Hill numbers, which are measures of diversity. The Hill number ${}^{q}D$ is given by
$$
{}^{q}D=\left(\sum_ip_i^q\right)^\frac{1}{1-q}.
$$
Entropy is the Hill number ${}^{1}D$, Simpson’s index is ${}^{2}D$. As $q$ increases, ${}^{q}D$ gives increasing weight to the most likely tokens. The diversity is related to heavy-tailedness because heavier tails means more diversity.

## Approximating Hill numbers

Since we do not have direct access to the true distribution, only $\hat p$, we need some way to approximate ${}^{q}D(p)$.

### Dataset sampling

**Conjecture (Hill number approximation).**  
Under certain assumptions and with some value $q$, we can approximate the Hill number ${}^{q}D$ with
$$
\mathop{\mathrm{\mathbb E}}_{p\sim P}
    \left[{}^{q}D(p)-{}^{q}D(\hat p)\right]
    \geq \left(
    \mathop{\mathrm{\mathbb E}}_{i\sim P}\left[\hat p_i^{q-1} 
    - {}^{q}D(\hat p)\right]
    \right)^\frac{1}{1-q}.
$$

Now, to test whether the model distribution is heavy-tailed compared to the true distribution, we can run inference on the corpus and compare expected probabilities to the true probabilities. Formally, the LM distribution is heavy-tailed with respect to the true distribution if
$$
  \mathop{\mathrm{\mathbb E}}_{\hat p,\mathrm{gold}\sim P}\left[\hat p_\mathrm{gold}-\mathop{\mathrm{\mathbb E}}_{i\sim\hat p}[\hat p_i]\right] > 0,
$$
where $D$ is a corpus from which we sample gold tokens and model next-token distributions.

### Results

We sample the first $366{,}456$ tokens of the Pile test set and feed them to GPT-Neo-125M. The result of our metric is $-0.00320$ with a standard error of $0.000274$. This suggests that the model’s next-token distribution is *not* heavy tailed. Using entropy instead of Simpson’s index we have a mean difference of $-0.0124$ and a standard error of $0.00347$, which seems to give the opposite conclusion: that the tail is *not* heavy.

One possible issue with this metric is that it may require assuming that all $\hat p$ distributions are similar. This may be problematic since $\hat p_\mathrm{gold}-\mathop{\mathrm{\mathbb E}}_{i\sim\hat p}[\hat p_i]$ is bounded above by $\sqrt{\mathop{\mathrm{\mathbb E}}_{i\sim\hat p}[\hat p_i]}-\mathop{\mathrm{\mathbb E}}_{i\sim\hat p}[\hat p_i]$ and below by $-\mathop{\mathrm{\mathbb E}}_{i\sim\hat p}[\hat p_i]$ as the vocabulary size grows. To remedy this, we can control for expected probability, to separate different distributions.

## Oracle model

Suppose we have 2 models, a small model parameterized by $\vartheta$ and a large model parameterized by $\theta$, such that the large model achieves lower perplexity on the test set, i.e., the large model is a better approximation of the true distribution. We can then compare the diversity of $p_\vartheta$ to $p_\theta$ over the test set. GPT-Neo-1.3B shows lower entropy on average than GPT-Neo-125M, suggesting the larger model has a less diverse tail.

We now have some conflicting results. Larger models have lower entropy on average, but our dataset sampling method suggests that the models are *not* hedging as much as they should. Perhaps the models are overconfident in the *wrong* tokens.

**Hypothesis (Non-fat tails).**  
Truncation works not because distribution tails are too fat, but because there are more mistakes outside the head. For a better model, the “safe zone” will expand.

## Disambiguating fat tails and disordered predictions

Two hypotheses: truncation sampling works because

- the model smooths the true distribution. Truncation sampling desmooths.
- the model gives a distribution where only most probable tokens follow the true distribution.

One way they could be different: tokens sampled from a smoothed distribution will have a lower mean probability than directly sampled tokens. This is because lower-probability tokens are more likely to be sampled by a smoothed probability distribution. If the sampled tokens have an equal or higher mean probability, it must be that the distribution is not a smoothed one.

Is it possible for the distribution to be less peaked but have a higher dot product? No. But it is possible for the distribution to be more peaked but have a lower dot product. In this case the original distribution is *not recoverable* from the estimation, except by extreme truncation sampling.

Every transformation of the probability distribution is a scale and rotation about the uniform distribution in $|V|-1$ dimensions. There are limits to the extent that the support of the original distribution can be recovered via truncation.

## Measuring the scaling factor between two models

Given model distribution $p$ and oracle distribution $p^*$, we want to find the amount of uniform smoothing applied to $p^*$ to obtain $p$. To do this, we can take $p$ and $p^*$ with respect to the uniform distribution by observing $p-u=p'$ and $p^*-u={p^*}'$. We can then have $p'={p^*}'A$ ($p'$ is a linear transformation of ${p^*}'$).

## Upper bounding the scaling required to recover the support

A model outputs some distribution $p$ which is the true distribution $p^*$ with some scaling $\lambda$ and rotation $R$ applied such that $p=\lambda R p$. We want to find some new scaling factor $\lambda'$ and rotation $R'$ such that the if $p^*_i=0$ then $\lambda'R'p_i<=0$. The intuition here is that the true distribution lies on a boundary of the simplex. Some scaling and rotation is applied which brings the probability to the inside of the hull. We want to rescale and rerotate the probability again to bring it outside the hull in a way that avoids exiting the hull along boundaries that the original distribution was not touching.

## Are model distributions smoothed?

Two working questions:

- Are distributions smoothed via uniform mixing?
- Do smoothing assumptions in prior work hold, or is there a weaker form we can lean on?
