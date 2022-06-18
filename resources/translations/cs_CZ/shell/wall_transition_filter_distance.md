Filtr vzdálenosti přechodu stěny
====
Některé modely mají tenké části vznášející se kolem prahu, kde se používá různý počet stěn. To může způsobit, že se počet stěn střídá sem a tam, i když se skutečná šířka dílu příliš neliší. Střídání kazí kvalitu tisku, vyžaduje spoustu změn toku a přidává další pohyby. Při použití této funkce se přechody odstraní, pokud by se do určité vzdálenosti přešlo tam a zpět.

![Bez filtru dochází ke střídání mezi 2 a 3 stěnami](../../../articles/images/wall_transition_filter_off.png)
![S filtrem již ke střídání nedochází](../../../articles/images/wall_transition_filter_on.png)

Když se přechod odstraní, mohou být dočasně některé linie příliš široké nebo příliš tenké a překročit [Minimální šířku linie stěny](min_wall_line_width.md). Přece jen tam byl přechod, aby lépe odpovídal šířce dílu. Bez tohoto přechodu se použije menší nebo větší množství stěn, než by bylo ideální, a šířka těchto stěn se podle toho upraví. To je povoleno až do výše [Filtru ohraničení přechodu stěny](wall_transition_filter_deviation.md). Pokud se šířka stěn příliš liší, přechod se neodstraní.

Cílem tohoto filtru je vyřešit běžný problém s tenkými díly pomocí 3D sítí s nízkým rozlišením. 3D model složený z plochých trojúhelníků nemůže křivku reprezentovat přesně, ale pouze ji aproximuje. Křivka bude mít hrany, mezi nimiž budou rovné plochy. Při modelování zakřiveného dílu s konstantní šířkou je důležité, aby hrany na vnější straně lícovaly s hranami na vnitřní straně. Pokud tomu tak není, šířka kruhu se mírně mění, což může způsobit výše uvedený efekt. Pokud se tak stane, přechodový filtr by měl zabránit tomu, aby to mělo příliš velký vliv.

Zvětšení vzdálenosti v některých případech zabraňuje vytváření malých úseček. Tisk je tak rychlejší a povrch může vypadat hladší. Způsobuje však také, že větší část tisku má extrémní šířku čar, které se nemusí dobře vytlačovat z trysky. Při tisku modelů s nízkým rozlišením a tenkými kusy může zvětšení vzdálenosti pomoci zlepšit kvalitu. U náročných materiálů je lepší zůstat na bezpečné straně.

**Toto nastavení není v současné době pro uživatele viditelné. Filtr lze nastavit pouze pomocí možnosti [Filtru ohraničení přechodu stěny](wall_transition_filter_deviation.md). Ovlivňuje nejen běžné stěny, ale také dodatečné stěny, opěrné stěny, výplňové stěny a soustředné vzory.**