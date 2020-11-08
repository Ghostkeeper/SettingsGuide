Vzdálenost pohybů otěru
====
Tento parametr umožňuje definovat šířku stíracích pohybů. Tryska se posune o tuto vzdálenost pro [každý pohyb otírání](wipe_repeat_count.md).

Na začátku bude tryska umístěna těsně za kartáč na otírání v [určité souřadnici X](wipe_brush_pos_x.md). Vzdálenost uvedená v tomto nastavení musí být taková, aby posunutí v této vzdálenosti ji umístilo na druhou stranu kartáče. Přílišný pohyb zavádí zbytečné pohyby a může způsobit, že se tryska vrátí do prostoru tisku, což může způsobit zbytečné zásahy do modelu, pokud nejsou [Z-skoky povoleny](wipe_hop_enable.md). Nedostatečný pohyb může zabránit tomu, aby se správně zasáhl kartáč.

Vzdálenost může být také záporná. Tryska pak otře jiným směrem. V závislosti na vaší volbě [souřadnice X](wipe_brush_pos_x.md) to může být nutné, aby bylo možné otírat správným směrem.