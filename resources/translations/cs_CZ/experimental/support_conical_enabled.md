Aktivovat kónické podpěry
====
Pokud je tento parametr aktivován, podpůrná struktura již nebude po stranách zcela svislá. Podpěra bude mít kónický tvar, ve spodní části bude menší nebo větší.

![Podpěra se směrem dolů zmenšuje](../../../articles/images/support_conical_enabled.png)
![Podpěra se směrem dolů zvětšuje](../../../articles/images/support_conical_angle_neg10.png)

Samotná podpěra bude nakloněna o určitý [úhel](support_conical_angle.md). V případě záporného úhlu se podpěra rozšiřuje dolů, což ji činí mnohem stabilnější. S kladným úhlem se směrem dolů zmenšuje. To šetří spoustu materiálu a času tisku. Aby se zabránilo nestabilitě podpěry, lze pro podpěru také definovat [minimální šířku](support_conical_min_width.md).

Kónická podpěra je nejsilnějším parametrem pro vyvážení doby tisku a stability podpěry. Existují dva hlavní případy použití kónické podpěry:
* Ušetřete materiál a čas tisku. Ušetřete materiál a čas tisku. Kónická podpěra vám může snadno ušetřit polovinu materiálu potřebného pro podpěru a prodloužením polovinu času stráveného jeho tiskem. To je zvláště efektivní, pokud existují velké objemy podpěry pro velké a vysoké tisky.
* Aby byla podpěra stabilnější použijte záporný úhel. Pokud váš tisk obsahuje drobné prvky, které vyžadují podpěru, obvykle vytvoří velmi vysoké [věže](../support/support_use_towers.md), které jsou během tisku náchylné k převrhnutí. Díky kónické podpěře mohou být tyto vysoké, tenké podpěrné struktury ve spodní části rozšířeny. To jim dává určitou přidanou stabilitu. Vytištění této podpěry však bude trvat déle, protože vyžaduje více materiálu.

Když je [umístění podpěry](../support/support_type.md) nastaveno tak, aby umístilo podpěru pouze na podložku tisku, umožní vám kónická podpěra rozšířit se kolem modelu a pokračovat v podpěře modelu na místech, která jsou nad ostatními částmi modelu. Podpěra bude stále spočívat pouze na tiskové podložce, ale díky svému tvaru se nyní může dostat do převislých oblastí v rozích, které by jinak nebyly podepřeny.

Tato funkce je o něco jednodušší a méně rušivá verze [stromové podpěry](support_tree_enable.md). Stromové podpěry mají stejné výhody jako kónická podpěra. Stromové podpěry však používají zcela odlišný algoritmus a mají větší svobodu při vytváření podpěry, zatímco kónická podpěra zůstává věrnější běžnému algoritmu generování podpěry. To znamená, že parametry běžných médií mají tendenci pracovat nejlépe, když se používají s kónickou podpěrou, ale že je třeba je výrazně upravit pro stromové podpěry. Stromová podpěra má tendenci šetřit více materiálu a tiskového času při zachování spolehlivosti tisku.
