Maximale varatie adaptieve lagen
====
Met deze instelling kunt u het bereik beperken waaruit de Adaptive Layers een laaghoogte mogen selecteren. De laaghoogte mag niet meer afwijken dan deze variatie van de normale [Laaghoogte](../resolution/layer_height.md).

Met een normale laaghoogte van 0,15 mm en een variatie van 0,1 mm kunnen Adaptive Layers bijvoorbeeld lagen maken met een dikte tussen 0,05 mm en 0,25 mm.

Deze instelling beperkt de prestaties van de functie Match Layers. Als het bereik van de laaghoogte te smal is, zal de laaghoogte altijd heel dicht bij de oorspronkelijke laaghoogte zijn die is ingesteld met de instelling voor de plakhoogte. De Fit Layers-functie doet dan niet veel om tijd te besparen of de kwaliteit te verbeteren.

Als het gebied echter erg groot is, kunnen de lagen erg dik of erg dun worden. Zeer dikke lagen vereisen een hoge uitstroom uit de nozzle, wat niet altijd mogelijk is door de beperkte nozzlegrootte en de smeltcapaciteit van het verwarmingsspoor in de printkop. Ook zijn zeer dunne lagen niet altijd mogelijk door de viscositeit van het materiaal of de onnauwkeurigheid van de Z-as. Daarom is het logisch om het bereik te beperken waarin Adaptive Layers de laaghoogte kunnen aanpassen. Anders heeft de printer moeite om de gewenste laaghoogte te bereiken.

De laaghoogte kan nooit onder de 0,001 mm komen, ook niet als het bereik het toelaat.