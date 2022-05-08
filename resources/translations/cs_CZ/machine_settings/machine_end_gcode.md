Konec g-kódu
====
S tímto nastavením lze zapsat část g-kódu, který bude proveden na samém konci každého tisku. Pomocí tohoto g-kódu může tiskárna vypnout své komponenty a vyčistit se po tisku.

Některé příklady věcí, které se běžně provádějí na konci g-kódu, jsou:

* Retrakce materiálu.
* Chlazení trysek.
* Chlazení tiskové plochy.
* Vypnutí ventilátorů.

Přiměřeně obsáhlý seznam dostupných g-kódů, které zde můžete zapsat, najdete na [RepRap Wiki](https://reprap.org/wiki/G-code).

Odkazy na nastavení
----
Při úpravě koncového g-kódu se můžete odkazovat na hodnoty ostatních nastavení. To používá určitou syntaxi. Nastavení jsou označena *key*. Tento klíč je v Cuře interním názvem. Není vidět v uživatelském rozhraní. Úplný seznam všech klíčů naleznete v [tomto dokumentu](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) ve zdrojovém kódu programu Cura.

Syntaxe pro získání hodnoty globálního nastavení je následující:

`{setting_key}`

Jinými slovy, zapište klíč nastavení do složených závorek. Tím získáte globální hodnotu nastavení. Mnoho nastavení se však může u každého extrudéru lišit. Na tyto by se mělo odkazovat takto:

`{setting_key, #}`

Zde místo symbolu `#` byste měli napsat číslo extrudéru, ze kterého chcete získat nastavení. Extrudéry se začínají počítat od 0. Globální nastavení lze také získat zadáním extrudéru, ale budou stejné pro všechny extrudéry. Pokud se pokusíte získat teplotu specifickou pro extrudér, aniž byste určili číslo extrudéru, dostanete globální výchozí nastavení pro vaši tiskárnu, než bude použit jakýkoli materiálový profil nebo cokoli (protože materiály jsou specifické pro extrudér).

Tyto odkazy můžete použít například k ochlazení na pohotovostní teplotu nebo k obnovení výchozího zrychlení a ryvu (jerku) tiskárny. Zde jsou nějaké příklady:

`M104 T0 S{material_standby_temperature, 0} ;pohotovostní režim pro další tisk`

`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

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

**Toto nastavení je nastavení stroje, takže se neobjeví v normálním seznamu nastavení. Lze ho změnit tak, že přejdete na seznam tiskáren v okně předvoleb a kliknete na "Nastavení stroje".**