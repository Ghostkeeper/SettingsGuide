Minimální podpíraná plocha
====
Tento parametr stanoví minimální velikost povolenou pro části podpěr. Pokud má část podpěry na určité vrstvě oblast menší než je hodnota tohoto parametru, je tam podpěra vynechána.

![Žádné filtrování plochy (minimální plocha je 0)](../../../articles/images/minimum_support_area_0.png)
![Malé části podpěry jsou vynechány](../../../articles/images/minimum_support_area_10.png)

Důvodem tohoto nastavení je to, že tenké sloupy podpěry se pravděpodobně převrhnou. Mají také tendenci podpírat malé položky, které by se pravděpodobně dobře tiskly bez podpěry. Pokud se podpěra převrhne, zůstane na tisku mnoho kapek. Proto je nejlepší tyto tenké sloupky podpěry vynechat. Toto nastavení filtruje podpěru podle průřezu sloupku.

Zvětšením povrchu se sníží množství tištěného materiálu, což mírně snižuje čas a použití materiálu. Ještě důležitější je, že zvyšuje spolehlivost tisku, protože existuje menší šance na převrácení sloupků podpěry. Odstraní však také podpěru malých prvků vašeho tisku, takže kvalita převisů se u těchto částí může zhoršit.

U některých tvarů to může mít nepříjemný vedlejší účinek při odstraňování střechy podpěry, pokud horní část klesne pod prahovou oblast, ale ne dolní část. To může nechat části nepodpírané, u kterých byste za normálních okolností očekávali, že budou podpírány.

![Špička oblouku není podpírána, protože oblast na těchto vrstvách je příliš malá](../../../articles/images/minimum_support_area_problem.png) 