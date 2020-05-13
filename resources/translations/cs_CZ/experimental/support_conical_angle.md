Úhel kónické podpěry
====
Toto nastavení určuje úhel sklonu, ve kterém je kónická podpěra vytištěna.

![Úhel 30 stupňů](../../../articles/images/support_conical_enabled.png)
![Úhel 10 stupňů](../../../articles/images/support_conical_angle_10.png)
![Úhel -10 stupňů, což rozšiřuje základnu](../../../articles/images/support_conical_angle_neg10.png)

Úhel kónické podpěry je nejvýznamnějším kompromisem mezi stabilitou podpěry a množstvím generované podpěry.

Použití velkého úhlu způsobí, že podpěra bude velmi velká pro velkou část její výšky. To šetří spoustu podpůrného materiálu a tiskového času. Když je potřeba hodně podpůrného materiálu, může to ušetřit spoustu času a materiálu, protože nahoře je polovina podpěry vynechána. Protože se však podpěra ve spodní části velmi ztenčí, podpěra se také může stát méně stabilní, což zvyšuje pravděpodobnost selhání tisku. Chcete-li tomu zabránit, můžete zvětšit [minimální šířku](support_conical_min_width.md).

Použití záporného úhlu způsobí, že podpěra bude širší směrem dolů, ve tvaru sopky. Pokud váš tisk obsahuje drobné prvky, které vyžadují podpěru, obvykle vytvoří velmi vysoké [věže](../support/support_use_towers.md), které jsou během tisku náchylné k převrhnutí. Se záporným úhlem budou tyto vysoké, tenké podpůrné struktury zespodu rozšířeny. To jim dává určitou přidanou stabilitu. Vytištění této podpěry však bude trvat déle, protože vyžaduje více materiálu. Úhel asi -5° je obvykle dostačující k tomu, aby poskytoval dostatečnou stabilitu i těm nejvyšším a nejtenčím podpůrným strukturám. Pokud má váš materiál během přesunů tendenci hodně vytékat, bude vyžadován větší záporný úhel, protože struktura bude více tlačena díky kuličkám na podpěře.
