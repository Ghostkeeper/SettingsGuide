Tloušťka podpěry okraje pláště
====
Při tisku konkávních tvarů bude část horního pláště, která končí někde uprostřed výplně. Toto nastavení přidává další linie skrz výplň pro podpěru okraje pláště, takže bude klesat o něco méně.

![Obvod je protažen výplní pod okrajem pláště](../../../articles/images/skin_edge_support_thickness.png)

Jedna linie napříč mezerami výplně se bude vždy prohýbat, takže linie může být nakreslena v několika vrstvách pod okrajem pláště, která musí být podepřena. Toto nastavení umožňuje nakonfigurovat vertikální tloušťku linie pod okrajem pláště. Můžete také přímo upravit [počet vrstev](skin_edge_support_layers.md) pod okrajem vnější vrstvy, kde bude tato linie nakreslena.

Zvětšení této tloušťky bude mít na tisk obvykle následující účinky:
* Okraj pláště bude lépe podepřen, což způsobí, že horní strana bude hladší, protože plášť může zcela přecházet z jedné strany na druhou.
* Tisk trvá trochu déle a spotřebovává více materiálu.

Pokud je rychlost výplně vysoká, nebude mít toto nastavení prakticky žádný vliv na horní povrch a mohlo by to způsobit [pře-extrudování](../troubleshooting/overextrusion.md) ve výplni. Je proto vhodné nechat ho na 0 mm.