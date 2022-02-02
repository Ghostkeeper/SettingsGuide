Začátek g-kódu
====
Pomocí tohoto nastavení lze napsat část g-kódu, který bude proveden na samém začátku každého tisku. Pomocí tohoto g-kódu lze tiskárnu nastavit tak, aby byla připravena k tisku.

Některé příklady věcí, které se běžně provádějí na začátku g-kódu, jsou:
* Plnění trysky.
* Zahřívání tiskové podložky.
* Zahřívání trysek.
* Kontrola výběru správného extrudéru.
* Konfigurace ventilátorů, zrychlení nebo ryvu (jerku).
* Automatické vyrovnání tiskového lože.
* Konfigurace lineárního postupu.

Přiměřeně obsáhlý seznam dostupných g-kódů, které zde můžete zapsat, najdete na [RepRap Wiki](https://reprap.org/wiki/G-code).

Odkazy na nastavení
----
Při úpravě počátečního g-kódu se můžete odkazovat na hodnoty ostatních nastavení. To používá určitou syntaxi. Nastavení jsou označena *key*. Tento klíč je v Cuře interním názvem. Není vidět v uživatelském rozhraní. Úplný seznam všech klíčů naleznete v [tomto dokumentu](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) ve zdrojovém kódu Cury.

Syntaxe pro získání hodnoty globálního nastavení je následující:

`{setting_key}`

Jinými slovy, zapište klíč nastavení do složených závorek. Tím získáte globální hodnotu nastavení. Mnoho nastavení se však může u každého extrudéru lišit. Na tyto by se mělo odkazovat takto:

`{setting_key, #}`

Zde místo symbolu `#` byste měli napsat číslo extrudéru, ze kterého chcete získat nastavení. Extrudéry se začínají počítat od 0. Globální nastavení lze také získat zadáním extrudéru, ale budou stejné pro všechny extrudéry. Pokud se pokusíte získat teplotu specifickou pro extrudér, aniž byste určili číslo extrudéru, dostanete globální výchozí nastavení pro vaši tiskárnu, než bude použit jakýkoli materiálový profil nebo cokoli (protože materiály jsou specifické pro extrudér).

Tyto odkazy můžete použít například k předehřátí na správnou teplotu nebo k nastavení zrychlení. Zde jsou nějaké příklady:

`M104 S{material_print_temperature_layer_0, 0} ;předehřev`

`M140 S{material_bed_temperature_layer_0} ;ohřev podložky tisku`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Buďte opatrní s rychlostmi. G-kód obvykle přijímá posuv v milimetrech za *minutu*, zatímco nastavení jsou uvedena v milimetrech za *sekundu*. Momentálně není možné zvolit správnou rychlost posuvu. Výpočty v těchto odkazech nejsou možné.

Další informace
----
Stejnou syntaxí jako odkazy na nastavení jsou k dispozici také některé pomocné informace:

* `{time}` označuje aktuální místní čas dne slicování.
* `{date}` označuje datum slicování.
* `{day}` označuje den v týdnu slicování.
* `{initial_extruder_nr}` odkazuje na extrudér, se kterým začne tisk.
<!--if cura_version>=4.12-->
* `{material_id}` odkazuje na jedinečný identifikátor aktivního materiálu. Extruder zadejte podobně jako u ostatních nastavení.
* `{material_name}` odkazuje na název aktivního materiálu. Obvykle se jedná o název, který je uveden na webových stránkách prodávajících tento materiál.
* `{material_type}` označuje třídu aktivního materiálu, jako je PLA nebo ABS.
* `{material_brand}` odkazuje na výrobce aktivního materiálu.
<!--endif-->

Zahřívání před spuštěním g-kódu
----
Cura automaticky vydá příkazy pro ohřev před spuštěním g-kódu. Takže váš startovací g-kód nemusí zvažovat, že se tryska musí zahřívat. Může okamžitě začít plnit trysku. Pokud váš startovací g-kód obsahuje odkaz na jakoukoli teplotu (pro trysku nebo lůžko), bude to deaktivováno (pro trysku nebo lůžko).

**Toto nastavení je nastavení stroje, takže se neobjeví v normálním seznamu nastavení. Lze ho změnit tak, že přejdete na seznam tiskáren v okně předvoleb a kliknete na "Nastavení stroje".**