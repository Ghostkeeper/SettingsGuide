Absolutní pozice zavádění extrudéru
====
Pokud je použita [zaváděcí kapka](../platform_adhesion/prime_blob_enable.md), lze polohu tohoto procesu zavádění upravit pomocí pozice souřadnic [X](../platform_adhesion/extruder_prime_pos_x.md) a [Y](../platform_adhesion/extruder_prime_pos_y.md). Toto nastavení určuje, zda se jedná o pozici na podložce tisku nebo pozici vzhledem k aktuální poloze tiskárny.

Pokud je toto nastavení povoleno, souřadnice X a Y se vztahují k určité pevné pozici na podložce tisku. Extrudér se tam bude vždy přesunovat, aby vytvořil zaváděcí kapku.

Pokud je toto nastavení zakázáno, souřadnice X a Y jsou relativní k poloze, kterou má tryska při prvním přepnutí na extrudér. Pro první extrudér by to byla souřadnice [0,0]. U ostatních extrudérů by to byla jejich počáteční pozice, jak je definováno v definičním souboru extrudéru. Tato počáteční pozice může být také relativní.

Důrazně se doporučuje používat absolutní pozici zavádění. Je zaručeno, že absolutní zaváděcí pozice bude bez kolizí s jinými částmi tisku, protože na toto místo na podložce tisku nemůžete umístit objekty. S relativní zaváděcí pozicí byste mohli skončit kdekoli na tiskové ploše a v důsledku toho by se kapky mohly skončit někde na vrcholu vaší první vrstvy. Použití relativní zaváděcí pozice by mohlo ušetřit nějaký čas na pojíždění, ale opravdu to nestojí za riziko

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.**