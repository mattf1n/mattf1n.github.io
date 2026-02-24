---
title: Sequence-level Temperature Sampling
author: "[Matthew Finlayson](index.html)"
---

Temperature sampling is a popular token-level decoding method for LLMs, where for a temperature $\tau$ the un-normalized probability distribution over next tokens is
$$ p(x_{t}\mid x_{<t})^{\frac1\tau}.$$
which approaches the uniform distribution as $\tau\to\infty$ and places all probability mass on the most likely token as $\tau\to0$. 

For a moment I wondered whether sampling from this token-level distribution is equivalent to sampling from the sequence-level distribution
$$ p(\boldsymbol{x})^{\frac1\tau}.$$
This is the case when $\tau=1$,
but not for other values of $\tau$.
One can verify this by noting that if this were true, then temperature sampling with $\tau=0$ would satisfy the MAP decoding objective (finding the most likely sequence) when in reality it is only greedy decoding. 

Best-of-$n$ sampling gets closer, since it approaches MAP as $n\to\infty$. 
