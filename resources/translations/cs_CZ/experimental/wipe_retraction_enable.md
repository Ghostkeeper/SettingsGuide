Aktivovat retrakci pro otírání
====
Pokud je tento parametr aktivován, bude materiál během procesu otírání zasunut. Tento parametr lze konfigurovat odděleně od [normálních retrakcí](../travel/retraction_enable.md).

Postup otírání způsobí, že se tryska dostane na stranu tiskárny, pohybuje se tam a zpět a poté se vrátí do své původní polohy. Je to v podstatě velmi dlouhý výlet. Protože je tento pohyb delší než průměrný pohyb během tisku, můžete chtít, aby byl materiál během tohoto postupu retrahován, i když jsou retrakce normálně zakázány.

Pokud je materiál zasunut, sníží se množství materiálu, který během procesu otírání vytéká. Materiál, který během procesu otírání vytéká, bude obvykle kartáčem setřen. Tento materiál je však ztracen. V důsledku toho dojde k určitému podextruzi těsně po dokončení otírání, protože tento materiál vytékal místo toho, aby byl umístěn na své správné místo.

Na druhou stranu, stažení může nějakou dobu trvat a způsobit zbytečné opotřebení vlákna. Pokud pod-extruze není problém, deaktivace retrakce může ušetřit čas a zvýšit spolehlivost. To může fungovat dobře, pokud například [je výplň vytištěna před stěnami](../infill/infill_before_walls.md), protože některé dílčí vytlačování během výplně není opravdu problém.