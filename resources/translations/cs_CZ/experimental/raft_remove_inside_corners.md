Odstranit vnitřní rohy raftu
====
Pokud je toto nastavení povoleno, všechny vnitřní rohy raftu se zcela odstraní, čímž se raft změní na [konvexní tvar](https://en.wikipedia.org/wiki/Convex_set). Raft bude mít pouze vnější rohy.

![Raft již nesleduje tvar modelu](../../../articles/images/raft_remove_inside_corners.png)

To se fakticky rovná velmi vysokému [vyhlazení](../platform_adhesion/raft_smoothing.md). Odstranění vnitřních rohů z raftu má řadu efektů:
* Není již možné, aby malá část raftu vyčnívala daleko za zbytkem raftu. U malých částí raftu je větší pravděpodobnost, že se uvolní z podložky tisku, zejména u vysoce deformovatelných materiálů. Odstraněním vnitřních rohů se tento efekt sníží, takže tisk je spolehlivější.
* Plavba je větší, čímž se zvyšuje celková přilnavá síla k podložce tisku.
* Tisk raftu trvá déle a spotřebuje se na něj více materiálu.