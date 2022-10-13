This repository contains experiments from our paper "A note on estimating global subgraph counts by sampling".

The included script calculates the minimum sample size $N$ as in our Corollary 5 with $\epsilon=0.1$ and $p=0.05$.

To choose $\Delta$ in (3.3), we take it the minimum such value that $\mathbb{E} \tilde{D}^{h-1} \mathbf{1}_{\tilde{D} \ge \Delta} \le \epsilon \mathbb{E} \tilde{D}^{h-1}$, where the random variable $\tilde{D}$ follows the empirical degree distribution. We assume that (3.3) holds with this $\Delta$ and $\lambda = \epsilon \mathbb{E} \tilde{D}^{h-1}$.

Thus, for the first experiment (contact count surveys) we make an assumption about $\Delta$ and $\lambda$ based on the empirical data, and for the second experiment (degree distributions from empirical networks), $\tilde{D}$ and the actual random degree $D$ have the same distribution, so (3.3) holds with the determined values for each tested graph.

As can be seen in the output in the `results/` directory (see the end of each file), for each degree distribution in our first experiment we got $\Delta \approx 100$, but this is approximately equal to the maximum degree in each survery. In each case there are just 1-3 data points with contact count $\ge Delta$, which suggests that more data might be needed to estimate $\mathbb{E} D^{h-1} \mathbf{1}_{D \ge \Delta}$ and determine $\lambda$ correctly.
