Zahrnout teplotu tiskové podložky
====
Toto nastavení komunikuje s back-endem slicování, zda má nebo nemá psát příkazy teploty tiskové podložky pro zahájení tisku před začátkem g-kódu. Automaticky se nastaví při spuštění slicování.

Pro většinu operací během [začátku g-kódu](machine_start_gcode.md) má smysl mít podložku tisku nastavenou na správnou teplotu pro tisk. Aby se usnadnilo lidem, kteří navrhují definice tiskáren, Cura automaticky zahřeje tiskovou podložku před spuštěním startovacího g-kódu. Pokud však startovací g-kód obsahuje jakýkoli odkaz na nastavení teploty podložky tisku, nebude již automaticky podložku tisku zahřívat.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné. Jeho změna také nemá žádný efekt, protože ho Cura automaticky změní.**