Maximální úhel špagetové výplně
====
Tento parametr konfiguruje maximální úhel převisu, kterého materiál dosáhne, když je materiál výplně uložen vedle něj. Pokud z důvodu tohoto limitu nelze místo vyplnit příslušnou hustotou, budou zavedeny [další kroky](spaghetti_infill_stepped.md) podél výšky objemu výplně, aby bylo zajištěno, že jsou tato místa správně dosažena.

Pokud má být špagetová výplň použita jako flexibilní výplň, mělo by být toto nastavení pravděpodobně nastaveno poměrně vysoko. Zvýšení tohoto nastavení způsobí, že se pod mělkými střechami dosáhne více kroků. Protože špagetová výplň nemá tendenci se rozpínat příliš daleko v horizontálních směrech, pomáhá přidání dalších kroků tlačit materiál pod tyto mělké střechy.

Pokud se má špagetová výplň používat s odlitým materiálem, lze toto nastavení výrazně snížit. Protože materiál, který se nalije, je tekutý, může dosáhnout velmi velkých vzdáleností pod povrchy. Nenastavujte ji však ještě na 0°, protože většina odlitků má určitou viskozitu. Stále ho můžete nalít pod mělké střechy, abyste se ujistili, že vylitý materiál zcela odpovídá jeho skořepině.
