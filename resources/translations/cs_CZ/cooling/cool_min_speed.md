Minimální rychlost
====
Pokud tisk vrstvy zabírá velmi málo času, rychlost tisku se sníží, takže vrstva bude stále k tisku potřebovat [minimální čas vrstvy](cool_min_layer_time.md). Nebude však snížena pod tuto minimální rychlost. Pokud tisk vrstvy minimální rychlostí trvá kratší dobu, než je minimální čas vrstvy, tiskárna počká na konci vrstvy, dokud neuplyne minimální čas vrstvy.

Je důležité respektovat minimální dobu vrstvy, aby předchozí vrstva mohla ztuhnout, než položí na vrch další vrstvul. Snížení rychlosti tisku je užitečné, protože ventilátory tiskové hlavy mohou na vlákno déle foukat. Na druhé straně je nadměrné snížení rychlosti tisku škodlivé, protože teplo trysky se může šířit do spodních vrstev a na sousední stěny. To může způsobit, že povrch bude velmi špinavý a způsobí místní ochabnutí. Proto existuje také minimální rychlost. Na konci vrstvy se tisková hlava normálně pohybuje trochu nahoru (pokud není deaktivován parametr [Zvednout hlavu](cool_lift_head.md)), který umožňuje ventilátoru foukat na vlákno o něco déle, dokud neuplyne minimální doba vrstvy. Tiskárna poté přejde na další vrstvu.

![Jaká rychlost ventilátoru se používá, a kde](../images/cool_fan_speed_cs.svg)

Například velmi malá část může mít vrstvu, která trvá 3 sekundy, než se vytiskne normální rychlostí 30 mm/s, ale nastavení minimální doby vrstvy je fixováno na 10 sekund. Tiskárna by pak snížila rychlost na 9 mm/s. Pokud je však minimální rychlost nastavena na 10 mm/s, tiskárna tuto vrstvu vytiskne rychlostí 10 mm/s a dokončí se po 9 sekundách. Tiskárna pak počká 1 sekundu na konci vrstvy, než začne další vrstvu.
