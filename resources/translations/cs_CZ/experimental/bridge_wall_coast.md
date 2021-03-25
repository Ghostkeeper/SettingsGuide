Doběh pro stěnu přemostění
====
Při přemostění liniemi stěn těsně před tiskem mostu se na okamžik zastaví podávání materiálu. Během této doby se zbývající materiál uvnitř tryskové komory nechá vytéct, aby se snížil tlak uvnitř tryskové komory. Tato technika se nazývá [doběh](coasting_enable.md). S tímto nastavením lze regulovat množství dojezdu. V zásadě to řídí, jak daleko před mostem přestane materiál proudit.

Jakmile je most hotový, materiál, který nebyl extrudován, bude stejně vytlačen. Celkové množství vytlačovaného materiálu zůstane stejné. Tím se obnoví tlak na trysku, což zabraňuje podtlaku.

![Žádné vytlačování na jedné straně mostu a další vytlačování na druhé straně](../../../articles/images/bridge_skin_density_100.png)

Jednotka tohoto nastavení nemá být intuitivní. Vzdálenost před mostem, po které se materiál zastaví, závisí na řadě faktorů:
* Délka stěny k mostu. Čím delší je stěna, tím větší může být doběh.
* Rychlost toku trysky během normální stěny, který závisí na [rychlosti](../speed/speed_wall.md), [šířce linií](../resolution/wall_line_width.md), [průtoku](../material/wall_material_flow.md) a [výšce vrstvy](../resolution/layer_height.md) těchto stěn. Čím vyšší je průtok v normálních stěnách, tím delší je vzdálenost dojezdu.
* Rychlost proudění z trysky během stěny přemostění, která závisí na [rychlosti](bridge_wall_speed.md) a [toku](bridge_wall_material_flow.md) těchto stěn. Čím větší je průtok v přemostěných stěnách, tím kratší je vzdálenost dojezdu.

Tento parametr je multiplikátor konečné délky.

Účelem tohoto dojezdu je snížit tlak uvnitř tryskové komory dolů. To je nezbytné, protože jakýkoli zbývající tlak v komoře trysky způsobí, že materiál bude stříkat dolů značnou vzdálenost před ztuhnutím, jakmile protitlak zmizí. Toto stříkání materiálu má za následek ochabnutí. Ve skutečnosti jsou převislé linie tlačeny dolů zbytkem materiálu, který je stále uvnitř trysky. Pokud se tlak uvnitř tryskové komory sníží, bude tato síla také snížena a bude zde menší ochabnutí.

Zvýšení velikosti dojezdu sníží tlak uvnitř komory trysky v době, kdy je třeba tisknout přemostění, což sníží velikost prověšování. Tisk bude přesnější. Přílišné zvýšení velikosti dojezdu povede k období pod-extruze těsně před tiskem přemostění. Protože je tato pod-extruze ve stěnách tisku, bude na straně tisku velmi viditelné.