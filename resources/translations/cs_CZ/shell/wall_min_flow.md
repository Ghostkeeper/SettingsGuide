Minimální tok pro stěny
====
Kompenzace překrývajících se linií stěn sníží tok pro některé stěny. To může být problematické, protože může snížit průtok libovolně nízko až na 1%, pokud se stěny téměř úplně překrývají. Tisk při extrémně nízkých průtocích nefunguje dobře. Má tendenci tvořit vzor kapiček místo vytlačovacích souvislých linií.

Toto nastavení transformuje linie s extrémně nízkým průtokem na pohyby přesunu a efektivně sníží jejich průtok na 0%. Materiál bude dále vytékat jako při běžných pohybech, ale nebude tvořit kapičky.

![Přesahy mezi stěnami jsou kompenzovány normálně](../../../articles/images/wall_min_flow_0.png)
![Stěny s méně než 50% extruzí jsou přeměněny na přesuny](../../../articles/images/wall_min_flow_50.png)

Tryska bude vždy sledovat dráhu stěny, aby vytékala na správné místo.

Zvýšením tohoto nastavení budou vaše stěny tenčí, než se požaduje. Namísto kreslení velmi jemných linií již nekreslíte nic. Technicky se jedná o pod-extruzi, díky kterému je vaše část tenčí, než se požaduje. Stěna by se přesto stejně dobře nevytiskla. Místo nakreslení dlouhé řady teček nebo korálků na stěnu se nevytiskne nic, což způsobí, že stěna bude trochu plynulejší.

Tento parametr nastavte na minimální průtokovou rychlost stěny, kterou může vaše tryska dosáhnout bez vytváření kapiček. Obecně je tato míra kolem 60%. Pokud by se šířka linií snížila pod 60%, vytvořily by se tyto kapičky, takže je výhodné transformovat tyto linie na pohyby přesunu. Pokud tisknete ve větších výškách vrstev nebo používáte silnější linie stěn, můžete toto nastavení trochu snížit, abyste získali větší rozměrovou přesnost.