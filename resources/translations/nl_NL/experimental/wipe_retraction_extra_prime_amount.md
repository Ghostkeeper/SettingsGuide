Extra primehoeveelheid na intrekken voor afvegen
====
Als [Intrekken voor afvegen inschakelen](wipe_retraction_enable.md) is ingeschakeld, wordt het materiaal teruggetrokken nadat het wissen is voltooid. Wanneer dit gebeurt, wilt u misschien dat het filament iets verder wordt geduwd dan de oorspronkelijke [Intrekafstand voor afvegen](wipe_retraction_amount.md) om het verloren filament ondanks het terugtrekken te compenseren. Dit kan apart worden geconfigureerd van de [Extra Primehoeveelheid na intrekken](../travel/retraction_extra_prime_amount.md).

Bij het afvegen beweegt nozzle helemaal naar de zijkant van de printer, beweegt daar heen en weer en trekt zich vervolgens helemaal terug. Dit is in wezen een zeer lange verplaatsbeweging. Aangezien deze verplaatsing langer duurt dan de gemiddelde verplaatsing door de print, kan er meer materiaal verloren zijn gegaan door lekkage. Om dit te compenseren, moet u mogelijk meer materiaal doorvoeren na het afvegen dan na normale verplaatsbewegingen.

Als er te veel extra materiaal wordt doorgevoerd, zal enige over-extrusie optreden. Dit manifesteert zich als een klodder waar de nozzle na het afvegen terecht komt.