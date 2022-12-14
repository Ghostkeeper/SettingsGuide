Maximale snelheid voor fluxbalancering
====
Wanneer de instelling [Egalisatie filamentstroom](speed_equalize_flow_enabled.md) is ingeschakeld, past de techniek voor het vullen van kleine openingen de snelheid aan zodat de doorvoer uit nozzle gelijk is aan de buitenskin, ook al zijn de lijnen veel dunner.

Een probleem hierbij is dat zeer dunne lijnen tot extreem hoge snelheden kunnen leiden. Dergelijke snelheden kunnen niet worden bereikt door de printer, wat resulteert in verloren stappen en eventuele laag overslaan. Met deze instelling zijn deze snelheden tot een maximum beperkt.

Omdat kleine openingen inherent klein zijn, zijn de lijnen die bij deze hoge snelheden worden getrokken, ook vaak kort. Dit betekent dat de nozzle de hoge snelheden sowieso niet kan halen vanwege acceleratielimieten. Deze instelling is meestal alleen van invloed op rechte mechanische printen, waarbij de gap-fill-techniek lange rechte sleuven tussen twee wanden opvult die te klein zijn voor het printen van de nozzle.