Modello per la path loss in ambienti urbani. È applicabile per frequenze di trasmissione comprese tra $1.5\ \text{GHz}$ e $2\ \text{GHz}$, un'altezza dell'antenna $30\ \text{m} < h_t < 200\ \text{m}$, un'altezza di ricezione del dispositivo $1\ \text{m} < h_r < 10\ \text{m}$ e celle di raggio compreso tra $1$ e $10\ \text{km}$.

Date $f,h_t,h_r$ e $d$, la loss $L^{(dB)}$ per una città media è
$$\begin{split} 
	L^{(dB)} = & 45.5 + 35.46 \log \frac{f}{\text{MHz}} - \left(1.1 \log \frac{f}{[\text{MHz}]} - 0.7\right) \frac{h_r}{[\text{m}]} \\ &
+ \left(44.9 - 6.55 \log \frac{h_t}{[\text{m}]}\right) \log \frac{d}{[\text{km}]} - 13.82 \log \frac{h_t}{[\text{m}]} 
\end{split}$$

La loss poi fluttua attorno a questo valore per mezzo di variazioni casuali distribuite normalmente, con deviazione standard $\sigma^2$