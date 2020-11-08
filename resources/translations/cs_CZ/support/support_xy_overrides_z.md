Priorita vzdálenosti podpěry
====
[Vzdálenost X/Y](support_xy_distance.md) a [vzdálenost Z](support_z_distance.md) podpěry musí být přesně dodrženy; nic víc, nic méně. Tato metoda je příliš restriktivní, takže mezi nimi musí existovat preference. Toto nastavení určuje tuto preferenci.

X/Y má přednost před Z
----
![X/Y má přednost před Z](../images/support_xy_overrides_z_cs.svg)

Pokud má vzdálenost X/Y přednost před vzdáleností Z, pak je vzdálenost X/Y vždy udržována konstantní, i když to znamená, že vzdálenost Z je větší než požadovaná. Vzdálenost Z je vždy udržována jako minimální vzdálenost, takže pokud je přesah velmi vodorovný, platí vzdálenost Z vždy, takže vzdálenost X/Y je větší, než je požadováno.

Z má přednost před X/Y
----
![Z má přednost před X/Y](../images/support_z_overrides_xy_cs.svg)

Pokud má vzdálenost Z přednost před vzdáleností X/Y, pak je vzdálenost Z vždy udržována konstantní, i když to znamená, že vzdálenost X/Y je menší, než je požadováno. Vzdálenost X/Y má vliv na tisk pouze v místech, kde vzdálenost Z nepřichází do hry, tedy ne na vrcholu nosných konstrukcí, ale pouze na bočních stranách.

Minimální vzdálenost X/Y je však vždy dodržována. Pokud je přesah velmi vertikální, vzdálenost X/Y by byla tak malá, že by se podpěra mohla spojit se stranami modelu. [Minimální X/Y vzdálenost podpěry](support_xy_distance_overhang.md) tomu zabrání.