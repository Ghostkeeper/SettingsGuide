Délka přechodu mezi stěnami
====
U tenkých dílů se do tvaru nevejdou všechny stěny. Pokud je díl na některých místech tenčí než na jiných, musí Cura na některých místech použít jiný počet stěn. Toto nastavení řídí, jak široká bude přechodová oblast v místech, kde přidá nebo odebere jednu ze stěn.

![Velmi krátký přechod](../../../articles/images/wall_transition_length_0_2.png)
![Delší přechod](../../../articles/images/wall_transition_length_1_5.png)

Přechodová oblast mezi různými počty stěn má vždy drobné problémy. Nejvíce je to patrné, když jedna linie uprostřed končí a dvě okolní stěny musí mezeru vyplnit. Ty však prostor nevyplní okamžitě a vznikne mezera. Výsledkem jsou drobné otvory v horní a dolní části výtisků. Opačná situace nastane, když se dvě stěny spojí v jednu, což způsobí, že se na chvíli překryjí, dokud se nespojí. Přesah může vést k rozměrové nepřesnosti, zejména tam, kde k němu dochází u vnější stěny. Tomu všemu lze zabránit tím, že přechod bude co nejkratší.

Krátký přechod však také způsobuje, že tryska musí udělat několik velmi ostrých zatáček, aby tuto mezeru rychle vyplnila. To má za následek větší zvlnění, zejména pokud k němu dochází při tisku vnější stěny. Delší přechod snižuje zrychlení v trysce, zejména pokud se tím sníží pod limit [ryvu (jerku)](../speed/jerk_print.md).

Pro začátek je vhodné nastavit tuto délku na jedno- až dvojnásobek šířky řádku. Tiskárny se slabšími rámy nebo těžšími tiskovými hlavami ji mohou potřebovat zvýšit, zatímco tiskárny, které mohou rychle zrychlovat bez drnčení, si mohou dovolit přechod zkrátit, aby se zlepšila vizuální kvalita.

**Toto nastavení se nevztahuje pouze na běžné stěny, ale také na dodatečné stěny, podpůrné stěny, výplňové stěny a soustředné vzory.**