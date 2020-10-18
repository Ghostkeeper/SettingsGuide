Zahrnout teplotu materiálu
====
Toto nastavení komunikuje s back-endem slicování, zda má nebo nemá psát příkazy teploty trysky pro zahájení tisku před začátkem g-kódu. Automaticky se nastaví při spuštění slicování.

Pro většinu operací během [začátku g-kódu](machine_start_gcode.md) má smysl mít trysku nastavenou na správnou teplotu pro tisk. Aby se usnadnilo lidem, kteří navrhují definice tiskáren, Cura automaticky zahřeje trysku před spuštěním startovacího g-kódu. Pokud však startovací g-kód obsahuje jakýkoli odkaz na nastavení teploty trysky, nebude již automaticky trysku zahřívat.

**Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné. Jeho změna také nemá žádný efekt, protože ho Cura automaticky změní.**