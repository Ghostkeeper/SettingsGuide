Rozdělit podpěru na bloky
====
Pokud je pro podpěru použit [vzor](../support/support_pattern.md) cikcak, může být podpěra zmačkaná, jako snadný způsob, jak ji odstranit. To je obtížnější, pokud je podpěra velmi široká. Při tomto nastavení je cikcak podpěra rozdělena na bloky, které se snáze jednotlivě oddělují, ale jsou stále dostatečně široké, aby si udržely svou stabilitu.

![Každých 8 řádků je ponecháno spojovací vedení, které rozděluje podpěru na části](../../../articles/images/support_skip_some_zags.png)

Rozdělením podpěry na bloky je snazší ji oddělit, protože je můžete odlomit jeden po druhém. To však mírně snižuje pevnost a tuhost podpěry, zejména pokud je [velikost bloku](support_skip_zag_per_mm.md) nastavena na velmi malou hodnotu. V důsledku toho je riziko pádu podpěry o něco vyšší, což má za následek spoustu strun a špatných převisů.

Toto nastavení také zabraňuje vytažení veškeré podpěry z jednoho kusu. Pokud existuje mnoho kusů podpěry, musí být vyjmuty jednotlivě. Pokud se podpěra uvolní dostatečně snadno, může toto nastavení ve skutečnosti způsobit větší pracnost při odstraňování podpěry (i když to může být snazší).

Toto nastavení nelze dobře kombinovat s parametrem [Počet linií podpěry](../support/support_wall_count.md). Pokud má podpěra kolem sebe další stěnu, tato stěna znovu spojí všechny kusy, což znesnadňuje jejich rozlomení.