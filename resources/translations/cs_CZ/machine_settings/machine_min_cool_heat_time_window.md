Minimální doba pohotovostního teploty
====
Toto nastavení konfiguruje minimální dobu pohotovosti, při které se bude obtěžovat ochlazovat trysku na pohotovostní teplotu. Pokud je tryska nastavena tak, aby byla v pohotovostním stavu po kratší dobu, než je tato, nebude ochlazena, ale zůstane na [konečné teplotě tisku](../material/material_final_print_temperature.md).

Vaše tryska má PID regulátor, který reguluje, kolik energie je spotřebováno k zahřátí vaší trysky, aby bylo dosaženo správné teploty. Když je trysce přikázáno se ochladit a zahřát se, s velkými teplotními rozdíly v rychlém sledu, PID regulátor má tendenci mylně předpovídat, kolik tepla je potřeba. To způsobuje velké kolísání skutečné teploty trysky. S tímto nastavením jí můžete zabránit tomu, aby přešla na [pohotovostní teplotu](../material/material_standby_temperature.md), pokud je tryska neaktivní po velmi krátkou dobu.

Optimální hodnota pro toto nastavení závisí na vyladění vašeho PID regulátoru. Některé regulátory zvládají rychlé změny cílové teploty lépe než jiné a ty mohou být schopny lépe zvládnout krátkou pohotovostní dobu. Snížení tohoto nastavení by pak pomohlo zabránit materiálu v degradaci uvnitř trysky.

*Protože se jedná o nastavení stroje, není toto nastavení normálně v seznamu nastavení viditelné.*