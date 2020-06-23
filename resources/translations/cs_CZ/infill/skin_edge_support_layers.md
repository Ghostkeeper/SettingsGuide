Vrstvy podpěry okraje pláště
====
Při tisku konkávních tvarů bude horní plášť, který končí někde uprostřed výplně. Toto nastavení přidává další linie skrz výplň pro podpěru okraje pláště, takže bude klesat o něco méně.

![Obvod je protažen výplní pod okrajem pláště](../../../articles/images/skin_edge_support_thickness.png)

Jedna linie napříč mezerami výplně se bude vždy prohýbat, takže linie může být nakreslena v několika vrstvách pod okrajem pláště, která musí být podepřena. Tento parametr umožňuje nakonfigurovat počet vrstev, kterými bude tato linie nakreslena pod okrajem pláště. Lze také nastavit [tloušťku](skin_edge_support_thickness.md) vrstev, kterými je linie vedena.

Zvýšení počtu vrstev bude mít obvykle na tisk následující účinky:
* Okraj pláště bude lépe podepřen, což poskytne hladší horní povrch, protože plášť může zcela přecházet z jedné strany na druhou.
* Tisk trvá trochu déle a spotřebovává více materiálu.

Pokud je rychlost výplně vysoká, nebude mít toto nastavení prakticky žádný vliv na horní povrch a mohlo by to způsobit [pře-extrudování](../troubleshooting/overextrusion.md) ve výplni. Je proto vhodné nechat ho na 0 mm.
