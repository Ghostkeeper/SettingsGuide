Z positie voor Primen Extruder
====
Wanneer [Primeblob inschakelen](../platform_adhesion/prime_blob_enable.md) is ingeschakeld, specificeert deze instelling de z-coördinaat waar de beweging van de priming-blob begint. Cura zal naar deze positie gaan voordat de doorvoer wordt uitgevoerd.

In tegenstelling tot de X- en Y-coördinaten is dit een machine-instelling. Dit komt omdat wordt aangenomen dat de bewerking een vaste Z-coördinaat heeft. Om een Primeblob te creëren, moet nozzle naar de platform toe bewegen en misschien een beetje op en neer bewegen. [X](../platform_adhesion/extruder_prime_pos_x.md) en [Y](../platform_adhesion/extruder_prime_pos_y.md) kunnen worden geselecteerd met de normale instellingen om de positie van de feed drop te verplaatsen als de ruimte op de platform beperkt is is, maar de z-coördinaat niet.

Het enige dat dit verandert, is de Z-coördinaat waar Cura de nozzle naartoe verplaatst voordat het doorvoer commando wordt uitgevoerd.

**Omdat dit een machine-instelling is, is deze instelling normaal gesproken niet zichtbaar in de instellingenlijst.**