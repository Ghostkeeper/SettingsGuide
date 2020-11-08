Rychlost vnitřní stěny
====

Rychlost tisku vnitřních stěn může být konfigurována odděleně od běžné rychlosti tisku a tisku vnější stěny.

![Různé struktury tištěné různými rychlostmi](../../../articles/images/speed_difference.png)

Vnitřní stěny jsou pro vizuální kvalitu méně důležité než vnější stěny. Ovlivňují však umístění vnějších stěn, takže materiál vnějších stěn je tlačen směrem ven, pokud je [vnější stěna vytištěna po vnitřních stěnách](../shell/outer_inset_first.md) nebo přímo tlačí vnější stěnu směrem ven, pokud je vnější stěna vytištěna jako první. Je proto důležité tisknout vnitřní stěny s přesností, ale lze je tisknout o něco rychleji než vnější stěny, aby se ušetřil čas.

Snížení rychlosti vnitřní stěny snižuje vibrace během tisku této struktury, což snižuje zvlnění. To také zlepšuje převis, protože ventilátory tiskové hlavy mají více času na ochlazení materiálu, zatímco je stále držen tryskou napnutý.

Pokud je však rychlost tisku vnitřní stěny příliš nízká, existuje riziko, že dojde k příliš velké změně průtoku. Pokud musí tryska náhle vytlačit mnohem pomaleji, bude chvíli vytlačovat hodně materiálu, zatímco tlak v komoře trysky klesá, takže na začátku stěny bude nad-extruze.

Vnitřní stěny také odpovídají za značnou část doby tisku, takže snížení rychlosti, při které se vnitřní stěny tisknou, výrazně prodlouží dobu tisku.