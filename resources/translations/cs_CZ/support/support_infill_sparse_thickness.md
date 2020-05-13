Tloušťka vrstvy výplně podpěry
====
Protože vizuální kvalita a rozlišení média nejsou důležité, můžete pro podpěry použít silnější vrstvy a zkrátit tak dobu tisku. Tento parametr umožňuje nakonfigurovat tloušťku vrstev, se kterými bude podpěra tisknuta.

Ve vrstveném pohledu bude mít člověk dojem, že linie podpěry jsou mnohem širší. Při tisku budou podpůrné linie klesat níže, místo aby se vodorovně roztahovaly.

![Tloušťka vrstvy výplně podpěry je definována na trojnásobek výšky vrstvy](../../../articles/images/support_infill_sparse_thickness.png)

Tloušťka vrstvy výplně podpěry musí být násobkem výšky běžné vrstvy. Pokud tomu tak není, bude zaokrouhlena na nejbližší výšku vrstvy.

Toto nastavení se nevztahuje na střechu nebo podlahu podpěry, ale pouze na hlavní strukturu podpěry.

Toto nastavení je zvláště užitečné, když je podpěra tištěna z jiného materiálu, než zbytek tisku a ještě více, když je tento materiál obtížně vytlačitelný, jako je PVA. Protože médium není extrudováno na každou vrstvu, tiskárna nebude muset extrudéry tak často měnit, což šetří spoustu času. Protože na tištěné vrstvy je vytlačováno více materiálu, budou materiály, které potřebují čas k zahájení toku, vytištěny spolehlivěji.

Dejte pozor, abyste tento tok příliš nezvýšili. Při výměně média by měl být průtok tryskou výrazně zrychlen a zpomalen. V tomto bodě existuje určité zpoždění, takže tok bude na začátku podpěry příliš nízký a po skončení podpěry příliš vysoký.
