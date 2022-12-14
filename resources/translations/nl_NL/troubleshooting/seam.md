Naden
====
De wanden van je print worden als doorlopende lussen geprint, maar de printer moet die lus ergens beginnen en goed afsluiten. Als de lus niet goed gesloten is, zal er een zichtbare naad zijn. Deze steken zijn moeilijk volledig te verwijderen, maar er zijn dingen die u kunt doen om ze te verbergen of kleiner te maken.

![Een lange verticale naad aan de oppervlakte](../../../articles/images/seam.jpg)

Dit moet niet worden verward met een "Z-naad", een naad die wordt gevormd als nozzle naar het niveau van de volgende laag beweegt. Deze beweging stopt nozzle voor een kort moment en creëert daar een [Klodders](blobs.md). Cura's terminologie over naadinstellingen is in dit opzicht historisch onjuist, aangezien de zogenaamde "Z-naad" -instellingen eigenlijk gaan over waar de normale naad zou moeten worden geplaatst.

Plaatsing van de naden
----
Naden zijn moeilijk te voorkomen, maar het is vaak vrij eenvoudig om de naad te verbergen op een plek waar deze niet zo zichtbaar is.

De belangrijkste instelling voor de plaatsing van de naad is de [Uitlijning Z-naad](../shell/z_seam_type.md). Om de naad te verbergen, plaatst u deze in de scherpste hoek. U kunt dan de instelling [Voorkeur van naad en hoek](../shell/z_seam_corner.md) gebruiken om te kiezen welk type hoek u wilt selecteren. Om de naad te verbergen, kiest u bij voorkeur voor "Verberg naad" of "Smart hide", waardoor de naad in een binnenhoek wordt geplaatst. Als uw model geen binnenhoeken heeft om te verbergen, kunt u Reveal Seam kiezen om de naad op een scherpe buitenhoek te plaatsen waar deze ook minder zichtbaar is dan op een verder vlak oppervlak.

Als de automatische plaatsing niet goed werkt, kunt u de naad ook zelf plaatsen door te kiezen voor "Aangepast". In dit geval kunt u de coördinaten [Z-naad X](../shell/z_seam_x.md) en [Z-naad Y](../shell/z_seam_y.md) invoeren waarop de naad moet worden uitgelijnd. Kies een plek waar de naad niet zichtbaar is.

Als al het andere niet lukt, kun je de naad ook over het hele gebied spreiden door "Willekeurig" te kiezen. In plaats van een doorlopende naad die over het onderdeel loopt, wordt de naad op willekeurige plaatsen over het oppervlak geplaatst. Het oppervlak zal wat pokdalig zijn, maar er is geen echte naad meer.

De naad sluiten
----
De naad kan ook minder zichtbaar worden gemaakt door de naad zorgvuldiger te sluiten bij het maken ervan. Er zijn enkele instellingen die de zichtbaarheid van de naad kunnen verminderen.
* Vergroot de Veegafstand buitenwand](../shell/wall_0_wipe_dist.md) iets. Deze instelling zorgt ervoor dat nozzle nog even rond de contour blijft bewegen nadat het een lus heeft voltooid. Dit voorkomt dat er een opening ontstaat wanneer de contour wordt gesloten. Als u deze instelling echter te veel verhoogt, kan dit ertoe leiden dat er te veel materiaal rond de naad wordt aangebracht, waardoor deze weer zichtbaar wordt.
* Het tegenovergestelde hiervan is het gebruik van [Coasting Inschakelen](../experimental/coasting_enable.md). Dit stopt het extruderen van materiaal net voordat de contour sluit. Dit vermindert de druk in nozzle. De gedachte hierachter is om niet te veel te extruderen wanneer de contour compleet is, waardoor het naar buiten uitsteken van de naad wordt verminderd. Zodra nozzle over het begin van de contour beweegt, heeft het eerder geïntroduceerde plastic de neiging om nieuw plastic te blokkeren, omdat de druk in nozzle niet in staat is om de tegendruk van de gestolde wandlijn te overwinnen.
* Print de buitenwand [Snelheid Buitenwand(langzamer)](../speed/speed_wall_0.md). Het materiaal kan dan beter uitvloeien om de naad aan het uiteinde te sluiten.