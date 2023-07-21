Primeblob inschakelen
====
Als deze optie is geactiveerd, geeft Cura een opdracht om de printer voor te bereiden net voordat de extruder voor het eerst wordt gebruikt. De printer bereidt zichzelf voor door een kleine klodder materiaal op de platform te maken.

Het doel van de voorbereiding is ervoor te zorgen dat het materiaal goed stroomt. Als de invoerdruppel niet is ingeschakeld, zal de printer in plaats daarvan primen tijdens de brim of skirt. Dit is het belangrijkste gebruik voor de skirt, maar met een brim zal dit de plakkerigheid van de brim enigszins verminderen.

Het effect van deze instelling op de G-code is dat Cura het M280-commando op een specifieke plaats zet. **Dit werkt momenteel alleen op Ultimaker-printers sinds de Ultimaker 3**, omdat zij de enige zijn die de M280-opdracht hebben geïmplementeerd. De instelling is niet zichtbaar op andere printers.