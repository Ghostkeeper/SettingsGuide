Délka proplachování materiálu
====
Pokud tiskárna musí vyměnit vlákno procházející určitou tryskou, musí vypláchnout zbytky materiálu, které byly stále v komoře trysky. Toto nastavení určuje množství materiálu použitého k vypláchnutí předchozího materiálu.

To platí pouze při přechodu na jiný typ materiálu. Pokud je znovu načten stejný typ materiálu (například protože předchozí cívka byla prázdná), použije se [jiná délka](material_end_of_filament_purge_length.md).

**Tento parametr není v rozhraní Cura v současné době viditelný. Může být definován pouze profily. Cura ho během slicování také nepoužívá. Tiskárny, které rozumí formátu materiálového souboru Cura, jej však mohou použít ke správné konfiguraci svého postupu změny vlákna.** Pomocí skriptu pro následné zpracování lze do výtisku vložit příkaz `M600`, který vyvolá změnu vlákna.