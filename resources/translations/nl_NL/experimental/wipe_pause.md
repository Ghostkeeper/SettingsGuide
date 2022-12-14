Afvegen pauzeren
====
Met deze instelling kan nozzle een korte pauze nemen na het afvegen.

Het veegproces is vrij lang voor een verplaatsbeweging. De nozzle gaat helemaal tot aan de rand van het bouwvolume en beweegt daar heen en weer en moet dan terug naar de print. Gedurende deze tijd zal er veel sijpelen en een langere [Intrekafstand voor afvegen](wipe_retraction_amount.md) die nodig kan zijn. Na het terugtrekken is er een tijd dat de stroming uit nozzle nog op gang moet komen. Door deze pauze kan de nozzlekamer opnieuw onder druk komen te staan ​​wanneer het materiaal weer wordt teruggetrokken, waardoor de eerste lijn goed kan printen zonder noemenswaardige onder-extrusie.

Als u te lang pauzeert, zal er een klodder verschijnen waar nozzle terechtkomt. Afhankelijk van de [Vulling vóór Wanden](../infill/infill_before_walls.md) maakt dit misschien niet uit, omdat de klodder aan de binnenkant van de print kan verschijnen waar deze niet zichtbaar is. Het materiaal dat voor deze klodder is gebruikt, wordt echter niet gebruikt voor de volgende geprinte lijnen, dus ook daar treedt onder-extrusie op. Deze instelling vereist een zorgvuldige afstemming.