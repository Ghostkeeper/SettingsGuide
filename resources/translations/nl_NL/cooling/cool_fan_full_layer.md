Normale Ventilatorsnelheid op Laag
====
De ventilatorsnelheid begint bij de waarde van de instelling [Startsnelheid ventilator](cool_fan_speed_0.md) wanneer het printen begint. Tijdens de eerste printlagen zal de ventilatorsnelheid geleidelijk toenemen tot de [Normale Ventilatorsnelheid](cool_fan_speed_min.md) volgens deze instelling.

![Welke ventilatorsnelheid wordt waar gebruikt](../../../articles/images/cool_fan_speed.svg)

Gewoonlijk wordt de initiële ventilatorsnelheid aanzienlijk verlaagd omdat de eerste laag tijdens het printen warm moet blijven. Als de eerste laag afkoelt, begint het beeldmateriaal te [Kromtrekken](../troubleshooting/warping.md). Hierdoor komt de eerste laag van de platform los, waardoor de print mislukt. Als de tweede laag echter te snel afkoelt, zal deze toch krimpen en de eerste laag naar boven afschuiven, waardoor ook de print kromtrekt. Het doel van deze instelling is om meerdere lagen te kunnen printen met een lagere ventilatorsnelheid. Op deze manier kan kromtrekken worden voorkomen totdat de print voldoende stijfheid heeft om kromtrekken te weerstaan.

* Het verhogen van deze instelling kan [Problemen met (print)bed hechting](../troubleshooting/bed_adhesion_problems.md) verbeteren.
* Als uw platform tot een hoge temperatuur wordt verwarmd, moet u deze instelling mogelijk verlagen om te voorkomen dat u [Olifantvoet](../troubleshooting/elephants_foot.md) of lekt.