- 4G (LTE):
	- Frequenze di operazione: 450 MHz fino a 3.8 GHz
	- Dimensione celle: in aree urbane < 1 km, aree rurali da 5 km fino a 100 km
- 5G medium band:
	- Frequenze: 1.7 GHz fino a 4.7 GHz
	- Dim. celle: le microcelle coprono 0.5 km - 2.5 km, usate indoor o in aree urbane delimitate
- Cose che usano la banda L
- UMTS/3G:
	- Frequenze: 850 MHz fino a 2.5 GHz, frequenze primarie attorno ai 2 GHz
	- Dim. celle: le macrocelle solitamente vanno da 1 km a 5 km
- HSPA:
	- Supporta frequenze da 850MHz a 2,6 GHz, quelle usate più di frequente stanno attorno ai 2/2,1 GHz. In generale, HSPA è un'evoluzione di UMTS, quindi probabilmente possiamo applicare gli stessi parametri
- Wimax (parte dai 2GHz):
	- Frequenze: 2/2.3 GHz fino a 60 GHz
	- Dim. celle: qualche chilometro (max 50/100, media non specificata)
- PCS:
	- Frequenze: 1.8 GHz in Europa (UK), 1.9 GHz negli USA
	- Dim. celle non specificata (PCS è solo un insieme di frequenze destinate all'uso per cellulari)
	- Sembra un termine generico per indicare reti cellulari digitali, a differenza delle vecchie reti cellulari analogiche
- HiperMAN:
	- Frequenze: 2-11 GHz, banda principale 3.5 GHz
	- Dim. celle: 2 km - 10 km
	- Alternativa europea a Wimax


## 5G

**Frequenze:** [Wikipedia](https://it.wikipedia.org/wiki/Bande_di_frequenze_5G_NR) dice che il 5G NR (livello fisico del 5G) usa (tra le altre) le bande n1, n2, n3, che coprono le frequenze da 1.7 GHz a 2.1 GHz; inoltre sono presenti anche bande che arrivano a 1.5 GHz. Altri link che dovrebbero contenere la stessa informazione:
- [TS 38.104](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3202)
- [TS 38.101-1](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3283)
- [TS 38.101-2](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3284)
- [TS 38.101-3](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3285)
- [TS 38.101-4](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3366)
- [TS 38.101-5](https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=3982)

**Potenza di trasmissione:** consideriamo trasmissioni in microcelle (che coprono circa 2km max).

| Sito                 |  Potenza di trasmissione    |       Note      |
|----------------------|-----------------------------|-----------------|
| [Sito 1](https://www.essentracomponents.com/en-us/news/industries/telecoms-data/a-guide-to-5g-small-cells-and-macrocells)             |          33-37 dBm          |                 |
| [Sito 2](https://www.ti.com/lit/wp/slyy166/slyy166.pdf?ts=1700663338553&ref_url=https%253A%252F%252Fwww.ti.com%252Fabout-ti%252Ftrade-shows-conferences%252Fembedded-world.html)             |          30-40 dBm          |                 |
| [Wikipedia](https://en.wikipedia.org/wiki/5G)          |          37-40 dBm          |                 |
| [Sito 4](https://dgtlinfra.com/small-cells-microcell-picocell-femtocell/)             |          33-43 dBm          |  (riferito LTE) |

Potremmo prendere come massima potenza di trasmissione 40 dBm (come assunzione, basta specificarlo).
- TS 38.104 specifica che per trasmissioni di medio raggio la potenza per base station di tipo 1C e 1H (che non so cosa siano) deve essere $\le$ 38 dBm
Direi che potremmo scegliere 38 o 40.