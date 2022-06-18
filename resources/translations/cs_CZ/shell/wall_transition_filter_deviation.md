Filtr ohraničení přechodu stěny
====
Některé modely mají tenké části vznášející se kolem prahu, kde se používá různý počet stěn. To může způsobit, že se počet stěn střídá sem a tam, i když se skutečná šířka dílu příliš neliší. Střídání kazí kvalitu tisku, vyžaduje spoustu změn toku a přidává další pohyby. Při použití této funkce se odstraní přechody, pokud by se přecházelo tam a zpět.

Když se přechod odstraní, mohou být dočasně některé linie příliš široké nebo příliš tenké. Toto nastavení omezuje, které přechody budou odfiltrovány, tím, že omezuje, o kolik může být linie širší nebo tenčí.

![S nízkým ohraničením se liniie střídavě pohybují mezi 2 a 3 stěnami.](../../../articles/images/wall_transition_filter_off.png)
![S vyšším ohraničením se již linie nestřídají](../../../articles/images/wall_transition_filter_on.png)

Přesněji řečeno, linie mohou být tenčí než [Minimální šířka linie stěny](min_wall_line_width.md) o tuto rezervu, pokud to brání přecházení mezi různými počty stěn. Stejně tak je povoleno, aby se linie staly o tuto rezervu mírně širší, i když by se do nich vešla i další stěna o minimální šířce linie stěny.

Cílem tohoto filtru je vyřešit běžný problém s tenkými díly pomocí 3D sítí s nízkým rozlišením. 3D model složený z plochých trojúhelníků nemůže křivku reprezentovat přesně, ale pouze ji aproximuje. Křivka bude mít hrany, mezi nimiž budou rovné plochy. Při modelování zakřiveného dílu s konstantní šířkou je důležité, aby hrany na vnější straně lícovaly s hranami na vnitřní straně. Pokud tomu tak není, šířka kruhu se mírně mění, což může způsobit výše uvedený efekt. Pokud se tak stane, měl by přechodový filtr zabránit příliš velkému efektu.

Zvětšení ohraničení v některých případech zabraňuje vytváření malých úseček. Tisk je tak rychlejší a povrch může vypadat hladší. Umožňuje však také extrémnější šířky linií, které se nemusí dobře vytlačovat z trysky. Při tisku modelů s nízkým rozlišením a tenkými dílky může zvýšení hranice pomoci zlepšit kvalitu. U náročných materiálů je lepší zůstat na bezpečné straně.

**Toto nastavení se nevztahuje pouze na běžné stěny, ale také na dodatečné stěny, podpůrné stěny, výplňové stěny a soustředné vzory.**