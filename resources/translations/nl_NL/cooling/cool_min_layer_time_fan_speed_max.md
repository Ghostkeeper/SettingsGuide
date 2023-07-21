Drempelwaarde Normale/Maximale Ventilatorsnelheid
====
Deze instelling specificeert de printtijd van de laag waar deze zo kort is dat de ventilatorsnelheid toeneemt in de richting van [Maximale Ventilatorsnelheid](cool_fan_speed_max.md). Voor lagen die langer nodig hebben om te printen, wordt de [Normale Ventilatorsnelheid](cool_fan_speed_min.md) gebruikt. Voor lagen die een kortere printduur hebben, wordt de ventilatorsnelheid geïnterpoleerd tussen de normale en maximale ventilatorsnelheid, tot [Minimale Laagtijd](cool_min_layer_time.md), waarbij de ventilatorsnelheid de maximale ventilatorsnelheid bereikt.

![Welke ventilatorsnelheid wordt waar gebruikt](../../../articles/images/cool_fan_speed.svg)

Door deze drempel te verlagen (naar kortere lagen) zal de ventilator vaker draaien met het normale toerental van de ventilator. Door deze drempel te verhogen zal de ventilator vaker op hogere snelheden draaien, ook al zijn de verschuivingen niet erg klein.

Het is raadzaam om een bepaalde afstand aan te houden tussen de minimale laagtijd en de drempel voor de normale/maximale ventilatorsnelheid. Als de drempel is ingesteld op de minimale laagtijd, stopt de ventilator abrupt als de verschuiving iets onder de drempel komt. Dit resulteert in zichtbare strepen op het oppervlak van de print omdat er een harde grens wordt gecreëerd waar de ventilator plotseling stopt. Als er in plaats daarvan een verschil is tussen de twee instellingen, zal de verandering van de ventilatorsnelheid geleidelijker zijn en zullen de strepen niet zichtbaar zijn in de print.