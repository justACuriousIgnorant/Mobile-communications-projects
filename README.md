# Mobile and Wireless Systems projects

This repository contains three projects for the **Mobile and Wireless Systems** course of the Alpen-Adria Universität Klagenfurt, winter semester 2023.

## Project 1

The requested task is to study the behaviour of a wireless technology under the effects of *path loss* and *shadowing*, using the [COST231-Hata model](https://en.wikipedia.org/wiki/COST_Hata_model).

The studied technology is 5G, using the n1, n2 and n3 frequency bands.
The following parameters for the model are used, accordingly to 3GPP's specifications:
- Transmit power $p_t$: 56 dBm
- Receiver sensitivity $\theta$: -96 dBm
- Transmit height: 40 m
- Receiver height: 3 m
- Frequencies: 1.7 to 2 GHz

The study consists in two parts: and analytical study and a simulation.

### Analytical study

The COST model is used to compute the loss of a user at a certain distance $d$, 0 < $d$ < 10 km; given the outage loss $L_{max} = p_t - \theta$, the probability of establishing a link depends on a shadowing factor, modeled by a random variable $X \sim N(0,\sigma^2)$, for a given standard deviation $\sigma$.

The probability of having a link is thus
$$
P[link] = P[L+X < L_{max}] = P[X < L_{max}-L]
$$
$$
P[X<L_{max}-L] = \frac{1}{2}\left[1+\text{erf}\left(\frac{L_{max}-L}{\sqrt2\cdot\sigma}\right)\right]
$$
We plot the behaviour of this function over the distance and different values of $\sigma$:
![](figures/prob_distance_and_sigma.png)

### Simulation

For the simulation, we generate $n$ samples $x_i$ from $N(0,\sigma^2)$, with $\sigma=$ 5. These represent the shadowing factors of each receiver $r_i$, at a set distance $d$. For each $r_i$, the loss is computed using the COST model, and for each distance $d$ we compute the percentage of receivers such that $L_{r_i}+x_{i} < L_{max}$. This represents the probability of establishing a link, and the results are compared to the analytical model:
![sim_compare](figures/sim_compare.png)