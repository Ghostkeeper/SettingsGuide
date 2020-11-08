Počet linií bloku podpěry
====
Pokud je podpěra [rozdělena na bloky](support_skip_some_zags.md), určuje tento parametr, kolik linií podpěry bude spojeno do jednoho bloku.

![Každý blok obsahuje 8 linií](../../../articles/images/support_skip_some_zags.png)

Menší bloky bývá snazší oddělit než větší bloky. Je tu menší plocha povrchu k přilepení k modelu, takže bude potřeba menší síly, aby se podpěra oddělila. Bude však také k více kusů, které se oddělují, takže pokud není normálně obtížné podpěru vyjmout, může to vést k další práci. Každý blok musí být poté stažen jednotlivě, místo toho, aby se veškerá podpěra stáhla v jednom velkém kusu.

Pokud jsou bloky velmi malé, může být narušena strukturální integrita podpěry. Vzor podpěry bude potom vypadat spíš jako přímý vzor, který s větší pravděpodobností poklesne. To by mělo za následek více strun a nižší kvalitu převisu tam, kde podpěra poklesla.