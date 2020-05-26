Aktivovat zaváděcí kapku
====
Je-li tato funkce povolena, umožňuje Cura odeslat do tiskárny příkaz k plnění, těsně před prvním použitím extrudéru. Tiskárna se zavádí vytvořením malé kapky materiálu na podložce tisku.

Účelem plnění je zajistit, aby materiál správně tekl. Pokud není aktivována úvodní kapka, tiskárna se aktivuje během sukénky nebo krempy. Toto je hlavní případ použití sukénky na prvním místě, ale u krempy to mírně sníží přilnavost okraje.

Účinek tohoto nastavení na g-kód je v tom, že Cura umístí příkaz M280 na určité místo. **To v současné době funguje pouze na tiskárnách Ultimaker od Ultimaker 3**, protože jsou jedinými, kdo implementují příkaz M280. U ostatních tiskáren nebude toto nastavení viditelné.
