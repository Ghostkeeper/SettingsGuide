Strunování
====
Jakmile tiskárna dokončí tisk části vrstvy a potřebuje přepnout na jinou část, měla by dočasně zastavit vytlačování. Když materiál i nadále vytéká, při přesunu, je mezi oběma částmi tažena tenká plastová struna. Tomu se říká strunování.

![Tenké linie plastu jsou vidět tam, kde se tryska přesunula z jedné části do druhé](../../../articles/images/stringing.jpg)

Struny jsou často vyrovnány navzájem na sobě, protože tryska dokončí díl v každé vrstvě na stejném místě. Tím se vytvoří svislý proužek. Na strunách předchozích vrstev se také může hromadit další plast, takže všude jsou plastové kuličky.

Strunování je někdy doprovázeno podextruzí. Slicer obecně předpokládá, že se během přesunu neztratí žádný materiál, a proto dává tiskárně pokyn, aby vytiskla jen tolik materiálu, aby vytiskla svou další část. Pokud nějaký materiál unikne z trysky během přesunu (což má za následek strunu), nebude tento materiál použit pro tisk další části, což má za následek pod-extruzi. Strunování obvykle není problém, pokud se vyskytuje uvnitř výplně, ale pokud je strunování příliš extrémní, může to být problém i tam, protože to následně vede k pod-extruzi.

Příčiny
----
Ke strunování dochází proto, že materiál během pohybu přesunu vytéká z trysky. Přestože tiskárna během přesunu nepodává nový materiál, tok materiálu se nezastaví okamžitě. Během tisku je uvnitř komory trysek určitý tlak způsobený vláknem, které akumuluje určitou sílu jako pružina. Jak se tryska pohybuje vzduchem, může se tento tlak uvolnit, neúmyslným vytlačením materiálu z trysky.

I když je materiál před pohybem retrahován, uvnitř tryskové komory bude stále materiál. To se děje proto, že materiál v této trysce je roztavený. Tah z jedné strany nezpůsobí reverzaci kapaliny. Pokud neztuhne, zůstává v trysce kapka roztaveného materiálu. Při přesunu tato kapka vyteče z trysky, je-li dostatečně tekutá.

Prevence
----
Retrakce je hlavní technikou, jak se vyhnout strunování. Pokud na vašich tiscích vidíte struny, můžete vyzkoušet několik věcí:
* Ujistěte se, že [je retrakce povolena](../travel/retraction_enable.md). Tisk trvá trochu déle, ale výrazně snižuje počet strun.
* Snižte hodnotu [teploty tisku](../material/material_print_temperature.md). Díky tomu je materiál méně tekutý, což způsobuje menší prosakování z trysky. To také umožňuje účinnější retrakci, protože více materiálu bude vytaženo z tryskové komory.
* Pokud je váš materiál viskózní, zvýšení [rychlosti retrakce](../travel/retraction_speed.md) obecně sníží strunování pro krátké pohyby podtlakem v komoře trysky. Tento snížený tlak udržuje materiál nasávaný, takže nevytéká ven.
* U dlouhých přesunů udržuje zvětšení [vzdálenosti retrakce](../travel/retraction_amount.md) materiál během pohybu chladnější, čímž se snižuje rychlost, kterou se materiál roztavuje a vytéká ven z trysky.
* Cura se někdy snaží zabránit opotřebení vlákna tím, že omezí počet retrakcí po určité délce vlákna. Vzhledem k tomu, že v tuto chvíli zde neexistují žádné retrakce, bude to mít za následek určitý strunování jako nezbytné zlo, než aby došlo k selhání tisku. Pokud váš podavač příliš materiál neobrušuje, můžete zvýšit [počet povolených retrakcí](../travel/retraction_count_max.md) nebo snížit [délku vlákna](../travel/retraction_extrusion_window.md) podle kterého počítají tyto retrakce.
* Pokud povolíte [objíždění](../travel/retraction_combing.md) na více místech, tryska bude procházet spíše uvnitř modelu než vně. Tím se strunování ve skutečnosti nezabrání, ale jeho umístěním uvnitř modelu se stane neviditelným.
* Pokud je [pořadí tisku stěn lépe optimalizováno](../shell/optimize_wall_printing_order.md), bude se tryska méně často pohybovat z jedné části na druhou, což sníží množství strun.
* Zvyšování [rychlosti přesunu](../speed/speed_travel.md) obecně umožňuje ztenčování strun během delších pohybů. U krátkých přesunů to ve skutečnosti nic nezmění, protože limity zrychlení tiskáren stejně brání trysce v dosažení těchto rychlostí.
* Tisk s menší tryskou také normálně sníží počet strun. Pro plasty je snazší vytékat z větší trysky.