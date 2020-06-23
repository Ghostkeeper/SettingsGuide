Firmwarová retrakce
====
Normálně způsobuje Cura retrakci tím, že řídí pohyb podavače a přikazuje mu, aby posunul vlákno trochu zpět. Pokud je toto nastavení povoleno, bude místo toho psát příkaz `G10`, což znamená, že tiskárna musí retrahovat vlákno nebo příkaz `G11`, aby se extrudovalo.

Výběrem možnosti použití firmwarové retrakce řídí firmware tiskárny, jak daleko a jak rychle se vlákno retrahuje. Tiskárna může vědět více o své vlastní geometrii než Cura, takže se bude moci lépe rozhodnout, jak vlákno retrahovat. To však znamená, že Cura již tyto retrakce neovládá a Cura ví více o samotném tisku. V zásadě mají slicer a firmware různé informace a toto nastavení rozhoduje, které z těchto dvou si vybere.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**