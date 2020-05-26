Tloušťka vrstvy výplně
====
Protože výška vrstvy výplně není důležitá pro vizuální kvalitu, můžete pro výplň použít tlustší vrstvy a zkrátit tak dobu tisku. Toto nastavení umožňuje sloučit vrstvy výplně za předpokladu, že je několik vrstev přímo na sebou. Na některé vrstvě nevytiskne žádnou výplň, ale v nejvyšší ze sloučených vrstev vytlačí více materiálu, aby se to kompenzovalo.

V pohledu vrstev budete mít dojem, že linie výplně jsou mnohem širší. Při tisku se linie výplně dále snižují, místo aby se vodorovně rozšiřovaly.

![Tloušťka vrstvy výplně je nastavena na trojnásobek výšky vrstvy](../../../articles/images/infill_sparse_thickness.png)

Tloušťka vrstvy výplně musí být násobkem výšky běžné vrstvy. Pokud tomu tak není, bude zaokrouhlena na nejbližší výšku vrstvy.

* Dávejte pozor, abyste ji příliš nezvyšovali. Při přepínání na vrstvu výplně a naopak musí tok tryskou výrazně zrychlovat a zpomalovat. V tomto bodě je určité zpoždění, takže na začátku výplně dojde k příliš malému vytlačování a po dokončení výplně příliš velkému.
* Ve středních vrstvách se bude vždy tisknout výplň s nižší tloušťkou vrstvy, kde ve vrstvách kolem ní výplň není. To může mít za následek tisk malých linií výplně podél šikmých stěn.
