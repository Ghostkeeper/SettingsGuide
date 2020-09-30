Rychlost propláchnutí materiálu
====
Pokud tiskárna musí vyměnit vlákno procházející určitou tryskou, musí vypláchnout zbytky materiálu, které byly stále v komoře trysky. Toto nastavení určuje, jak rychle se vlákno vtlačí do podavače, aby se starý materiál odstranil.

To platí pouze při přechodu na jiný typ materiálu. Pokud je znovu načten stejný typ materiálu (například protože předchozí cívka byla prázdná), použije se [jiná rychlost](material_end_of_filament_purge_speed.md).

**Tento parametr není v rozhraní Cura v současné době viditelný. Může být definován pouze profily. Cura ho během slicování také nepoužívá. Tiskárny, které rozumí formátu souboru materiálu Cura, jej však mohou použít ke správné konfiguraci svého postupu změny vlákna.** Díky skriptu pro následné zpracování lze do tisku vložit příkaz `M600`, který vyvolá změnu vlákna.