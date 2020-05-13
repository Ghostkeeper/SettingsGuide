Jizvy
====
Pokud má tisk velkou, rovnou horní stranu, existuje riziko zjizvení. To je případ, kdy je na horní straně tisku jasně viditelná linie, která nepatří k normálnímu vzoru. Tato linie označuje jinak hladký horní povrch tisků.

![Diagonální jizva na povrchu](../../../articles/images/scarring.jpg)

Jizvy jsou vytvářeny přesuny, které procházejí přes horní povrch. Horká tryska škrábe povrch, odřízne část plastu, mírně roztaví ostatní plasty a možná vtéká trochu více materiálu do štěrbin. Jizva je čistě vizuální. Neexistuje žádný významný rozdíl v síle nebo přesnosti tisku. Pokud se však na první vrstvě vytvoří jizva, mohlo by se škrábáním oddělit vaše vrstva od podložky tisku.

Prevence
----
Abyste se vyhnuli zjizvení, musíte zabránit tomu, aby tryska poškrábala horní povrch. Horní ploše se můžete vyhnout vodorovně (objezdy), svisle (Z-skoky) nebo zcela zabránit přesunům.
* Pokud nastavíte [režim objíždění](../travel/retraction_combing.md) na „Ne v plášti“, tryska se během pohybu vyhne zasažení pláště. Při přemísťování modelu je dovoleno překročit pouze výplň a stěny. Protože neprochází pláštěm, neměli byste mít jizvy. Pokud však pohyb přesunu začíná nebo končí v plášti nebo není-li k dispozici žádná cesta bez dotyku s pláštěm, bude  pohyb přesunu rovný, aniž by se něčeho dotkl a pokud možno i s retrakcí.
* Aktivujte [Z-skok při retrakci](../travel/retraction_hop_enabled.md) tak, aby tryska mírně stoupla před přechodem přes povrch. Tím bude udržována určitá vzdálenost mezi tryskou a povrchem, takže tryska nebude škrábat. To také pomáhá se vyhnout jizvě. Pokud používáte objíždění, tryska se nejprve pokusí horizontálně vyhnout plášti. Pokud není k dispozici žádná trasa, retrahuje se a poté se zvedne.
* Někdy je možné se vyhnout přesunu nebo provést přesun pouze přes část pláště, která ještě nebyla vytištěna, jednoduše úpravou [horního/dolního směru linií](../shell/skin_angles.md). Cura bude ovládat linie, aby se minimalizovala doba přesunů, ale nad tímto příkazem nedává velkou kontrolu. Otáčením linií pláště nebo otáčením modelu se všechny linie přizpůsobí různě, pořadí tisku se bude lišit a tím se liší i přesuny. Možná už nebudete třeba pjezdů. Jedná se však o proces pokusu a omylu.
