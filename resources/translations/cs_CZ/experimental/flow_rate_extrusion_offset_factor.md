Koeficient kompenzace toku
====
Kompenzace toku je experiment podobný funkci [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) společnosti Marlin. Účelem kompenzace průtoku je kompenzovat pod-extruzi a nad-extruzi, když se mění průtok materiálu tryskou. Toto nastavení umožňuje nakonfigurovat velikost efektu.

Kompenzace toku posouvá vlákno dopředu o další materiál, který je nezbytný v následující sekundě, s každým pohybem. Mezi každým pohybem jsou tři možné scénáře.
* Pokud mají dva sousední příkazy pohybu stejný tok (protože jejich šířky linií, jejich výška vrstvy a jejich rychlost jsou stejné), bude také postup stejný. Vlákno se nebude pohybovat v žádném směru mezi těmito liniemi.
* Pokud se průtok s další linií zvýší, vlákno se během druhé linie posune dále dopředu. Tím se zvyšuje tlak v tryskové komoře, takže se materiál může během tisku linie a následujících linií rychleji vytlačovat.
* Pokud průtok s další linií klesne, vlákno se během druhé linie posune dozadu. Tlak v komoře trysky se tím sníží, takže materiál se během tisku druhé a následujících linií zpomalí.

Vzdálenost, po které se vlákno pohybuje, se rovná množství materiálu, které by bylo během linie každou sekundu vytlačováno (pokud byla linie dostatečně dlouhá, aby mohla tisknout celou sekundu). Díky tomuto nastavení však lze tuto vzdálenost upravit. Zvýšením faktoru bude kompenzační účinek silnější. Jeho snížení oslabí kompenzační účinek. Vyšší faktory budou také vyžadovat více času pro tisk, protože vlákno musí být posouváno nahoru a dolů.

Pokud je tato kompenzace průtoku aktivována, měl by být tlak uvnitř komory trysek lépe vybaven pro zvládnutí nastávajícího průtoku. To může omezit pod-extruzi i nad-extruzi a dát objektu přesnější rozměry.

Kompenzace je však aplikována během jedné linie. Někdy to může být krátká linie, během níž se vlákno musí pohybovat velmi rychle. Možná bude muset tisková hlava zpomalit podávání podavače, což způsobí kapku. Někdy to může být dlouhá linie, která snižuje sílu efektu. Díky tomu je celá kompenzace rychlosti vytlačování nespolehlivá, a proto je toto nastavení stále experimentální.