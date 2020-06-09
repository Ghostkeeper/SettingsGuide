Šev
====
Stěny vašeho tisku jsou vytištěny v souvislých smyčkách, ale tiskárna musí tuto smyčku někde opustit a řádně ji uzavřít. Pokud smyčka není správně uzavřena, vytvoří se viditelný šev. Tyto švy je obtížné úplně odstranit, ale je možné je skrýt nebo zmenšit jejich velikost.

![Dlouhý svislý šev na povrchu](../../../articles/images/seam.jpg)

Nemělo by se to zaměňovat se "Z švem", což je šev, který se vytvoří, když se tryska posune do výšky další vrstvy. Tento pohyb zastaví trysku na krátkou dobu a vytvoří tam [kapku](blobs.md). Terminologie Cury s nastavením švu je v tomto ohledu historicky nesprávná, protože jeho takzvané nastavení "Z švu" je opravdu o tom, kam umístit normální šev.

Umístění švu
----
Švům je obtížné se vyhnout, ale často je docela snadné skrýt šev na místě, kde to není tak viditelné.

Hlavním parametrem pro úpravu umístění švu je [Zarovnání švu v Z](../shell/z_seam_type.md). Chcete-li skrýt šev, umístěte ho do nejostřejšího rohu. Pomocí parametru [Preference rohového švu](../shell/z_seam_corner.md) si pak můžete vybrat typy rohů, které chcete použít. Pro skrytí švu je lepší zvolit "Skrýt šev" nebo "Inteligentní maskování", které umístí šev do vnitřního rohu. Pokud váš model nemá vnitřní rohy, které lze skrýt, můžete vybrat "Vystavit šev" a umístit šev na špičatý vnější roh, kde je také méně viditelný než na jinak rovném povrchu.

Pokud automatické umístění nefunguje dobře, můžete se také rozhodnout umístit šev sami výběrem "Uživatelsky specifikované". To vám umožní zadat souřadnice [X](../shell/z_seam_x.md) a [Y](../shell/z_seam_y.md), na které bude šev orientován. Vyberte místo, kde nebude šev vidět.

Pokud vše ostatní selže, můžete se také rozprostřít šev po celé ploše výběrem "Náhodné". Namísto spojitého švu na součásti bude spoj umístěn na náhodných místech na povrchu. Povrch bude mírně označen, ale již nebude existovat žádný skutečný šev.

Uzavření švu
----
Šev lze také učinit méně viditelným, pečlivým uzavřením švu, když je vytvořen. Zde jsou některé parametry, které lze upravit tak, aby se snížila viditelnost švů.
* Mírně zvyšte [Vzdálenost otěru vnější stěny](../shell/wall_0_wipe_dist.md). Toto nastavení způsobí, že tryska krátce pokračuje ve svém pohybu kolem obrysu po vytvoření smyčky. Tím se zabrání vytvoření mezeru, kde bude obrys uzavřen. Pokud však toto nastavení příliš zvětšíte, riskujete ukládání příliš velkého množství materiálu kolem místa, kde je šev umístěn, což by ho znovu zviditelnilo.
* Opakem je použití [doběhu](../experimental/coasting_enable.md). Tím se zastaví vytlačování materiálu krátce před uzavřením obrysu. To snižuje tlak uvnitř trysky. Zde je myšlenka, že po dokončení kontury nebude příliš mnoho vytlačování, což snižuje vysunutí švu směrem ven. Jakmile se tryska posune na začátek obrysu, dříve umísťovaný plast snadno zablokuje jakýkoli nový plast, protože tlak v trysce nemůže překonat protitlak zpevněné linie stěny.
* Vytiskněte vnější stěnu [pomaleji](../speed/speed_wall_0.md). Materiál bude moci lépe odtékat pak uzavře šev na konci.
