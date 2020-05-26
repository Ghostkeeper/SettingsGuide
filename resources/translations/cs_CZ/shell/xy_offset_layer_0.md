Horizontální rozšíření počáteční vrstvy
====
Toto nastavení rozšiřuje pouze počáteční vrstvu, která spočívá na tiskové podložce (nebo na raftu). Pokud jde o [Horizontální rozšíření](xy_offset.md), pozitivní hodnota rozšíří počáteční vrstvu, zatímco záporná hodnota ji sníží.

![Původní model](../../../articles/images/xy_offset_layer_0_original.png)
![Počáteční vrstva je zmenšená](../../../articles/images/xy_offset_layer_0_enabled.png)

Počáteční vrstva je často vytištěna na vyhřívané tiskové podložce, která ji udržuje v mírně kapalném stavu, aby se zlepšila přilnavost k podložce tisku. Počáteční vrstva je obvykle mnohem tlustší než ostatní vrstvy. To ponechává dostatek času a materiálu, aby se vrstva mohla příčně prohýbat, čímž se vytvoří jev nazývaný „sloní noha“, kde spodní strana tisku má mírně širší okraj. Toto nastavení může kompenzovat sloní nohu tím, že původní vrstva se předem ztenčí. Dejte tomuto nastavení malou zápornou hodnotu, abyste kompenzovali sloní nohu.

Tomuto parametru můžete také přiřadit důležitou hodnotu k vytvoření pseudo-krempy kolem vašeho tisku, které lze kombinovat s jinými adhezními technikami, jako je například raft. Mějte na paměti, že to také způsobí expanzi pláště, takže pod stěnami druhé vrstvy bude plášť.

**Kombinace tohoto nastavení s krempou je neúčinné, protože krempa v každém případě vytvoří široké ohraničení kolem počáteční vrstvy.**
