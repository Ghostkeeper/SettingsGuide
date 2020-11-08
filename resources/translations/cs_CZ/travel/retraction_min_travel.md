Minimální přesun pro retrakci
====
Toto nastavení zabraňuje retrakci materiálu při velmi krátkých přesunech. Během těchto pohybů je velmi málo času na to, aby materiál unikl z trysky, takže retrakce by způsobila více škody než užitku.

![Nejkratší pohyb uprostřed není retrahován](../../../articles/images/retraction_min_travel.png)

Retrahování materiálu je určeno k zamezení strunování. Velmi krátké posuny nevytvářejí struny, protože materiál ještě neměl čas vytéct z trysky. Extrémně krátké pohyby přibližně šířky jedné linie budou dokonce zcela překrývající se linie, takže pro strunu nebude místo. Na druhé straně, retrakce způsobí, že tryska zůstane po krátkou dobu v klidu, zatímco je materiál v pohybu. To umožňuje, aby část materiálu vytekl a vytvořil tam kapku. Z těchto důvodů je obecně výhodné neretrahovat při přesunech na krátké vzdálenosti, i když jsou tyto stopy na viditelných částech modelu.

Pokud je toto nastavení příliš zvýšeno, budou stopy strunování v detailních částech modelu nebo pokud jsou součásti blízko sebe.