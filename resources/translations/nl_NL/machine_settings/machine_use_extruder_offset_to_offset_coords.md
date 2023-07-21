Offset met extruder
====
Deze instelling bepaalt of Cura coördinaten schrijft voor de printkop of voor nozzle om naar toe te bewegen.

Als uw printer slechts één nozzle heeft, is het coördinatensysteem van uw printer hoogstwaarschijnlijk uitgelijnd met nozzle. Dit betekent dat als u naar positie [50,50] gaat, de nozzletip daadwerkelijk naar die positie wordt verplaatst. Als uw printer echter meerdere nozzles heeft en die nozzles zich naast elkaar in de printkop bevinden, dan is dit van belang.

Op sommige printers zal de printkop naar dezelfde plek bewegen, ongeacht welk nozzle momenteel is geactiveerd. Terwijl de G-code de printer zou kunnen bevelen om naar positie [50,50] te gaan, zou de punt van de momenteel actieve nozzle in plaats daarvan naar positie [68,50] kunnen worden verplaatst, aangezien deze zich bijvoorbeeld 18 mm rechts van de eerste nozzle. Als dit het geval is, moet deze instelling worden ingeschakeld.

Andere printers passen automatisch de positie van de printkop aan om de actieve nozzle te verplaatsen naar de positie gespecificeerd in de G-code. Dat wil zeggen, als de G-code de printer vertelt om naar positie [50,50] te gaan, zou de momenteel actieve extruder naar die positie gaan. De printkop zelf zou een beetje opzij bewegen om de actieve extruder daar te positioneren. Als uw printer zich zo gedraagt, moet deze instelling worden uitgeschakeld.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**