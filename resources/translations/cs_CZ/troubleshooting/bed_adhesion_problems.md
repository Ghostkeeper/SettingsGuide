Problém s přilnavostí k tiskové ploše
====
Jedním z nejčastějších režimů selhání pro 3D výtisky je to, že se tisk uvolnil od podložky tisku, zatímco byl stále tisknut. V tomto článku jsou uvedeny některé úpravy, které mohou zabránit, aby k tomu nedošlo.

Pokud se tisk z tiskové plochy ztratí, na tiskové podložce obvykle uvidíte spoustu volných vláken. Pokud máte více štěstí, může se to také projevit jako jednoduchý [posun vrstvy](layer_shift.md) (a bude jich méně k vyčištění). V obou případech je tisk zničen.

Metody přilnavosti podložky tisku
----
Cura nabízí několik metod pro zlepšení přilnavosti k tiskovému lůžku. Můžete si vybrat mezi těmito metodami, nastavením parametru [Typ přilnavosti tiskové plochy](../platform_adhesion/adhesion_type.md). K dispozici jsou následující možnosti.
* Krempa, nejběžnější technika, přidává okraje kolem spodní strany tisku, což zvětšuje povrch tisku tak, aby lépe přilnul k tiskové ploše.
* Raft je deska umístěná pod celým tiskem. Tato deska také získá větší povrch, takže dobře přilne. Pokud je raft tištěn materiálem, který dobře přilne k tisku (jako u stejného materiálu), tisk tak zůstane na svém místě.
* Sukénka není připojena k tisku, ale jednoduše ho obkrouží. Tato linie zajišťuje, že materiál před zahájením skutečného tisku proudí, takže nedochází k žádném pod-extruzi v první vrstvě, která by mohla narušit adhezi.
* Nemusíte také mít žádnou přilnavost výběrem "Žádný". To šetří čas a materiál a vyhýbá se dalším negativním účinkům výše uvedených metod. Tuto možnost použijte pouze v případě, že má vaše tiskárna jinou techniku ​​plnění, například napouštěcí kbelík.

Krempa a raft jsou nejúčinnější techniky pro zvýšení přilnavosti, protože jsou navrženy speciálně pro tento účel. Většina tisků přiměřené velikosti bude potřebovat některou z těchto technik.

Je-li použita krempa, můžete dále zvýšit přilnavost zvýšením [šířky krempy](../platform_adhesion/brim_width.md). Také můžete přidat krempu do [vnitřku podpěry](../support/support_brim_enable.md) a do [aktivační věže](../dual/prime_tower_brim_enable.md) a také mezi [model a podpěru](../platform_adhesion/brim_replaces_support.md) a [vnitřní otvory](../platform_adhesion/brim_outside_only.md) modelu.

Podobně, pokud se používá raft, můžete zvýšit přilnavost zvýšením [šířky raftu](../platform_adhesion/raft_margin.md). Raft bude vždy vytištěn pod vším, protože vrstvy se musí shodovat. Pokud je problémem přilnavost mezi modelem a raftem, zvažte snížení [vzduchové mezery](../platform_adhesion/raft_airgap.md) mezi raftem a modelem. Kromě toho můžete zvážit zvýšení [šířky základní linie raftu](../platform_adhesion/raft_base_line_width.md).

Prevence deformace
----
Pokud je váš tisk deformovaný, je kontaktní plocha mezi tiskem a montážní deskou výrazně zmenšena. Chcete-li tomu zabránit, přečtěte si článek o [deformacích](warping.md). Stručně řečeno, je zde několik úprav, aby k deformaci nedošlo.
* Nastavte [vzor dolní počáteční vrstvy](../top_bottom/top_bottom_pattern_0.md) na soustředný.
* Snižte hodnotu [teploty tiskové podložky](../material/material_bed_temperature.md) a zvyšte hodnotu [teploty prostoru objemu tisku](../material/build_volume_temperature.md).
* Upravte model tak, aby na první vrstvě bylo méně ostrých vnějších rohů.

Vyrovnání tiskové plochy
----
Dalším častým zdrojem problémů s přilnavostí je nerovnost tiskové plochy. Cura předpokládá, že se tryska při pohybu na souřadnici Z 0 dotýká tiskové plochy, ale to se stává jen zřídka. Podložky tisku se naklánějí, pohybují se nahoru a dolů, a dokonce se ohýbají. Pokud není tisková plocha všude na souřadnici 0, bude Cura vytlačovat více materiálu, než se vejde do prostoru mezi tryskou a tiskovou plochou, a dojde buď k nadměrnému, nebo nedostatečnému vytlačování. Pokud je podklad příliš blízko, může nadměrná extruze vést k tvorbě kapek, které mohou způsobit, že tryska při pojezdu odtrhne výtisk od popdložky. Když je podložka příliš daleko, nederextruze zabraňuje vytlačení materiálu na tiskovou plochu, což brání jeho správnému spojení s ní. V obou případech není tisk spolehlivý.

