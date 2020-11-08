Aktivovat doběh
====
Pokud je toto nastavení povoleno, tryska zastaví vytlačování materiálu před uzavřením kontury stěny. Myšlenka je taková, že komora trysky se pak může vyprázdnit na poslední linii, což snižuje tlak na trysku a umožňuje, aby začátkem kontury blokována. Tím se vytvoří méně švu, kde začíná kontura, a omezuje se strunování v následujícím pohybu.

![V pohledu vrstev je šev snadno patrný, pokud je doběh povolen, protože je tam pohyb přesunu](../../../articles/images/coasting_enable.png)

Aktivace doběhu má za cíl snížit viditelnost švu ve stěnách. Pokud máte normálně velké švy, aktivace této funkce může tento efekt zmenšit. Toto je v podstatě opak toho, co dělá [Vzdálenost otěru vnější stěny](../shell/wall_0_wipe_dist.md), před pokusem o doběh je proto vhodné pokusit se omezit otírání.

Doběh bude teoreticky vždy vytvářet podtlak. Zda je viditelný nebo ne při skutečném tisku závisí na okolnostech. U tiskáren s přímým pohonem bývá doběhu o něco efektivnější. Pokud má vaše tiskárna přímý pohon, budete chtít snížit [objem doběhu](coasting_volume.md) na nižší hodnotu než při použití bowdenových trubiček nebo pružných hnacích hřídelů, protože reakce průtoku je pak mnohem rychlejší. U bowdenových systémů podávání bude také mnohem obtížnější řídit hodnotu doběhu, aby se účinně snížila viditelnost švu.