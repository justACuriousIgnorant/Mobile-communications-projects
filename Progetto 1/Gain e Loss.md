La loss è definita come:
- Nel dominio lineare: $L = \frac{p_t}{p_r} = \frac{1}{g} = \frac{1}{g_tg_rg_p}$
- Nel dominio logaritmico: $L^{(dB)} = \left[ \frac{p_t}{p_r} \right]^{(dB)} = 10 \log \frac{p_t}{p_r}= -10 \log \frac{p_r}{p_t} = -10 \log(g_tg_rg_p) = -g_t^{(dB)} - g_r^{(dB)} - g_p^{(dB)}$
Possiamo vedere la loss come $L= L_p^{(dB)}-g_t^{(dB)}-g_r^{(dB)}$

**Obiettivo del progetto:** data la distanza $d$ e la deviazione standard $\sigma$, trovare la *probabilità* di stabilire un link per un dispositivo a distanza $d$, con fluttuazioni del gain dovute allo shadowing (modellate attraverso una variabile casuale normale con deviazione standard $\sigma$).
Noi abbiamo il modello per la loss (senza tenere conto dello shadowing), in base alla tecnologia scelta per stabilire un link bisogna avere una certa potenza di trasmissione ($\le$ a una potenza max $p_{\max}$) e una certa potenza minima di ricezione (sensibilità, $p_{min}$). 
La loss massima per stabilire un collegamento dovrebbe essere:
$$L_{max} = \frac{p_{max}}{p_{min}}$$
Infatti se $p_r < p_{min}$ la loss aumenta rispetto a $L_{max}$ (abbiamo una potenza di ricezione troppo piccola); se invece $p_t > p_{max}$ trasmettiamo con più potenza di quanto potremmo, ma la perdita di segnale aumenta rispetto a quanto riceviamo.
**QUINDI:** noi vogliamo che la nostra $L$ calcolata con il modello COST213 sia sempre inferiore a $L_{max}$:
$$L \le L_{max}$$
Il modello non tiene conto dello shadowing, quindi la probabilità di stabilire un link è **la probabilità che $L+X \gt L_{max}$**:
$$P[link] = P[L+X < L_{max}] = P[X < L_{max}-L]$$
Questo dipende dalla distanza $d$ e dalla distribuzione $\sigma$ di $X$.