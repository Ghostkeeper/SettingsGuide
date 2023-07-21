Extruders delen nozzle
====
Met deze instelling kunt u specificeren dat uw printer slechts één nozzle heeft en dat al het filament door hetzelfde nozzle wordt geduwd. Cura zal dan haar voorbereidingsstrategie wijzigen.

Normaal gesproken gaat Cura ervan uit dat na het uitvoeren van de [Start G-Code](machine_start_gcode.md) alle extruders hun filament bij de nozzletip hebben en klaar zijn om te printen. Als de extruders een nozzle delen, is dit niet mogelijk omdat er maar één filament tegelijk in de nozzle kan zitten. In plaats van de normale vulprocedure met een [Primeblob inschakelen](../platform_adhesion/prime_blob_enable.md) of extra roklijnen, moet nozzle worden geprimed als een volledige extruderwissel. Dit omvat printen in de [Primepijler inschakelen_tower](../dual/prime_tower_enable.md) indien ingeschakeld.

Als alle extruders een nozzle delen, is het logisch dat ze ook een verwarming [Extruders delen verwarming](machine_extruders_share_heater.md). Cura creëert echter niet op zichzelf een verbinding tussen de twee. Zorg er dus voor dat u beide inschakelt als uw printer daadwerkelijk een enkele nozzle en een enkele verwarming voor alle extruders heeft.

**Omdat dit een apparaatinstelling is, wordt deze normaal gesproken niet vermeld in de normale lijst met instellingen. Er is echter een selectievakje voor deze instelling in het dialoogvenster Printerinstellingen, dat u kunt vinden in de lijst met toegevoegde printers in het dialoogvenster Instellingen.**