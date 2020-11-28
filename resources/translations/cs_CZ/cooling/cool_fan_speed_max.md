Maximální rychlost ventilátoru
====
Rychlost, jakou běží ventilátory tiskové hlavy, když je vrstva vytištěna v minimálním čase. Při minimální době vrstvy budete chtít vrstvu co nejrychleji ochladit, abyste zkrátili dobu potřebnou k vychladnutí vrstvy, než tiskárna umístí  na vrch další vrstvu.

![Jaká rychlost ventilátoru se používá, a kde](../images/cool_fan_speed_cs.svg)

Pokud je tisk vrstvy někde mezi parametry [Práh normální/maximální rychlosti ventilátoru
](cool_min_layer_time_fan_speed_max.md) a [Minimální čas vrstvy](cool_min_layer_time.md), bude rychlost ventilátoru interpolována mezi [normální rychlostí ventilátoru](cool_fan_speed_min.md) a maximální rychlostí ventilátoru. Jakmile je dosaženo minimální doby vrstvy, dosáhne se také maximální rychlosti ventilátoru. Tímto způsobem bude tisk zchlazen na maximum, aby byl co nejrychleji ochlazen, než bude na povrch položena další vrstva.