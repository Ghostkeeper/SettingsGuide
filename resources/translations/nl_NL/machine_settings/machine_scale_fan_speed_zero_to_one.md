Zet de ventilatorsnelheid op 0-1
====
Om de snelheid te regelen waarmee de ventilatoren van de printer draaien, voegt Cura een snelheidsregelende parameter in de g-code-commando's in. Meestal is deze parameter een getal tussen 0 en 255. Sommige printers accepteren echter ook een getal tussen 0 en 1 en interpreteren dit dan anders. Deze instelling zorgt ervoor dat Cura de ventilatorsnelheid schrijft als een getal tussen 0 en 1 in plaats van tussen 0 en 255.

Er zijn 3 verschillende firmware-gedragingen in de verschillende printers op de markt.
* De meeste printers accepteren de ventilatorsnelheid alleen als een getal tussen 0 en 255. Deze instelling moet dan worden uitgeschakeld, anders zal de ventilator nooit goed draaien.
* Sommige printers (met name RepRapFirmware) accepteren getallen tussen 0 en 255, maar interpreteren getallen tussen 0 en 1 als ze 1 of lager zijn. Deze instelling moet dan worden ingeschakeld, anders kan het voorkomen dat Cura de ventilatorsnelheid probeert in te stellen op 0,4% (1 op 255), maar dat de printer deze in plaats daarvan op 100% instelt.
* Sommige printers accepteren alleen cijfers tussen 0 en 1. Deze instelling moet dan ook worden geactiveerd, anders staat de ventilator altijd volledig uit of volledig aan.