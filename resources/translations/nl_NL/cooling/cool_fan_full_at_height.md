Normale Ventilatorsnelheid op Hoogte
====
De ventilatorsnelheid begint bij de waarde van de instelling [Startsnelheid ventilator](cool_fan_speed_0.md) aan het begin van de print. Tijdens de eerste printlagen om het in deze instelling gespecificeerde niveau te bereiken, zal de ventilatorsnelheid geleidelijk toenemen tot de [Normale Ventilatorsnelheid](cool_fan_speed_min.md).

![Welke ventilatorsnelheid wordt waar gebruikt](../../../articles/images/cool_fan_speed.svg)

Gewoonlijk wordt de initiële ventilatorsnelheid aanzienlijk verlaagd omdat de eerste laag tijdens het printen warm moet blijven. Als de eerste laag afkoelt, begint het materiaal te [Kromtrekken](../troubleshooting/warping.md). Hierdoor komt de eerste laag van de platform los, waardoor de print mislukt. Als de tweede laag echter te snel afkoelt, zal deze toch krimpen en de eerste laag naar boven afschuiven, waardoor ook de print kromtrekt. Het doel van deze instelling is om meerdere lagen te kunnen printen met een lagere ventilatorsnelheid. Op deze manier kan kromtrekken worden voorkomen totdat de print voldoende stijfheid heeft om kromtrekken te weerstaan.

Het simpelweg verminderen van de snelheid van de ventilator tijdens de eerste paar lagen zou resulteren in een grote verandering in ventilatorsnelheid, wat merkbaar zou zijn in de oppervlaktekwaliteit van de uiteindelijke print. Dit leidt tot strepen. In plaats daarvan wordt de ventilatorsnelheid geleidelijk gewijzigd naar de normale ventilatorsnelheid.

* Het verhogen van deze instelling kan [Problemen met (print)bed hechting](../troubleshooting/bed_adhesion_problems.md) verbeteren.
* Als uw platform tot een hoge temperatuur wordt verwarmd, moet u deze instelling mogelijk verlagen om te voorkomen dat u een [Olifant voet](../troubleshooting/elephants_foot.md) print of lekt.