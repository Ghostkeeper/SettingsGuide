Počáteční retrakce sdílené trysky
====
Pokud extrudery tiskárny [sdílejí trysku](machine_extruders_share_nozzle.md), nepředpokládá Cura, že všechny extrudery začínají s vláknem na špičce trysky. Toto nastavení udává, jak daleko od trysky filament začíná. Filament může začínat v jiné vzdálenosti, než je [vzdálenost retrakce pro přepnutí trysek](../dual/switch_extruder_retraction_amount.md), protože filament může být uložen dále, když byla tiskárna neaktivní, než když extruder během tisku stojí.

![Vzdálenost neaktivního vlákna před tiskem](../../../articles/images/machine_extruders_shared_nozzle_initial_retraction.svg)

Cura to použije, aby se ujistila, že je filament na špičce trysky, než zahájí proceduru zaplnění prvního přepnutého extrudéru.