Hustota výplně
====
Toto nastavení konfiguruje hustotu objemu uvnitř tisku, což je hlavní faktor v síle finálního tisku a v kvalitě vrchního povrchu. Čím vyšší je hustota výplně, tím blíže budou linie výplně od sebe vzdáleny. Můžete dokonce překročit hustotu o 100%, ale to způsobí nadměrné vytlačování.

![Hustota 20%](../../../articles/images/infill_sparse_density_high.png)
![Hustota 10%](../../../articles/images/infill_sparse_density_low.png)

Různé hustoty fungují nejlépe s různými vzory výplně. Výplňové vzory se spoustou rohů a křížení nebudou s velkou hustotou výplně dobře fungovat. Rohy jsou problém, protože vlákno má sklon táhnout se spolu s rohem a vytvářet vnější kapsy na vnější straně rohu, kde měl být materiál uložen. Křižování jsou ještě větším problémem, protože když jedna linie křižuje druhou, její tok je přerušen, což způsobuje pod-extruzi hned po křížení.

Zvýšení hustoty výplně (zmenšením vzdálenosti mezi liniemi) má důležitý vliv na váš tisk, a to:
* Váš tisk bude silnější.
* Horní povrch bude lépe podepřen, díky čemuž bude hladší a voděodolnější.
* Snížení polštářování, protože tepelné kapsy budou menší.
* Váš tisk bude vyžadovat více materiálu, a proto bude těžší.
* Tisk trvá déle.
