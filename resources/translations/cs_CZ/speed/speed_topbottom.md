Rychlost horní/dolní strany
====
Rychlost tisku horní a spodní strany modelu lze konfigurovat odděleně od běžné rychlosti tisku.

![Různé struktury tištěné různými rychlostmi](../../../articles/images/speed_difference.png)

Obecně platí, že pokud má model přesah, měl by být vytištěn relativně pomalu. V opačném případě může rychlý tisk ušetřit spoustu času. Pomalý tisk horní a dolní plochy modelu bude mít následující efekty:
* Prodlužuje dobu tisku, někdy drasticky. Protože horní a dolní strana mají dlouhé linie, rychlost má největší vliv na dobu tisku, nikoli na zrychlení a ryv (jerk). Horní a dolní část může představovat významnou část celkové doby tisku.
* Zlepšuje kvalitu převisu, pokud je převis velmi plochý. Převis, který je stále velmi nakloněný, není příliš ovlivněn, protože plášť tohoto převisu není v tuto chvíli vystaven. Pomalým tiskem přesahu je udržováno napětí na vláknech, což jim umožňuje se déle chladit.
* Podobně jako převis zlepšuje kvalitu horní plochy. Stejný efekt převisu je aplikován na způsob, jakým horní povrch spočívá na výplni.
* Tiskárna obecně méně vibruje. Pokud tisková podložka méně vibruje, bude horní a dolní část vypadat lépe.

**Toto nastavení nemá významný vliv na přilnavost podložky tisku. [Rychlost tisku počáteční vrstvy](speed_print_layer_0.md) se používá pro první vrstvy.**
