La loss è definita come:
- Nel dominio lineare: $L = \frac{p_t}{p_r} = \frac{1}{g} = \frac{1}{g_tg_rg_p}$
- Nel dominio logaritmico: $L^{(dB)} = \left[ \frac{p_t}{p_r} \right]^{(dB)} = 10 \log \frac{p_t}{p_r}= -10 \log \frac{p_r}{p_t} = -10 \log(g_tg_rg_p) = -g_t^{(dB)} - g_r^{(dB)} - g_p^{(dB)}$
Possiamo vedere la loss come $L= L_p^{(dB)}-g_t^{(dB)}-g_r^{(dB)}$

**Obiettivo del progetto:** data la distanza $d$ e la deviazione standard $\sigma$, trovare la *probabilità* di stabilire un link per un dispositivo a distanza $d$, con fluttuazioni del gain dovute allo shadowing (modellate attraverso una variabile casuale normale con deviazione standard $\sigma$).
Noi abbiamo il modello per la loss (senza tenere conto dello shadowing), in base alla tecnologia scelta per stabilire un link bisogna avere una certa potenza di trasmissione ($\le$ a una potenza max $p_{\max}$) e una certa potenza minima di ricezione (sensibilità, $p_{min}$). In base

