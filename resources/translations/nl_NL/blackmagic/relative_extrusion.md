Relatieve Extrusie
====
Cura schrijft opdrachten voor de printer om uw object in G-code te printen. Deze commando's verplaatsen de printkop naar specifieke posities en zetten de feeder aan. Normaal slaat Cura zowel de coördinaten voor de beweging van de printkop als de positie van de feed op als absolute coördinaten. Als deze instelling echter is ingeschakeld, worden de inspringcoördinaten relatief vastgelegd.

Als dit is uitgeschakeld (d.w.z. absolute extrusie), wordt de positie van het filament aan het begin van de print vergrendeld als de nulcoördinaat. De positie van het filament neemt door het hele bestand toe naarmate er meer materiaal wordt geëxtrudeerd en het filament steeds verder weg moet bewegen van het startpunt aan het begin van de print.

Als dit echter is geactiveerd, wordt de extrusie afzonderlijk in elke regel G-code geschreven, relatief ten opzichte van de positie van de vorige regel. Elke lijn bevat dan alleen de hoeveelheid materiaal die voor die specifieke lijn is geëxtrudeerd.

Relatieve extrusie maakt het gemakkelijk om de G-code te bewerken nadat deze is gemaakt. Als er ergens tussenin, als extra materiaal moet worden geëxtrudeerd (om lijnsegmenten toe te voegen of te verwijderen, of om nozzle aan te passen), moet de nieuwe extrusie gewoon in het te bewerken onderdeel worden geschreven. Als een absolute extrusie wordt gebruikt, moet de positie van de extruder vervolgens worden gereset met G92 om ervoor te zorgen dat alle volgende opdrachten correct zijn.

Als er echter op enig moment tijdens de verwerking van de G-code (in Cura, de firmware of de beweging) afrondingsfouten zijn, zal de absolute extrusie deze automatisch corrigeren in de volgende regel. Bij relatieve extrusie resulteert dit in over- of onder-extrusie, zij het in zeer geringe mate.

Niet alle printerfirmware ondersupportt relatieve extrusie.

**Als absolute extrusie wordt gebruikt, stelt Cura de filamentpositie elke 10 meter opnieuw in om afrondingsfouten met drijvende komma in de firmware te voorkomen.**