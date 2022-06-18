Horizontální rozšíření otvoru
====
Toto je kompenzační opatření pro tiskařský efekt, kde mají otvory tendenci skončit menším tiskem, než bylo zamýšleno. S tímto nastavením můžete zvětšit velikost svislých otvorů v tisku. Podobně jako u běžného nastavení parametru [Horizontální rozšíření](xy_offset.md) se otvory vašeho tisku rozšíří ve všech směrech.

Protože se otvor rozšiřuje ve všech směrech, hodnota tohoto nastavení se ve skutečnosti vztahuje na poloměr otvorů, nikoli na jejich průměr.

![Otvory v tomto tisku musí odpovídat šroubům a osám, ale jsou vytištěny příliš malé](../../../articles/images/hole_xy_offset_0.png)
![Otvory byly zvětšeny, ale zbytek tvaru se nezměnil](../../../articles/images/hole_xy_offset.png)

V důsledku viskozity materiálu má plast při tisku linie plastu v křivce tendenci se táhnout spolu s tryskou v křivce. To způsobí, že křivka je o něco menší, než bylo zamýšleno, když se struna vtáhne dovnitř křivky. Normálně to není opravdu viditelné, ale při tisku položek, které se musí velmi přesně přizpůsobit nebo při tisku položek s velmi malými svislými otvory, se stává přesnost vašeho tisku zničující. Šrouby se už víc nehodí, díly do sebe úhledně nezapadají a tak dále.

Toto nastavení to kompenzuje tím, že všechny otvory mírně zvětší. Na rozdíl od parametru [Horizontální rozšíření](xy_offset.md) to však ovlivní pouze uzavřené otvory. Pokud je na jedné straně dokonce i malý otvor (vodorovně, ve stejné vrstvě), pak tato část nebude považován za otvor a toto nastavení nebude ovlivněno.

Kladná hodnota otvory zvětšuje. Záporná hodnota otvory zmenší. Při kombinaci s horizontálním rozšířením se otvory nejprve rozšíří před použitím obvyklého horizontálního rozšíření. To by mohlo způsobit, že tenké díly úplně zmizí dříve, než se rozšíří běžným horizontálním rozšířením.

Všimněte si, že toto nastavení se týká pouze otvorů v rovině vrstev. Upravuje pouze velikost otvorů v horní nebo dolní části tisku. Otvory na boční straně tisku se neupravují. Navíc neexistují žádná omezení týkající se velikosti nebo tvaru otvoru. Rozšíří se jakákoli dutina, která je zcela obklopena materiálem v dané vrstvě, dokonce i vnitřek nádoby. Navíc to znamená, že jakmile se na boku takové nádoby objeví otvor, vnitřek již není na těchto vrstvách zcela uzavřen, a tak se nerozšíří. Výsledkem je často viditelný hřeben na vnitřní straně nádoby, přesně ve výšce otvoru na boku, kde se vnitřek kvůli tomuto otvoru momentálně nerozšiřuje.