Minimumbreedte dunne wandlijn
====
Met deze instelling kunnen zeer kleine details worden geprint met een lijndikte die eigenlijk te groot is voor hen. In plaats van hele dunne lijnen te printen, print hij met een redelijke lijndikte.

Als de [Minimum elementgrootte](min_feature_size.md) erg klein is ingesteld, kunnen sommige zeer dunne delen worden geprint. Dat werkt niet goed. Hoewel het mogelijk is om lijnen te printen die kleiner zijn dan de nozzle, niet veel. Printlijnen die te dun zijn, resulteren in inconsistente extrusie.

In plaats daarvan zijn deze zeer dunne lijnen breder gemaakt, zodat ze gelijkmatiger worden geëxtrudeerd. Elk deel van het model dat dunner is dan de minimale wanddikte van de dunne lijn, wordt geprint met een enkele lijn van de minimale wanddikte van de dunne lijn. De lijnen worden dan breder dan de oorspronkelijke breedte van het model. Dit vermindert de maatnauwkeurigheid, maar het print in ieder geval betrouwbaarder.

De waarde van deze instelling moet de dunste lijnbreedte zijn die de printer betrouwbaar kan printen voordat hij ruwe oppervlakken en inconsistente extrusie gaat produceren. Deze waarde ligt meestal tussen de grootte van de nozzle en de helft van de grootte van de nozzle. Een hogere waarde leidt ertoe dat dunne delen te dik worden geprint, maar vermindert het risico op onder-extrusie als gevolg van het proberen om te dunne lijnen te printen.