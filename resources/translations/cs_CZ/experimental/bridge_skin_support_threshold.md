Mezní hodnota podpěry pláště přemostění
====
Tento parametr umožňuje upravit citlivost detekce přemostěných oblastí. Překlenovací oblasti jsou detekovány na základě části oblasti pláště, která je podporována něčím v předchozí vrstvě.

Pro každou disjunktní oblast pláště vyhledá, jak velká část tohoto pláště je podpírána něčím ve spodní vrstvě. Pokud je oblast podpírána příliš málo, bude technika přemostění aplikována na oblasti pláště, které nejsou podpírány.

Aplikace techniky přemostění na plášť způsobuje změny průtoku a rychlosti tisku. Tito se snaží upravit rychlost, jakou se materiál vylévá z trysky, ale to bývá obtížné měnit. Výsledkem je, že v některých částech tisku dojde k nad-extruzi a v jiných k pod-extruzi, protože se tok snaží průtok upravit. Úprava rychlosti průtoku pro velmi malou část převisu tedy s největší pravděpodobností sníží kvalitu tisku místo toho, aby ji vylepšilo.

Zvýšením tohoto nastavení bude přemosťovací technika aplikována na menší části převisu, kde přemostění je méně účinné, ale kde je tok vždy přerušen. Pokud je toto nastavení sníženo, bude přemosťovací technika použita pouze ve velmi velkých převislých oblastech. To nezpůsobí tolik změn toku, ale může to snížit kvalitu převisu pro menší oblasti převisu.