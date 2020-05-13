Velikost kapes 3D kříže
====
3D křížový [vzor výplně](../infill/infill_pattern.md) byl vytvořen pro usnadnění flexibilních výtisků. Vzor obsahuje čtyřcestné křižovatky, které jsou však velmi rigidní. Toto nastavení způsobí, že se vzor vyhne křížení, aby na některých místech nebyl příliš pružný. To způsobí, že vzor zanechá v křížení vzduchovou kapsu. Toto nastavení určuje velikost kapsy.

![Výchozí velikost kapsy 2 mm](../../../articles/images/infill_pattern_cross_3d.png)
![Velikost kapsy 0,5 mm](../../../articles/images/cross_infill_pocket_size_0_5.png)

Vzor mění vzdálenost kolem čtyřcestného přechodu. Toto nastavení určuje velikost kapsy ve vrstvách, když se linie úplně dotýkají. Maximální velikost kapsy je určena hustotou výplně. Velikost kapsy nebude nakreslena větší než druhá odmocnina dvojnásobku vzdálenosti výplně. Pokud je zadána větší hodnota, nebude to mít žádný účinek, ale větší hodnoty mohou být zadány pro usnadnění větších velikostí kapes v případě [postupné výplně](../infill/gradual_infill_steps.md) nebo [proměnné hustoty výplně](cross_infill_density_image.md).

Zvýšením hodnoty pro toto nastavení je výplň slabší ve svislém směru a lépe se rozprostírá kolem síly, aby se vytvořilo rovnoměrnější rozdělení síly.
