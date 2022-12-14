Bewegingsoptimalisatie vulling
====
Als u deze instelling inschakelt, kan de doorlooptijd van uw print enigszins worden verkort. Door de verplaatsbewegingen te verkorten zal de druk iets sneller zijn en zal de nozzle ook wat minder gaan lekken. Het duurt echter ook langer om het model te slicen.

Normaal gesproken optimaliseert Cura nogal naïef de volgorde waarin de opvullijnen worden geprint. Na elke lijn zoekt en tekent Cura de dichtstbijzijnde lijn om te tekenen. Voor sommige ongebruikelijke, gecompliceerde vormen kan het pad naar deze volgende vulling echter behoorlijk lang zijn, omdat de [Combing-modus](../travel/retraction_combing.md) vereist dat nozzle een omweg maakt. Cura onderschat dan naïef de afstand en kiest wellicht voor een langere verplaatsbeweging in plaats van een kortere. Als deze instelling is ingeschakeld, wordt de afstand nauwkeurig berekend zodat een betere keuze kan worden gemaakt.

Deze instelling heeft doorgaans weinig invloed op de slicing tijd. Voor gecompliceerde printen met veel kleine onderdelen (waar dit het handigst is), kan het echter de slicing tijd met orden van grootte verlengen.