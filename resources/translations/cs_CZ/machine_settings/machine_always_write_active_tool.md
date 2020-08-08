Vždy zapsat aktivní nástroj
====
Toto nastavení udává, jak tiskárna interpretuje urèité pøíkazy g-kódu s parametrem nástroje. Nìkteré pøíkazy g-kódu mohou zahrnovat parametr, který oznaèuje, na který extrudér se vztahuje. Nìkterý firmware interpretuje tento parametr jako pøíkaz k pøepnutí na tento nástroj a poté spouští g-kód, zatímco jiný firmware interpretuje tento parametr jako pøíkaz, aby aplikoval g-kód na jiný extrudér, než je ten, který je aktuálnì aktivní..

Jediné pøíkazy, které se vztahují na 3D tisk, jsou pøíkazy ohøevu trysek, `M104` a `M109`. Vezmìte následující pøíklad pøíkazu ohøevu, provádìného bìhem tisku prvního extrudéru (`T0`):

`M104 S210 T1`

Tento pøíkaz lze interpretovat dvìma zpùsoby:
* Zatímco pokraèujete v tisku prvním extrudérem, zaènìte zahøívat druhý extrudér na 210 °C. Toto je interpretace Marlin, Reprap, Sailfish a jejich odvozených firmwarových balíèkù.
* Nejprve pøepnìte na druhý extrudér, poté zahøejte druhý extrudér na 210 °C. Toto je interpretace spoleènosti Smoothieware a jeho odvozeného firmwaru.

Vzhledem ke strategii regulace teploty Cury, nemusí nikdy provádìt druhou interpretaci. Pokud tiskárna interpretuje pøíkaz g-kódu druhým zpùsobem, Cura místo toho zapíše následující g-kód:

`M104 S210 T1`

`T0`

V podstatì ví, že tiskárna se pøepne na druhý extrudér kvùli tomuto pøíkazu, a proto musí pøepnout zpìt na první extruder, aby tam pokraèovala v tisku.