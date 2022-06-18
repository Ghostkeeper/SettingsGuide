Zrychlení tisku střední vrstvy raftu
====
<!--if cura_version<5.0:Toto nastavení umožňuje konfigurovat hodnotu zrychlení tiskové hlavy během tisku střední vrstvy raftu. Zrychlení během tisku střední vrstvy raftu může být konfigurováno odděleně od zrychlení základní a horní vrstvy.-->
<!--if cura_version>=5.0-->Toto nastavení konfiguruje míru zrychlení tiskové hlavy při tisku středních vrstev rastru. Zrychlení během tisku středních vrstev raftu lze konfigurovat odděleně od základní a horní vrstvy.<!--endif-->

![Kde je umístěna střední vrstva raftu](../images/raft_dimensions_simplified_cs.svg)

Protože raft obvykle sestává z dlouhých úseček, zvyšující se zrychlení má obvykle velmi malý dopad na dobu tisku. Zvýšení zrychlení však ušetří trochu času, když prochází rohy na konci linií.

Zvýšení hodnoty zrychlení způsobí, že tiskárna během tisku středních vrstev raftu více vibruje. Tím se zhorší hladkost horního povrchu raftu, což zase způsobí, že spodní strana tisku spočívající na raftu je méně hladká.