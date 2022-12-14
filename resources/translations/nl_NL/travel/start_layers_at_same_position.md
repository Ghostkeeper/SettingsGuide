Begin lagen met hetzelfde deel
====
Oorspronkelijk zorgde deze instelling ervoor dat de printer elke laag startte met het object dat zich het dichtst bij de positie bevindt die is opgegeven in de instellingen [Layer Start X](layer_start_x.md) en [Layer Start Y](layer_start_y.md) in plaats van het object dat het laatst is geprint in de vorige laag.

**De instelling was verborgen in Cura 2.4 en is nooit correct verwijderd, daarom is deze instelling nog steeds aanwezig in deze lijst. Het heeft echter geen invloed op het printen.**

De alternatieve methode was niet langer mogelijk nadat multi-threaded slicing was geïntroduceerd, dus de instelling is verborgen.

Door alle lagen in dezelfde volgorde printen, wordt voorkomen dat twee lagen direct achter elkaar op elkaar worden gestapeld wanneer meerdere delen moeten worden geprint. Hierdoor kan de vorige laag langer afkoelen terwijl de nozzle bezig is met het printen van de andere delen. Dit verbetert de overhang en vermindert bandvorming en doorzakken. Aan de andere kant verplaatst dit de printer iets meer, waardoor de printtijd iets langer wordt.