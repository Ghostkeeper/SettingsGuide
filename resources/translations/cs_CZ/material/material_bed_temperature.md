Teplota tiskové podložky
====
Některé tiskárny mají vyhřívanou podložku tisku. Toto nastavení určuje teplotu tiskové podložky.

Zahříváním podložky tisku zůstane materiál mírně tekutý a lepivý. Některé materiály tvoří během zmrazování krystaly, což má za následek významné smrštění materiálu při zmrazování. Topné lože udržuje materiál těsně nad teplotou mrazu, aby se zabránilo smrštění. Účelem toho všeho je zlepšit přilnavost tisku k tiskové podložce.

Pokud je však tisková podložka příliš horká, bude tisk velmi tekutý, když se dotkne podložky tisku. Materiál se pak trochu propadne a způsobí sloní nohu na spodní straně tisků. Tento jev lze kompenzovat parametrem [Horizontální rozšíření počáteční vrstvy](../shell/xy_offset_layer_0.md), ale ovlivňuje to rozměrovou přesnost.

Pokud je tento parametr nastaven na 0 stupňů, Cura nevydá žádný příkaz ke změně teploty podložky tisku, což by mohlo zmást firmware, pokud podložka tisku neexistuje.

**Když nastavíte teplotu podložky tisku v materiálovém profilu, upraví se nastavení parametru [Výchozí teplota tiskové podložky](default_material_bed_temperature.md). Normálně bude teplota podložky tisku stejná jako výchozí teplota podložky tisku, ale někdy volba jiné kvality tisku může mít za následek mírné přizpůsobení teploty podložky tisku. Toto nastavení teploty podložky tisku je takové, jaké se skutečně používá pro tisk.**
