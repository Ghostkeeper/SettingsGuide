Vždy zapsat aktivní nástroj
====
Toto nastavení udává, jak tiskárna interpretuje určité příkazy g-kódu s parametrem nástroje. Některé příkazy g-kódu mohou zahrnovat parametr, který označuje, na který extrudér se vztahuje. Některý firmware interpretuje tento parametr jako příkaz k přepnutí na tento nástroj a poté spouští g-kód, zatímco jiný firmware interpretuje tento parametr jako příkaz, aby aplikoval g-kód na jiný extrudér, než je ten, který je aktuálně aktivní.

Jediné příkazy, které se vztahují na 3D tisk, jsou příkazy ohřevu trysek, `M104` a `M109`. Vezměte následující příklad příkazu ohřevu, prováděného během tisku prvního extrudéru (`T0`):

`M104 S210 T1`

Tento příkaz lze interpretovat dvěma způsoby:
* Zatímco pokračujete v tisku prvním extrudérem, začněte zahřívat druhý extrudér na 210 °C. Toto je interpretace Marlin, Reprap, Sailfish a jejich odvozených firmwarových balíčků.
* Nejprve přepněte na druhý extrudér, poté zahřejte druhý extrudér na 210 °C. Toto je interpretace společnosti Smoothieware a jeho odvozeného firmwaru.

Vzhledem ke strategii regulace teploty Cury, nemusí nikdy provádět druhou interpretaci. Pokud tiskárna interpretuje příkaz g-kódu druhým způsobem, Cura místo toho zapíše následující g-kód:

`M104 S210 T1`

`T0`

V podstatě ví, že tiskárna se přepne na druhý extrudér kvůli tomuto příkazu, a proto musí přepnout zpět na první extruder, aby tam pokračovala v tisku.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**