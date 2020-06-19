Odstranit prázdné první vrstvy
====
Pokud je tato možnost povolena, budou prázdné vrstvy na spodní straně tisku odstraněny. Celý tisk se posune dolů, dokud nebude spočívat na tiskové ploše. Namísto prázdných vrstev, které způsobí selhání tisku, bude tisk o něco nižší.

Pokud je aktivována možnost Cury "Automaticky přetahovat modely na tiskovou plochu", bude toto nastavení pravděpodobně mít jen velmi malý efekt. Může to však efekt mít. Když automaticky spustíte modely na plochu tisku, modely jsou přesně zarovnány s podložkou tisku. Pokud však první vrstva (vrstvy) obsahují pouze příliš malé prvky k tisku (pravděpodobně proto, že dolní plocha není zcela hladká), může být první vrstva v konečném tisku stále prázdná. Toto nastavení tomu brání přesunutím dalších vrstev o jednu vrstvu dolů.

Po posunutí tisku dolů jsou stále aplikovány parametry, které platí pro první vrstvu. Tedy, i když je odstraněna první původní vrstva, na novou první vrstvu se vždy použije [Teplota tisku počáteční vrstvy](../material/material_print_temperature_layer_0.md) a podobné parametry.

Normálně by toto nastavení mělo být vždy povoleno, aby se zabránilo selhání výtisků kvůli tomu, že nejsou vespod zcela hladké nebo jsou nesprávně zarovnány se tiskové podložce. Toto nastavení však můžete deaktivovat, pokud provádíte tiskovou úlohu s více fázemi, které musí být spuštěny ve vzduchu.

Pokud je [aktivována podpěra](../support/support_enable.md), tato podpěra se rozšíří na tiskovou plochu, takže první vrstvy již nebudou prázdné. Žádné vrstvy nebudou odstraněny a tisk se neposune dolů.

Pokud je parametr [Tolerance slicování](../experimental/slicing_tolerance.md) nastaven na "Exkluzivní", bude první vrstva vždy prázdná. Pokud toto nastavení není povoleno, bude první vrstva ve skutečnosti prázdná a váš tisk pravděpodobně selže.


