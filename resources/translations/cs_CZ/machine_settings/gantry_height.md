Výška portálu
====
Toto nastavení měří vzdálenost mezi tiskovou plochou a portálovým systémem, na kterém je zavěšena tisková hlava. Tato výška je strop, když tisknete [jeden objekt po druhém](../blackmagic/print_sequence.md), protože dříve vytištěný objekt se může srazit s portálem.

![Rozměry tiskové hlavy](../images/head_dimensions_cs.svg)

Většina 3D tiskáren má tiskovou hlavu zavěšenou na příčce nebo na dvou. Tvar tohoto portálu Cura nemodeluje: ať už se jedná o dva příčné nosníky, jediné rameno přicházející z jednoho směru nebo jediný příčník, podél kterého se tisková hlava může pohybovat v jednom směru. Cura vidí tento portál jako pevný strop, když tisknete jeden po druhém, bez ohledu na to, v jakém pořadí jsou modely vytištěny. Když se tiskne jeden po druhém, výška objemu tisku se sníží na tuto výšku portálu, což znamená, že žádné modely vyšší než výška portálu nejsou povoleny.

Jedinou výjimkou je, když je na podložce tisku načten pouze jeden objekt. Tento objekt smí být vyšší než výška portálu, protože na podložce tisku nebude nic jiného, co by se s ním mohlo srazit.

**Protože se jedná o nastavení stroje, nebude obvykle uvedeno v normálním seznamu nastavení. Výšku portálu lze změnit v dialogu nastavení tiskárny, který najdete v seznamu přidaných tiskáren v dialogu předvoleb.**