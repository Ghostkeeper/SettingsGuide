Faktor für Bewegung ohne Ladung
====
Diese Einstellung drückt den Unterschied in der Länge des Filaments aus, wenn es zwischen dem Feeder und der Düsenkammer komprimiert wird.

Wenn das Filament aus der Düse gedrückt wird, entsteht ein Gegendruck durch die Düse selbst (aufgrund der kleineren Düsenöffnung) und durch das Material unter der Düse, sei es das gedruckte Teil oder das Bett. In der Zwischenzeit drückt die Zuführung vom anderen Ende her. Dadurch wird das Filament auf dem Weg zwischen der Zuführung und der Düse zusammengedrückt, wodurch das Filament effektiv verkürzt wird. Daher ist für den Transport des Filaments von der Zuführung zur Düsenspitze weniger Bewegung erforderlich als für den Transport des Filaments in die richtige Druckposition.

Diese Einstellung teilt dem Drucker mit, wie weit das Filament bewegt werden muss, um es zur Düse zu bringen, da er weiß, wie lang die Strecke von der Zuführung zur Düse ist. Dies kann auch dabei helfen, zu bestimmen, wie viel Material vorgespannt werden muss, um die Düse auf den richtigen Druck für den Druck zu bringen.

Materialien, die sich leichter zusammendrücken lassen, wie TPU oder Polypropylen, haben einen niedrigeren Faktor als steife Materialien wie PLA.

**Diese Einstellung ist derzeit nicht in Curas Oberfläche sichtbar. Sie kann nur von den Profilen gesetzt werden. Sie wird auch nicht von Cura beim Slicen verwendet. Drucker, die das Materialdateiformat von Cura verstehen,können es jedoch verwenden, um zu bestimmen, wie das Filament zwischen der Zuführung und der Düse verschoben werden soll.**