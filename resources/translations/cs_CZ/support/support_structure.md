Struktura podpìry
====
S tímto nastavením si mùete vybrat, kterı algoritmus pouijete k vytvoøení podpùrnıch struktur. Tyto konstrukce mají vıraznì odlišné vlastnosti, take vıbìr algoritmu bude mít velkı vliv na to, jak dobøe bude váš tisk podpírán. K dispozici jsou dvì monosti.

Normální
----
![Normální podpùrná konstrukce](../../../articles/images/support_type_everywhere.png)

Jedná se o tradièní podpùrnou strukturu, na kterou je vìtšina lidí zvyklá. Struktura je generována pod pøevislımi oblastmi a obvykle je vyplnìna vzorem, kterı pøímo podpírá pøevislé oblasti. Odtud klesá pøímo dolù, dokud nedosáhne tiskovou podloku nebo èásti modelu, kterou podpírá.

Normální konstrukce podpìry byla vıchozí pro vìtšinu historie 3D tisku a funguje podobnì ve všech slicerech. Toto je zlatı standard, a ne bez dùvodu:
* Díky své robustní struktuøe, velkım kontaktním plochám na modelu a podloce tisku je velmi spolehlivá. Odpouští velmi špatné nastavení nebo špatnì naladìné tiskárny.
* Protoe je tvar jednoduchı, lze ji rychle slicovat.
* Pøímou strukturu podpìry lze snadno pøizpùsobit pro uivatele, protoe je okamitì jasné, které hranice budou podpírány a které nikoli.

Nejdùleitìjší nevıhody vyplıvají ze stejnıch vlastností:
* Díky velkım kontaktním oblastem je podpìra èasto obtínì odstranitelná a mùe na povrchu, kde se dotıká, zanechat znaèné jizvy.
* Pøestoe je stabilní, mùe spotøebovat spoustu materiálu a tisk mùe zabrat spoustu èasu. To lze do urèité míry potlaèit pomocí [kónické podpìry](../experimental/conical_overhang_enabled.md).

Protoe podpìra bude obvykle velká a široká, je pro správné podepøení povrchu potøeba [vıplòovı vzor](support_pattern.md). Cik-cak vzor vıplnì mùe bıt pouit k tisku podpìry z velké èásti z jedné linie a pro umonìní snadnìjšího odstranìní. Další vzory lze kombinovat s extra [obrysy](support_wall_count.md) aby byla podpìra místo toho robustní.

Strom
----
![Stromová podpìra](../../../articles/images/support_structure_tree.png)

Pøi stromové podpìøe zaène podpùrná struktura na desce sestavy malá a její vìtve rostou smìrem k èástem tisku, které potøebují podepøít.

Stromová podpìra se mùe vyhnout pøekákám, kdy roste smìrem k pøevislım oblastem, protoe nemusí splıvat pøímo dolù. Pokud je to vùbec moné, bude podpìra spoèívat pouze na tiskové podloce, aby se zabránilo zjizvení povrchu, na kterém podpìra spoèívá. Pokud z podloky tisku k pøevisu neexistuje ádná cesta, bude podpìra spoèívat na povrchu, kterı je co nejblíe pøevisu, aby se minimalizovalo pouití materiálu. Vìtve stromové podpìry jsou omezeny hodnotou parametru [Úhel vìtve stromové podpìry](support_tree_angle.md) take samotné nevytváøí pøíliš strmı pøevis. To omezuje schopnost rùst kolem pøekáek a také urèuje vıšku, ve které se kmeny zaènou rozvìtvovat.

Konstrukce stromové podpìry má oproti bìné podpìøe øadu velkıch vıhod:
* Stromová podpìra èasto pouívá mnohem ménì materiálu ne bìná podpìra. Bìné je 25 a 50% vyuití materiálu. To šetøí spoustu èasu a sniuje náklady na tisk.
* Vzhledem k jeho malé kontaktní ploše má pøevis pøi pouití stromové podpìry tendenci vypadat lépe.
* Také díky malé kontaktní oblasti bude podpìru snadnìjší odstranit.
* Zanechává na povrchu ménì jizev ne bìná podpìra, protoe je schopna se pohybovat kolem modelu od tiskové podloky smìrem k pøevisu.

Hlavní nevıhody jsou:
* Slicování trvá podstatnì déle ne normální podpìra. Bude zapotøebí trpìlivosti, zejména u vysokıch modelù.
* Pøi tisku nejmenších vìtví dochází v toku k mnoha pøerušením, co zpùsobuje, e stromová podpìra není vhodná pro tisk pomocí materiálù, které lze tìko vytlaèovat, jako je PVA nebo pruné materiály.
* Stromová podpìra nefunguje dobøe pro podpírání nìkterıch mechanickıch modelù. Zejména má tendenci umísovat pøíliš málo vìtví na podporu plochıch, šikmıch pøevisù.

Ve vıchozím nastavení je stromová podpìra dutá. Vìtve budou mít malı hrot, take vıplòovı vzor neposkytuje zvláštní podporu pro pøevislı povrch tištìné poloky. Díky svému zubatému tvaru je stromová podpìra obvykle pomìrnì robustní. Bìná nastavení podpìry však stále platí pro oblast ohranièenou vìtvemi stromu. Pro zvıšení pevnosti podpùrné struktury mùe bıt pouit parametr [Hustota podpìry](support_infill_rate.md).