Vyčistit neaktivní trysku na aktivační věži
====
Pokud je tato funkce aktivována, tiskárna po spuštění další trysky otře na aktivační věži předchozí trysku.

Pokud je toto povoleno, bude pořadí událostí následující:
1. Tiskárna přepne na nový extruder.
2. Nový extruder je připraven tiskem aktivační věže.
3. Tryska, která byla aktivní před přepnutím extruderu, je otřena o aktivační věž.
4. Tiskárna pokračuje v tisku součásti pomocí nového extruderu.

To způsobí, že tiskárna otře trysku, která byla aktivní před přepnutím extruderu, nikoli právě aktivní trysku. Pokud má vaše tiskárna více trysek s určitou vzdáleností mezi nimi, můžete vidět pohyb dráhy v pohledu vrstev, který se jeví jako zbytečný. Je to proto, že pohyb do tohoto místa způsobí, že předchozí tryska se bude pohybovat po aktivační věži (což není v pohledu vrstvy zobrazeno).

Když je tryska přepnuta do pohotovostního režimu, zůstane na chvíli dostatečně teplá. Pokud je horká, mají některé materiály sklon k vytékání. Při aktivaci další trysky v aktivační věži bude mít šanci se trochu ochladit, což výtok zpomalí. Toto nastavení umožňuje setřít výtok uprostřed aktivační věže, aby nekončil na straně tištěného modelu.