Maximální variace adaptivních vrstev
====
Pomocí tohoto nastavení můžete omezit rozsah, ve kterém mohou adaptivní vrstvy zvolit tloušťku vrstvy. Výška vrstvy se nesmí od této odchylky lišit o více než tato odchylka od normální [výšky vrstvy](../resolution/layer_height.md).

Například s normální výškou vrstvy 0,15 mm a variací nastavenou na 0,1 mm mohou adaptivní vrstvy vytvářet vrstvy o tloušťce mezi 0,05 mm a 0,25 mm.

Toto nastavení omezuje výkon funkce "Adaptivní vrstvy". Pokud je rozsah tlouštěk vrstvy příliš úzký, bude tloušťka vrstvy vždy velmi blízká tloušťce původní vrstvy, jak je definováno nastavením výšky vrstvy. Adaptivní vrstvy nebudou moc šetřit čas ani zlepšovat kvalitu.

Pokud je však rozsah velmi široký, vrstvy mohou být velmi silné nebo velmi tenké. Velmi silné vrstvy vyžadují vysoký průtok na výstupu z trysky, což není vždy možné vzhledem k omezené velikosti trysky a tavicí kapacitě topné dráhy v tiskové hlavě. Velmi tenké vrstvy také nejsou vždy možné kvůli viskozitě materiálu nebo nepřesnosti osy Z. Je proto vhodné omezit rozsah, v němž mohou adaptivní vrstvy tloušťku vrstvy upravit. Jinak bude mít tiskárna potíže s dosažením požadované tloušťky vrstvy.

Tloušťka vrstvy nesmí nikdy klesnout pod 0,001 mm, i když to rozsah dovolí.