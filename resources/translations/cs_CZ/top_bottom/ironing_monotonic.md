Monotónní pořadí žehlení
====
Normálně Cura řadí žehlicí linie tak, aby vzdálenost mezi nimi byla malá. Pokud je toto nastavení povoleno, uspořádá zažehlovací linie tak, aby se sousední linie tiskly vždy s překrytím ve stejném směru.

Žehlicí linie jsou ve výchozím nastavení mnohem tenčí než tryska, kterou jsou tištěny, takže se budou hodně překrývat s vedlejšími liniemi. Díky tomuto překrytí mají linie mírný sklon, což způsobuje, že odrážejí světlo různými směry. Pokud se sousední linie různě překrývají, tento odraz se změní. To je vidět na konečném výsledku. Různé oblasti povrchu se díky tomu různě lesknou. Tisk v monotónním pořadí zajišťuje, že překrytí je na celém povrchu stejné, takže se neliší v tom, jak odráží světlo. Povrch tak vypadá konzistentněji a hladčeji.

Na rozdíl od [ekvivalentu pro horní/dolní linie](skin_monotonic.md) je však tento efekt pro žehlení přehlušen jiným efektem. Žehlení má tak nízký průtok, že změna průtoku pocházející z běžného tisku je velmi velká. Díky tomu je vrstva žehlení při zahájení tisku silnější a stále zanechává znatelný okraj v místě, kde byl tisk přerušen. Monotónní pořadí tyto okraje neodstraní. Povrch sice může vypadat o něco hladší, ale v praxi je tisk nažehlovacích linií v monotónním pořadí do značné míry neúčinný, pokud vaše tiskárna nemá velmi přesnou kontrolu nad průtokem.

Monotónní pořadí mírně prodlouží délku pojezdů, ale tento vliv je velmi minimální.

Chcete-li dosáhnout hladkého povrchu, zvažte kombinaci tohoto nastavení s nastavením [režimu objíždění](../travel/retraction_combing.md), abyste se vyhnuli vzniku koženého povrchu, a případně zapněte [Z-skok](../travel/retraction_hop.md)..