Zahájit vrstvy se stejnou součástí
====
Původně tento parametr způsobil, že tiskárna zahájila každou vrstvu s objektem nejblíže poloze určené v parametrech [X začátku vrstvy](layer_start_x.md) a [Y začátku vrstvy](layer_start_y.md), místo objektu, který byl naposledy vytištěn v předchozí vrstvě.

**Parametr byl v Cura 2.4 skryt, ale nebyl správně odstraněn, proto tento parametr v tomto seznamu stále existuje. Nemá to však žádný vliv na tisk.**

Po implementaci vícezávitových řezů již nebylo možné alternativní chování, takže nastavení bylo skryto.

Tisk každé vrstvy ve stejném pořadí se vyhne stohování dvou vrstev na sebe bezprostředně za sebou, pokud je k tisku několik částí. To umožňuje předchozí vrstvě vychladnout déle, když je tryska zaneprázdněna tiskem ostatních částí. To zlepšuje přesah a snižuje pásy a ochabování. Na druhé straně to způsobí, že se tiskárna pohybuje o něco více a lehce se zvyšuje doba tisku.