Minimální obvod mnohoúhelníku
====
Cura normálně odstraňuje detaily modelu, které jsou menší než to, co může tryska vytisknout. Pomocí tohoto nastavení můžete upravit tuto prahovou hodnotu a odstranit tak více či méně podrobností. Tento parametr měří obvod každého tvaru na každé vrstvě a pokud je menší než hodnota tohoto parametru, nebude tento tvar vytištěn.

Je vhodné odstranit podrobnosti, jejichž šířka je menší než jedna linie. To mírně urychluje slicování. Toto však nefunguje vždy s částmi menšími než je hodnota parametru [Šířka linie vnější stěny](../resolution/wall_line_width_0.md), když je funkce [Tisk tenkých stěn](../shell/fill_outline_gaps.md) aktivní. Pokud se stále potřebujete pokusit o velmi malé kousky, můžete toto nastavení zmenšit.

Zvýšení tohoto nastavení může také pomoci odstranit malé detaily a získat rychlejší tisk. Pokud není nutné tyto malé detaily tisknout, je možné ušetřit několik přesunů k jejich dosažení.