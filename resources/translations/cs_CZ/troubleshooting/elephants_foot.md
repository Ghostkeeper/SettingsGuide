Sloní noha
====
Někdy je spodní strana tisků mírně širší než zbytek tisků, což tam dává malou ret. Tomu se říká „sloní noha“, protože se podobá nohám slona, jehož prsty jsou o něco širší než zbytek nohy.

Existuje několik efektů, které lidé nazývají „sloní nohou“ a jejichž příčiny jsou zcela odlišné. Tyto efekty také vyžadují zcela jiná řešení. Tento článek vám pomůže najít hlavní příčinu.

![Sloní nohy způsobené silou vrstev pláště](../../../articles/images/elephants_foot.jpg)

Krempa
----
Sloní noha je někdy jen část krempy, která nebyla řádně odstraněna. Pokud jste odtrhli krempu ručně, můžete to říci, protože čára okraje zcela sousedí s normální linií stěny a normální linie stěny je přímo pod zbytkem zdi. Chcete-li krempu úplně odstranit, je nejlepší použít ostrý nůž k odřezávání podél spodní strany tisku..

Pokud model nemá velkou spodní stranu, zvažte místo toho nastavení [metody přilnavosti](../platform_adhesion/adhesion_type.md) na sukénku. Pokud to způsobí příliš mnoho problémů s přilnavostí k lůžku, můžete vyzkoušet jiné metody ke zlepšení přilnavosti, například úpravou [vzoru počáteční vrstvy](../shell/top_bottom_pattern_0.md) na „soustředný“.

Deformace
----
Snad nejčastější příčinou sloní nohy je deformace. Když se materiál ochladí, trochu se zmenší. Někdy se materiál spodní vrstvy (vrstev) nemůže smrštit. Zachovávají si svoji původní velikost, ale horní vrstvy se trochu zmenšují. Existuje několik důvodů, proč se spodní vrstvy nemohou smrštit:
* Je přilepena k tiskové podložce, která se nesmršťuje.
* Zahřívá se tiskovou podložkouu, což zabraňuje smrštění.
* Vedle ní je plášť, který blokuje smrštění. (Na horních vrstvách může být místo toho výplň).

Chcete-li se vyhnout deformaci, podívejte se na [článek o odstraňování problémů](warping.md). Pro tento typ deformace uvádíme několik příkladů toho, co můžete vyzkoušet:
* Zvětšete [tloušťku stěny](../shell/wall_thickness.md), abyste zabránili zmenšení stěn vedle výplně.
* Snižte teplotu [podložky tisku](../material/material_bed_temperature.md), aby se první vrstva mohla smrštit stejně jako ostatní vrstvy. Pokud bylo teplota lože velmi vysoká, může to také umožnit, aby se materiál trochu prohnul, čímž je na dně širší. Tento efekt je obecně slabý, ale dá se mu také zabránit snížením teploty lože.
* Zvětšete [tloušťku spodní vrstvy](../shell/bottom_thickness.md) a postupně přecházejte na zmenšenou velikost. Můžete dokonce zvážit tisk modelu zcela plného (nejlépe nastavením tloušťky spodní strany na extrémně vysokou úroveň), abyste zcela eliminovali rozdíl ve smršťování.

Nastavení podložky tisku
----
Sloní noha může být také způsobena skutečností, že tisková plocha je při tisku první vrstvy příliš blízko trysky. To má za následek nadměrné vytlačování, které tlačí první vrstvu směrem ven.

Chcete-li upravit  tiskovou plochu, přečtěte si návod k vaší 3D tiskárně. Většina tiskáren je vybavena seřizovacími šrouby v loži nebo portálu pro nastavení výškového rozdílu montážní desky během první vrstvy. Upravte montážní desku během tisku (nejlépe během krempy, sukénky nebo raftu) tak, aby první vrstva byla hladká a ne tenčí než ostatní.

Můžete také přímo upravit [tok v první vrstvě](../material/material_flow_layer_0.md) v aplikaci Cura, abyste kompenzovali případné nadměrné vytlačování. Dalším řešením je snížit [šířku linii vrstvy](../resolution/initial_layer_line_width_factor.md) tak, aby se extruze dostatečně normalizovala, aby se zabránilo sloní noze.

Obecná řešení
----
Zde je několik řešení, která můžete vyzkoušet a zbavit se jakéhokoli typu sloní nohy, bez ohledu na její příčinu:
* Použitím [raftu](../platform_adhesion/adhesion_type.md) se přesune celý tisk z podložky tisku, čímž se zabrání jakýmkoli účinkům způsobeným tiskovou podložkou, jako je její teplota a přílišná adheze k podložce, a také se zabrání potřebě na krempy.
* Zmenšete [Horizontální rozšíření počáteční vrstvy](../shell/xy_offset_layer_0.md) (možná na nějakou zápornou hodnotu). To kompenzuje sloní nohu v první vrstvě.