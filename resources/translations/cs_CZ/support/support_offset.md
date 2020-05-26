Horizontální rozšíření podpěry
====
Toto nastavení způsobí, že se podpěra mírně rozšíří a vodorovně se rozprostírá ve všech směrech.

![Podpěra je širší, než je nezbytné pro podepření modelu](../../../articles/images/support_offset.png)

Tento nastavení má více použití, v závislosti na materiálu použitém pro podpěru a typu modelu, který je třeba podpírat:
* Zvýšením tohoto parametru se podpěra rozšíří, a proto bude pevnější. To je užitečné pro vysoké modely s malými částmi převisu, protože převis by jinak byl podpírán velmi vysokým a tenkým podpůrným sloupkem. S trochou vodorovného rozšíření se stává velmi vysokým, ale mírně širším pilířem podpěry.
* Zvýšení tohoto parametru je také bezpečnostním opatřením k zajištění toho, aby oblasti podpěry měly určitou minimální plochu. To je nezbytné pro těžko vytlačitelné materiály, jako je PVA.
* Snížením tohoto nastavení se sníží spotřeba materiálu a doba tisku podpěry. Jeho zvýšením samozřejmě zvýšíme potřebný materiál a dobu tisku. Podívejte se také na funkci [kónická podpěra](../experimental/support_conical_enabled.md), která zmenšuje šířku podpěry bez ohrožení povrchu, který podpírá.
* Nastavení tohoto parametru na zápornou hodnotu může také úplně odstranit tenké podpůrné sloupy. Pokud se tato podpěra přesto netiskne, může být lepší podpěru úplně vynechat. Jednou z metod, jak odstranit podpěru, aniž by byla ohrožena kvalita převisu zbytku modelu, je nástroj Blokátor podpěr.
