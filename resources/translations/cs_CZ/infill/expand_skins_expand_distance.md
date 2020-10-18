Vzdálenost rozšíření pláště
====
Pevné vrstvy můžete v horní a dolní části tisku rozšířit nebo zúžit. Normálně jsou pevné vrstvy generovány pouze v oblastech, kde je nad nebo pod nimi vzduch, ale s tímto nastavením je můžete vodorovně o něco více rozšířit, což zvyšuje odolnost, takže se plášť lépe lepí na sousední stěny a uzavírá mezery v plášti.

![Normální vzhled pláště (žluté části)](../../../articles/images/expand_skins_expand_distance_original.png)
![Plášť rozšířený o 1 mm](../../../articles/images/expand_skins_expand_distance_1mm.png)

* Pokud máte malé otvory v horní nebo dolní vrstvě tisku (otvory, které jsou vyplněny vzorem výplně), nastavení tohoto parametru o něco výš je uzavře. To umožňuje tiskárně tisknout spodní linie nepřetržitě, což výrazně zvyšuje odolnost.
* Pokud má váš model vodorovnou plochu vedle tuhé stěny, může zvýšení tohoto nastavení zlepšit přilnavost mezi stěnami tuhé plochy a pláštěm, protože plášť bude vytištěn přímo v kontaktu s těmito stěnami.
* Pokud nastavíte tento parametr na zápornou hodnotu, šířka horní a dolní vrstvy se zmenší a nahradí výplní. To může ušetřit čas tisku na úkor pevnosti.

**Z důvodu technických omezení nemůžete toto nastavení snížit pod hodnotu parametru [Šířka odstranění pláště](skin_preshrink.md). Zvyšte nastavení šířky odstranění pláště a odstraňte více pláště.**