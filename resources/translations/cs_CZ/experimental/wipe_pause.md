Pauza po otírání
====
S tímto nastavením lze trysku krátce po ukončení procesu otírání krátce zastavit.

Postup otírání je poměrně dlouhý, pokud jde o pohyb. Tryska se posune až na stranu objemu tisku a provede pohyb tam a zpět, poté se musí vrátit k tisku. Během této doby bude spousta výtoku a může být zapotřebí [delší retrakce](wipe_retraction_amount.md). Po zavedení materiálu zpět bude čas, po kterém by měl tryska začít proudit. Tato pauza umožňuje, aby se komora trysky vrátila k tlaku, když se materiál opět vrátil, což umožňuje řádný tisk prvního limie bez výrazné pod-extruze.

Příliš dlouhá přestávka způsobí, že se v místě přistání trysky, objeví kapka. V závislosti na [pořadí tisku](../infill/infill_before_walls.md) to nemusí být významné, protože se kapka může objevit uvnitř tisku tam, kde není viditelná. Materiál použitý pro tuto kapku však nebude použit pro následné tištěné linie, což tam ještě způsobuje pod-extruzi. Tento parametr vyžaduje pečlivé nastavení.
