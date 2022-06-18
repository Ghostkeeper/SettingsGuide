Ryv (jerk) tisku středních vrstev raftu
====
<!--if cura_version<5.0:Toto nastavení konfiguruje rychlost, jakou může tryska procházet rohy, zatímco se tiskne středová vrstva raftu. Rychlost ryvu (jerku) během tisku střední vrstvy raftu může být konfigurována odděleně od ryvu (jerku) základní a horní vrstvy.-->
<!--if cura_version>=5.0-->Tímto nastavením se konfiguruje rychlost, kterou může tryska projíždět rohy, zatímco se tisknou střední vrstvy rastru. Rychlost ryvu (jerku) při zpracování středních vrstev raftu lze nakonfigurovat odděleně od základních a horních vrstev.<!--endif-->

![Kde je umístěna střední vrstva raftu](../images/raft_dimensions_simplified_cs.svg)

Protože rafty jsou obvykle tvořeny dlouhými lineárními segmenty, zvýšení hodnoty ryvu (jerku) má obvykle velmi malý dopad na dobu tisku. Zvýšení rychlosti ryvu (jerku) však ušetří trochu času při průchodu rohy na koncích linií.

Zvýšení hodnoty ryvu (jerku) způsobí že tiskárna bude při tisku střední <!--if cura_version<5.0:vrstvy--><!--if cura_version>=5.0-->vrstev<!--endif--> raftu více vibrovat. To mírně zvyšuje riziko vytažení voru z podložky tisku.