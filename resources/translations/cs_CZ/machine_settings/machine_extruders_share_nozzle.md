Extrudéry sdílí trysku
====
Tímto nastavením můžete označit, že tiskárna má pouze jednu trysku a všechna vlákna jsou protlačována stejnou tryskou. Cura pak změní strategii plnění.

Normálně Cura předpokládá, že po spuštění příkazu [Začátek g-kódu](machine_start_gcode.md) mají všechny extrudery filament na špičce trysky a jsou připraveny k tisku. Pokud extrudery sdílejí jednu trysku, není to možné, protože uvnitř trysky může být v daném okamžiku pouze jeden filament. Namísto běžného postupu plnění pomocí [zaváděcí kapky](../platform_adhesion/prime_blob_enable.md) nebo dodatečných linií sukénky je třeba trysku naplnit jako při plném přepnutí extrudéru. To zahrnuje tisk v [aktivační věži](../dual/prime_tower_enable.md), je-li povolena.

Pokud všechny extrudery sdílejí jednu trysku, je logické, že také [sdílejí ohřev](machine_extruders_share_heater.md).  Cura však mezi nimi sama o sobě nevytváří žádnou vazbu, takže pokud má vaše tiskárna skutečně jednu trysku a jeden ohřev pro všechny extrudery, nezapomeňte povolit obojí.

**Protože se jedná o nastavení stroje, není obvykle uvedeno v běžném seznamu nastavení. V dialogu nastavení tiskárny, který najdete v seznamu přidaných tiskáren v dialogu předvoleb, je však pro toto nastavení k dispozici zaškrtávací políčko.**