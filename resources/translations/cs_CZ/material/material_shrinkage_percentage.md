Faktor kompenzace míry smrštění
====

<!--if cura_version >= 4.8-->Toto nastavení před slicováním automaticky efektivně změní měřítko modelu. Cílem je kompenzovat jakékoli smrštění, ke kterému dojde, když se tisk ochladí na pokojovou teplotu. Pokud bude tisk o něco větší, než je žádoucí, konečný výsledek může být přesnější k původním rozměrům vstupního modelu. Tento faktor měřítka se použije stejně na všechny dimenze (X, Y a Z).

Celá scéna je zmenšena od středu. Když tisknete více modelů, všechny mají měřítko od stejného počátečního bodu. To vám umožní umístit tyto modely velmi blízko u sebe, aniž by se v konečném tisku překrývaly. Kolizní oblasti modelů jsou zmenšeny, takže můžete přesně vidět, kde váš tisk skončí. Tím také zabráníte umisťovat modely na scénu na místa, kde by kolidovaly s prvky tisku nebo tiskárny, jako je plnící věž nebo klipy na podložce tisku.

Faktor 100% nezpůsobí žádnou změnu měřítka. Faktor změny o něco větší než 100% je vhodný pro mnoho technických materiálů, jako je ABS nebo polypropylen. Faktor změny měřítka menší než 100% by naznačoval, že se materiál při chlazení rozrůstá, podobně jako pěna.

Čistě chemická data o tom, jak moc se materiál smršťuje mezi teplotou tisku a pokojovou teplotou, nestačí k předpovědi dobré hodnoty pro toto nastavení, protože i proces tisku ovlivňuje smrštění. Při extrudování v linii se plast roztáhne ve směru délky linie a v této ose se v této ose také více smrští. Smrštění není rovnoměrné, ale toto nastavení aplikuje pouze jednotný faktor měřítka ve všech směrech. Abyste získali přesné výsledky, musíte použít měřítko na ose, která je pro vaši aplikaci nejdůležitější. Pokud je podél rozměru spousta dlouhých linií, které jsou nejdůležitější, bude muset být faktor měřítka větší.

Pokud je faktor měřítka větší než 100,5% a tisknete něco velkého, zobrazí Cura varování, že mohou vzniknout [deformace](../troubleshooting/warping.md).<!--endif-->

<!--if cura_version < 4.8:Toto je popisné nastavení, které umožňuje Cuře vědět, jak moc se materiál smršťuje, když přechází z teploty tisku na pokojovou teplotu.

Tento parametr se v současné době nepoužívá pro slicování. V současné době se používá pouze k zobrazení upozornění uživatele při tisku velkých dílů, pokud je míra smrštění větší než 0,5%.
-->
**Tento parametr není v seznamu parametrů viditelný. Jedná se pouze o interní nastavení, které musí být přepsáno materiálovým profilem.**