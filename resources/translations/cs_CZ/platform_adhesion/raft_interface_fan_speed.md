Rychlost ventilátoru střední vrstvy raftu
====
<!--if cura_version<5.0:Toto nastavení umožňuje konfigurovat rychlost ventilátoru při tisku střední vrstvy raftu. Rychlost ventilátoru při tisku střední vrstvy lze konfigurovat odděleně od rychlosti ventilátoru pro základní a horní vrstvu.-->
<!--if cura_version>=5.0-->Toto nastavení konfiguruje rychlost ventilátoru při tisku středních vrstev raftu. Rychlost ventilátoru při tisku středních vrstev lze konfigurovat odděleně od základní a horní vrstvy.<!--endif-->

![Kde je umístěna střední vrstva raftu](../images/raft_dimensions_simplified_cs.svg)

Je užitečné nakonfigurovat Rychlost ventilátoru pro střední <!--if cura_version<5.0:vrstvu--><!--if cura_version>=5.0-->vrstvy<!--endif--> zvlášť, protože snížení rychlost ventilátoru může zlepšit přilnavost k lůžku a snížit deformaci. Zvýšení rychlosti ventilátoru může zlepšit hladkost povrchu, ale to není problém pro střední <!--if cura_version<5.0:vrstvu--><!--if cura_version>=5.0-->vrstvy<!--endif-->. Proto je vhodné nastavit rychlost ventilátoru o něco níže než v horních vrstvách.