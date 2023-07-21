Supportstructuur in Stukken Breken
====
Als het zigzag [Patroon Pupportstructuur](../support/support_pattern.md) wordt gebruikt voor de support, kan de support eenvoudig worden verfrommeld om deze te verwijderen. Dit wordt moeilijker wanneer het draagvlak erg breed is. Deze instelling breekt de zigzagsupport in stukken die gemakkelijker één voor één uit elkaar kunnen worden gehaald, maar die nog steeds breed genoeg zijn om hun stabiliteit te behouden.

<!--screenshot {
"image_path": "support_skip_some_zags.png",
"modellen": [{"script": "rack.scad"}],
"camerapositie": [0, 184, 10],
"instellingen": {
    "support_enable": waar,
    "support_pattern": "zigzag",
    "support_skip_some_zags": waar,
    "support_skip_zag_per_mm": 20
},
"kleuren": 32
}-->
![Elke 8 regels wordt een verbindingslijn weggelaten, waardoor de support in stukken wordt gebroken.](../../../articles/images/support_skip_some_zags.png)

Door de support in stukken te breken, is het gemakkelijker om de support af te breken, omdat u de support stuk voor stuk kunt afbreken. Dit vermindert echter de sterkte en stijfheid van de support enigszins, vooral als de [Grootte Supportstuk](support_skip_zag_per_mm.md) erg klein is ingesteld. Als gevolg hiervan is er een iets grotere kans op kantelen van de support, wat leidt tot stringing en slechte overhangen.

Deze instelling voorkomt ook dat de hele support in één stuk wordt losgetrokken. Als er veel supporten zijn, moeten deze afzonderlijk worden verwijderd. Als de support anders gemakkelijk genoeg is om los te trekken, kan deze instelling het zelfs moeilijker maken (hoewel het nog steeds gemakkelijker kan zijn) om de support uit te trekken.

Deze instelling gaat slecht samen met het [Aantal wandlijnen supportstructuur](../support/support_wall_count.md). Als de support een extra wand om zich heen heeft, verbindt die wand de stukken opnieuw, waardoor het moeilijker wordt om stukken af te breken.