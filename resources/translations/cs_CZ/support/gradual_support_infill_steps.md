Postupné kroky výplně podpěry
====
Progresivní podpěra snižuje množství použitého podpůrného materiálu a snižuje hustotu podpěry ve spodních vrstvách. To šetří čas a tiskový materiál, aniž by se výrazně snížila kvalita převisu. Hlavním účelem podpěry je podpírání převislých oblastí. Tato vlastnost umožňuje soustředit podpěru pro tento jediný účel.

Tento parametr udává, v jakých fázích je snížena hustota podpěry. V každé fázi je hustota podpěry snížena na polovinu. Například od hustoty 20% a dvou progresivních fází podpěry bude hustota podpěry dolních částí 10% a 5%.

![Hustota podpěry je snížena na nižší hustotu ve 3 krocích](../../../articles/images/gradual_support_infill_step_height_1mm.png)

Zvýšení počtu kroků vede ke stále výraznějšímu snížení hustotu, což má za následek snížení hustoty podpěry. To šetří spoustu materiálu a tiskového času, ale podpěry jsou slabší.

Část podpěry bude vznášet ve vzduchu. V praxi se to však u většiny podpíraných modelů rychle opraví, protože vrstvy se mohou správně vybudovat i na oslabených spodních vrstvách. Cílem parametru [Výška kroku postupné výplně podpěry](gradual_support_infill_step_height.md) je poskytnout vrstvám dostatek času k opravě před tím, než bude další krok postupné podpěry naskládán na vrchol..

Tento parametr musí být kombinován s alespoň jedním [Počet linií stěny podpěry](support_wall_count.md). To dává liniím podpěry něco, na co se bude moci pověsit, než aby visely ve vzduchu.