Některé tiskárny mají senzory, které dokáží měřit polohu tiskovéplochy a kompenzovat ji ve firmwaru. U těchto tiskáren přesunutí trysky na souřadnici Z 0 skutečně způsobí, že se tryska dotkne tiskové plochy. To má však tu nevýhodu, že se tím model deformuje. Chcete-li kompenzovat nakloněnou podložku tisku, získáte nakloněnou spodní stranu, nebo se může celý tisk naklonit, pootočit nebo zdeformovat. Pokud vaše tiskárna není schopna kompenzovat nerovnou plochu tisku, je několik věcí, které lze udělat i ze strany Cury:
* Zvyšení [výšky počáteční vrstvy](../resolution/layer_height_0.md). To nabízí o něco větší prostor pro chyby. Zvyšuje také sílu, kterou je materiál vytlačován z trysky na tiskovou plochu.
* Snížení [rychlosti přesunu počáteční vrstvy](../speed/speed_layer_0.md). Tím se sníží pravděpodobnost, že pohyby pojezdu vytáhnou dříve vytištěné linie z podložky tisku.
* Stejně tak zvažte úpravu parametrů [zrychlení počáteční vrstvy](../speed/acceleration_layer_0.md) a ryv (jerk) počáteční vrstvy](../speed/jerk_layer_0.md). Ty snižují vibrace, které mohou způsobit periodické podextruze a nadextruze.
* Zvyšte [počet pomalejších vrstev](../speed/speed_slowdown_layers.md). Snížíte tak pravděpodobnost, že rychlé pohyby strhnou předchozí vrstvy.

Různé úpravy
----
Tyto parametry lze také upravit, pokud normální metody adheze k lůžku nejsou dostatečné.
* Zvětšete [šířku linie počáteční vrstvy](../resolution/initial_layer_line_width_factor.md). To tlačí materiál s větší silou a dobře ho přilepuje k tiskové ploše.
* Zvýšení [teploty tisku počáteční vrstvy](../material/material_print_temperature_layer_0.md) způsobuje, že materiál více vytéká na tiskovou podložku, čímž se zvětšuje kontaktní plocha.
* Stejně jako zvýšení teploty, můžete také snížit [rychlost ventilátoru počáteční vrstvy](../cooling/cool_fan_speed_0.md) nebo zvýšit [trvání tohoto nastavení](../cooling/cool_fan_full_at_height.md), abyste materiál udrželi déle tekutý.
* Podobně snižte [rychlost počáteční vrstvy](../speed/speed_layer_0.md). Snížení [rychlosti tisku počáteční vrstvy](../speed/speed_print_layer_0.md) způsobí, že materiál znovu více vytéká, protože materiál je horkou tryskou udržován déle tekutý.

Tiskové plochy
----
Kromě dobrého tisku je pro přilnavost důležitá dobrá podložka tisku. Dobrá podložka tisku by měla být: 
* ...čistá! Je velmi důležité, aby podložka tisku neobsahovala žádné mastnoty (například z prstů) ani prach. Čištění pod horkou vodou je velmi efektivní. Ideální je použít trochu tření alkoholem a hadříkem z mikrovlákna. 
* ...vodorovná! Pokud je podložka tisku příliš blízko, bude tok z trysky nekonzistentní, což bude mít za následek hrboly, které se tryska při příštím průchodu strhne. Pokud je podložka tisku příliš daleko, materiál není na konstrukční desku dobře zatlačen, což výrazně snižuje povrchovou plochu. Většina tiskáren umožňuje seřizovat plochu tisku pomocí několika šroubů, takže se ujistěte, že je dokonale vyrovnána a ve správné vzdálenosti od trysky. 
* ...hrubá! U mírně zdrsněné podložky tisku je kontaktní plocha mezi plochou tisku a potiskem na rozdíl od dokonale hladké podložky tisku značně zvětšena. Některé tiskárny se proto dodávají s matným sklem nebo eloxovaným kovem. 

Materiál podložky tisku má také velký vliv na adhezivní vlastnosti. To se může u různých tiskových materiálů výrazně lišit. Běžnými materiály pro tiskovou podložku jsou sklo, akryl, hliník, ocel nebo eloxovaný hliník. Každý z nich se drží na různých materiálech. Plastové podložky tisku se mohou k vašemu materiálu chemicky přilepit. Ostatní materiály spoléhají na drsný povrch, aby se zvýšila kontaktní plocha. 

Existují také adhezivní metody přilnavosti na podložku, které můžete použít na jakoukoli desku: 
* Běžné lepicí tyčinky fungují velmi dobře. Přestože lepidlo rychle vysychá, vytváří drsný povrch se zvětšenou plochou, na kterou se může tisk přilepit. 
* Maskovací páska má podobný účinek, protože má drsný povrch vyrobený z papíru, ale na rozdíl od papíru zůstává na desce sestavy dokonale plochá. Silnější typy maskovací pásky vyrobené pro venkovní použití jsou nejúčinnější. 
* Vlasový sprej funguje podobně jako lepidlo v tom, že zanechává jemně zrnitý drsný povrch na tiskové podložce. Je velmi snadné ho aplikovat rovnoměrně. 
* Na sestavovací desku naneste trochu brusného papíru, který ji zdrsní a zvětší kontaktní plochu. Nerostte to však příliš nebo budete mít na nerovný povrch. K tomu použijte velmi jemnozrnný brusný papír, zrnitost 500 nebo více. 
* Specializované "adhezní listy" prodává mnoho dodavatelů 3D tiskáren, které lze natáhnout přes podložku tisku. Fungují podobně jako maskovací páska, ale vydrží déle. Některé jsou vyrobeny z plastu, který se také chemicky váže na tištěný materiál. 
