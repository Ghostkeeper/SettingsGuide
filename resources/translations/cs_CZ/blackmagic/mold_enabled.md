Forma
====
Namísto tisku samotného modelu tato funkce způsobí, že tiskárna vytvoří negativ modelu, formu, do které byste mohli nalít svůj materiál k vytvoření vašeho modelu. Tato forma má několik specifických vlastností, díky kterým je jak použitelná pro odlévání, tak i tisknutí pomocí tisku FDM. To umožňuje proces [Rychlého odlévání](https://en.wikipedia.org/wiki/Rapid_casting).

![Model, který chcete formovat](../../../articles/images/mold_enabled_shell.png)
![Forma pro tento model](../../../articles/images/mold_enabled_mould.png)

Generace forem Cura vytvoří dutinu s přesným tvarem, který chcete formovat. Kolem této dutiny bude vytvořena skořepina s určitou šířkou, konfigurovatelnou díky parametru [Minimální šířka formy](mold_width.md). Nad a pod formou bude vytvořen plášť s určitou výškou, konfigurovatelnou díky parametru [Výška stropu formy](mold_roof_height.md). Tento plášť však nebude generována na samém vrcholu modelu, takže do ní můžete nalít formovací materiál. Nebude také generována ve spodní části modelu. Během formování ji musíte ponechat na podložce.

Návrh vaší formy
----
Generace forem Cura není dokonalá. Některé prvky chybí. Zde je několik tipů, jak je opravit.
* Cura nevytváří vtoky pro všechna lokální maxima ve vašem modelu. Do svého modelu musíte přidat svislé pruty, kdekoli vtok potřebujete.
* Cura neumožňuje doplnění dalšího materiálu pro případ, že se materiál během ochlazování smršťuje. Pokud používáte materiál, který se hodně smršťuje, budete muset přidat další vtoky do nejvyššího bodu vašeho modelu.
* Forma Cury je vždy z jednoho kusu. Pro mnoho tvarů to znamená, že forma musí být zničena, aby byla odstraněna. Formy mohou být zničeny různými způsoby; pouhou silou nebo zahřátím, pokud to materiál uvnitř umožňuje nebo použitím materiálu jako je PVA, který se ve vodě rozpustí.
* Cura nedovolí vložit pruty nebo dráty k posílení formy. Chcete-li to umožnit, vložte do svého modelu další tyče, aby jim Cura nechala dutiny, a poté vložte do formy tyč nebo drát.
* Podříznutí ve vaší formě jsou generovány bez varování. Pokud váš díl potřebuje hodně podříznutí, budete potřebovat nějaké vtoky nebo jiné kanály, abyste tam dostali materiál, aby tam správně tekl a aby se vzduch dostal ven. Také si uvědomte, že vaše formu může být nutné zničit, aby se po vyhlazení dostala součást ven.

Materiály pro tisk formy
----
Ideální forma je:
* velmi tuhá
* odolná vůči vysokým teplotám
* chemicky inertní, takže se neváže na váš formovací materiál
* vyrobena z materiálu, který se nesmršťuje

Kromě toho musí být některé formy zničeny, aby bylo možné model vyjmout. Za tímto účelem si můžete vybrat křehký materiál nebo materiál, který lze rozpustit pomocí vody nebo jiných chemikálií, jako je PVA.

Materiály použité pro formování
----
Existuje mnoho různých typů materiálů pro odlévání do formy. Některé jsou kompatibilnější se 3D tištěnými formami, než jiné. Zde je několik příkladů materiálů, které mohou fungovat:

* **Silikon**. Silikon se neváže na plasty, takže se snadno odstraňuje. Silikon je také velmi pružný, což ho činí shovívavějším k podříznutí. Kromě toho jsou silikony tepelně tvrditelné a odolné vůči teplu, takže můžete zvážit roztavení formy po jejím vytvrzení. K odlévání silikonu je však třeba použít speciální nástroje. Zejména budete potřebovat vakuovou komoru k odsávání plynových bublin ze silikonu.
* **Písek**. Písek je průmyslovým standardem pro vytváření negativů něčeho, protože je velmi odolný vůči teplu, ale pro odlití nemusí být zahříván. Po nalití ho můžete spojit s betonem nebo lepidlem, abyste zabránili jeho rozpadu. Poté ho můžete použít k vytvoření dalšího negativu z tepelně odolnějšího materiálu.
* **Štuk**. Podobá se písku, ale obvykle se vyrábí z jemnějších zrn. To má tu výhodu, že vazba je již obsažena v materiálu, takže není nutné ho vázat. Může to však vést ke křehčímu konečnému výsledku.
* **Vosk**. Chcete-li vyrobit vlastní svíčky nebo figurky, můžete odlít voskový model. Vosk má nízkou teplotu tání, netaví formu. Rovněž se neváže na plasty, což usnadňuje uvolňování z formy. Vosk je velmi poddajný a snadno se modifikuje po uvolnění z formy. Pokud z něj vyrábíte vlastní svíčku, nezapomeňte vložit knot, než bude odlita.
* **Čokoláda**, jako pochoutka nebo speciální osobní dárek. Chcete-li nalít čokoládu, roztavte ji těsně nad bod tání, poté ji nalijte, trochu vibrujte, abyste dostali vzduchové bubliny ven a okamžitě ji vložte do mrazničky. Formu můžete dokonce umístit do lázně se studenou vodou uvnitř mrazničky, aby se teplo rychle odvádělo. Po pěti minutách čokoládu opatrně vyjměte z formy.

FFF tisk může fungovat pouze s termoplasty. Termoplasty jsou plasty, které při vysokých teplotách přirozeně měknou. To není kompatibilní s litými materiály, které jsou při lití horké. Některé materiály, které jsou obecně nekompatibilní s 3D tištěnými formami:

* **Kovy**, které musí být zahřívány nad bod tání plastů, aby byly dostatečně tekuté, aby mohly být formovány. Tepelná hmota kovu vaši formu roztaví.
* **Plasty, které se váží** na plast, ze kterého je forma vyrobena. Po formování nemůžete od součásti formu oddělit. Můžete nastříkat trochu uvolňovacího činidla, ale pokud je materiál příliš podobný, bude se na formu stále lepit.
* **Materiály po ztuhnutí smršťují**. Materiály, které se před ztuhnutím smršťují, jsou přijatelné za předpokladu, že máte dostatečně dlouhé vtoky, aby mohl nový materiál vyplnit dutinu, když k tomu dojde.
* **Epoxidová pryskyřice** není vhodná, protože když je pryskyřice během lisování studená, chemická reakce těchto dvou složek uvolní dostatečné teplo pro roztavení plastu. Epoxid také velmi dobře k plastům přilne.

Pokud potřebujete vytvořit objekt z materiálu, který není přímo kompatibilní s 3D tiskem, musíte pracovat ve více fázích odlévání. Každá fáze vytváří negativ předchozí fáze. Například byste mohli vytisknout tvar vašeho objektu normálně (s tímto nastavením vypnutým) a pak vytvořit negativ tím, že vložíte formu do štukatury. Vzhledem k tomu, že štuk je mnohem odolnější vůči teplu, můžete použít materiály, které je třeba zahřát na teplotu, aby se roztavily, například bronz nebo materiály, které se vážou na plasty, jako je epoxid.

Proces odlévání
----
Odlévání pomocí 3D tištěné formy je do značné míry stejné jako u jakékoli jiné formy a bude velmi záviset na použitých materiálech. Je tu však několik zvláštních pozorností, pokud jde o 3D tištěné formy.

Termoplast, kterým jste vytiskli svou formu, má nízkou tepelnou kapacitu a může mít poměrně nízkou teplotu skelného přechodu. To znamená, že po vylití formy je rozhodující čas. Pokud materiál chladne příliš pomalu, může forma změknout. To může způsobit její deformaci a ztížení uvolnění výsledku z formy. Chcete-li urychlit nastavení odlévání, můžete ji například vložit do ledové lázně.

3D tištěné formy také mají více zvrásnění podél jejich stran kvůli hranicím mezi vrstvami. To ztěžuje uvolnění odlitku z formy. Používáte-li mezi formou a odlitkem separační prostředek, použijte něco, co tyto mezery zaplní. Tenká maziva nestačí. Vhodnějšími vrstvami pro rozhraní jsou vosková nebo plnější maziva.