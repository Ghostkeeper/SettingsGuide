Tisk výplně před stěnami
====
To má vliv na pořadí, ve kterém jsou věci vytištěny. Když je tento parametr aktivován, bude výplň části vytištěn před tiskem stěn této části na této vrstvě.

![Nastavení je vypnuto, takže jsou nejprve vytištěny stěny](../../../articles/images/infill_before_walls_disabled.gif)
![Parametr je aktivován, takže se nejprve vytiskne výplň ](../../../articles/images/infill_before_walls_enabled.gif)

Toto nastavení je kompromis mezi přesností a pevností:
* Pokud jsou vytištěny stěny před výplní, nemusí mít stěny k sobě nic, co by způsobilo, že by se dále prohýbaly. Stěny však nejprve ztuhnou a nebudou výplní zatlačeny zpět, což zabrání tomu, aby výplň skrz stěny prosvítala.
* Pokud je výplň vytištěna před stěnami, budou stěny tlačeny zpět na místo, kde je výplň připevněna ke stěnám, takže stěny budou méně přesné a mohou způsobit, že výplň bude přes povrch prosvítat a vytvoří viditelný vzor na vnějším povrchu. Výplň však během tisku lépe drží stěny na místě.
