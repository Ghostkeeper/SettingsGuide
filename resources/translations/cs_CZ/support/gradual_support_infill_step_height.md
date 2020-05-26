Výška kroku postupné výplně podpěry
====
Při použití postupné podpěry je hustota podpěry pravidelně snižována shora dolů v několika krocích. V každé fázi je hustota podpěry na polovině. Tento parametr označuje výšku těchto kroků, vzdálenost mezi dvěma místy, kde je hustota podpěry dělena dvěma.

![Výška kroku 1 mm](../../../articles/images/gradual_support_infill_step_height_1mm.png)
![Výška kroku 3 mm](../../../articles/images/gradual_support_infill_step_height_3mm.png)

Progresivní podpěra ze své podstaty postaví část podpěry ve vzduchu. To se však normálně automaticky opravuje. První vrstva podpěry bude zavěšena ve vzduchu a připojí se správně pouze k stranám podpěry. Vrstvy nahoře mohou spočívat na předchozí vrstvě trochu na koncích, ale budou uprostřed klesat. To se postupně zlepšuje, vrstvu po vrstvě. Pokud je výška kroku postupné podpěry dostatečně velká, je podpěra v době, kdy nastane další krok hustoty, dostatečně robustní.

Snižte výšku kroku postupné podpěry, abyste mohli rychle sestoupit k slabému podpůrnému hustotu. To šetří čas tisku a spotřebu materiálu. Zvyšte výšku kroku postupné výplně podpěry, pokud podpěra nemá dostatek místa k opravě do doby, než dojde k další fázi hustoty podpěry. Zvýšení hodnoty tohoto parametru zvyšuje spolehlivost tisku.
