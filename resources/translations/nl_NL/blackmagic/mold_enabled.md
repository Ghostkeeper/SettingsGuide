Matrijs
====
Met deze functie maakt de printer, in plaats van het model zelf te printen, een negatief van het model, een matrijs waarin u een ander materiaal kunt gieten om uw model te maken. Deze matrijs heeft een aantal specifieke eigenschappen die hem geschikt maken voor zowel gieten als printen met de FFF printer. Dit maakt het proces van [Rapid Casting](https://en.wikipedia.org/wiki/Rapid_casting) mogelijk.

<!--screenshot {
"image_path": "mold_enabled_shell.png",
"modellen": [{"script": "stature.scad"}],
"camerapositie": [-78, 160, 228],
"laag": -1
}-->
<!--screenshot {
"image_path": "mold_enabled_mould.png",
"modellen": [{"script": "stature.scad"}],
"camerapositie": [-78, 160, 228],
"instellingen": {
    "mold_enabled": "Waar"
},
"kleuren": 32
}-->
![Een model dat je wilt casten](../../../articles/images/mold_enabled_shell.png)
![De Matrijs voor dit model](../../../articles/images/mold_enabled_mould.png)

Cura's vormgeneratie creëert een holle body met de exacte vorm die u wilt gieten. Rond deze holte wordt een matrijs gemaakt met een specifieke breedte, die configureerbaar is via de instelling [Minimale matrijsbreedte](mold_width.md). Boven en onder de matrijs wordt een laag gemaakt met een specifieke hoogte, die kan worden ingesteld met de instelling [Dakhoogte matrijs](mold_roof_height.md). Om het gietmateriaal in te kunnen vullen wordt deze laag niet bovenop het model gemaakt. Het wordt ook niet onderaan het model gemaakt. Het is bedoeld om op de platvorm te blijven terwijl het model wordt gegoten.

Ontwerp uw matrijs
----
Vormcreatie in Cura is niet perfect. Er ontbreken een paar dingen. Hier zijn enkele tips om ze te repareren.
* Cura maakt geen sprues voor alle lokale pieken in uw model. Overal waar u een spruw nodig heeft, moet u verticale takken aan uw model toevoegen.
* Cura ondersupportt het gieten van extra materiaal niet als uw materiaal krimpt als het afkoelt. Als je materiaal gebruikt dat veel krimpt, moet je zelfs op het hoogste punt van je model extra gietbomen toevoegen.
* De vorm van Cura bestaat altijd uit één stuk. Voor veel vormen betekent dit dat de vorm wordt vernietigd om deze te verwijderen. Vormen kunnen op een aantal manieren worden vernietigd: door pure kracht, of door het te verwarmen als het materiaal binnenin dit toelaat, of door een materiaal te gebruiken zoals PVA dat oplost in water.
* Cura ondersupportt niet het inbrengen van staven of draden om de vorm te versterken. Om dit mogelijk te maken, plaatst u extra staven in uw model zodat Cura holtes voor hen achterlaat, en plaats daarna de staaf of draad.
* Leegtes in uw matrijs worden zonder voorafgaande kennisgeving gemaakt. Als je gietstuk veel holtes vereist, heb je lopers of andere kanalen nodig om het materiaal goed naar binnen te laten stromen en de lucht eruit te laten komen. Houd er ook rekening mee dat uw matrijs mogelijk moet worden vernietigd om de matrijs eruit te krijgen zodra deze is gestold.

Materialen om de matrijs te printen
----
De ideale vorm is:
* heel stijf
* bestand tegen hoge temperaturen
* chemisch inert zodat het niet hecht aan het gietmateriaal
* gemaakt van een materiaal dat niet krimpt

Ook moeten sommige vormen worden vernietigd om het model eruit te krijgen. Hiervoor kun je een bros materiaal kiezen of een materiaal dat kan worden opgelost met water of andere chemicaliën, zoals PVA.

Materialen om te gieten
----
Er zijn veel verschillende soorten materialen waaruit een matrijs kan worden gegoten. Sommige zijn meer compatibel met 3D-geprinte matrijsen dan andere. Hier zijn enkele voorbeelden van materialen die geschikt zijn:
* **Siliconen**. Siliconen hecht niet aan kunststoffen, dus makkelijk te verwijderen. Bovendien is siliconen zeer flexibel, waardoor het geschikt is voor ondersnijdingen. Daarnaast zijn siliconen thermohardend en hittebestendig, waardoor je de matrijs ook na het uitharden eenvoudig kunt verwijderen. Het gieten van siliconen vereist echter speciaal gereedschap. Bovenal heb je een vacuümkamer nodig om de luchtbellen uit de siliconen te krijgen.
* **Zand**. Zand is een industriestandaard voor het maken van een negatief, omdat het zeer hittebestendig is, maar niet verwarmd hoeft te worden om te worden gegoten. Na het gieten kun je het vastbinden met beton of lijm om te voorkomen dat het uit elkaar valt. Je kunt het dan gebruiken om nog een negatief te maken van een meer hittebestendig materiaal.
* **stucwerk**. Vergelijkbaar met zand, maar over het algemeen gemaakt van een fijnere korrel. Dit heeft als voordeel dat de binding al in het materiaal is verwerkt, zodat deze niet opnieuw hoeft te worden ingebonden. Het eindresultaat kan echter brozer zijn.
* **Was**. U kunt een model in was gieten om individuele kaarsen of beeldjes te maken. Wax heeft een lage smelttemperatuur waardoor de matrijs niet zal smelten. Bovendien hecht het niet aan kunststoffen, waardoor het makkelijker uit de vorm te halen is. Wax is zeer kneedbaar en gemakkelijk te veranderen zodra het uit de matrijs is verwijderd. Als je hier een kaars op maat van maakt, vergeet dan niet om een ​​lont toe te voegen voor het uitharden.
* **Chocolade**, als een speciale, individuele traktatie of geschenk. Om chocolade te gieten, smelt het tot net boven het smeltpunt, giet het in de vorm, schud een beetje om de luchtbellen eruit te krijgen en plaats het onmiddellijk in de vriezer. Je kunt de vorm ook in een koudwaterbad in de vriezer plaatsen om de warmte sneller af te voeren. Na vijf minuten kun je de chocolade voorzichtig uit de vorm halen.

FFF-printen kan alleen met thermoplasten. Thermoplasten zijn kunststoffen die van nature zacht worden bij hoge temperaturen. Dit is niet compatibel met gietmaterialen die heet zijn bij het gieten. Sommige materialen die over het algemeen niet compatibel zijn met 3D-geprinte matrijsen:
* **Metalen** die moeten worden verwarmd tot boven het smeltpunt van kunststoffen om vloeibaar genoeg te zijn om te gieten. De hoeveelheid warmte van het metaal zal je matrijs smelten.
* **Kunststof die hecht aan het plastic waarvan de matrijs is gemaakt**. U kunt de matrijs na het gieten niet van het model scheiden. Je kunt wat lossingsmiddel opspuiten, maar als het materiaal te veel op elkaar lijkt, blijft het permanent aan de matrijs plakken.
* **Materialen die te veel krimpen na stollen**. Materialen die krimpen voordat ze stollen, zijn prima, zolang je maar lang genoeg poorten hebt voor nieuw materiaal om de holte te vullen wanneer dit gebeurt.
* **Epoxy** is niet geschikt, want hoewel de hars koud is wanneer deze wordt gegoten, komt er door de chemische reactie van de twee componenten voldoende warmte vrij om het plastic te smelten. Bovendien hecht epoxyhars zeer goed aan kunststoffen.

Als je een object moet maken van een materiaal dat niet direct compatibel is met 3D-printen, moet je in verschillende gietfasen werken. Elke fase creëert een negatief van de vorige fase. U kunt bijvoorbeeld de vorm van uw object normaal printen (met deze instelling uit) en er vervolgens een negatief van maken door de vorm in een stucbad te plaatsen. Omdat stucwerk veel hittebestendiger is, kun je dan materialen gebruiken die heter moeten worden verwarmd om te smelten, zoals: Als brons, of materialen die combineren met kunststoffen zoals. B. Epoxy.

Het gietproces
----
Gieten met een 3D-geprinte matrijs is vrijwel hetzelfde als met elke andere matrijs en is sterk afhankelijk van de gebruikte materialen. Er zijn echter een paar eigenaardigheden om op te letten als het gaat om 3D-geprinte vormen.

De thermoplast waarmee u uw matrijs heeft geprint, heeft een lage warmtecapaciteit en kan een relatief lage glasovergangstemperatuur hebben. Dit betekent dat de tijd na het gieten van de matrijs van cruciaal belang is. Als het materiaal te langzaam afkoelt, kan de matrijs week worden. Hierdoor kan de vorm vervormen en wordt het moeilijker om de vorm los te maken van het resultaat. Om het uitharden van het gietstuk te versnellen, kunt u het bijvoorbeeld onderdompelen in een ijsbad.

3D-geprinte mallen hebben ook meer ribbels langs hun zijkanten vanwege de grenzen tussen de lagen. Deze maken het moeilijker om de mal uit het gips te halen. Als je een lossingsmiddel gebruikt tussen de vorm en het gietstuk, gebruik dan iets dat deze openingen kan opvullen. Dunne smeermiddelen zijn niet genoeg. Meer geschikte tussenlagen zijn was of dikkere smeermiddelen.