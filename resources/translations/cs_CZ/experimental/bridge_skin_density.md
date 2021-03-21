Hustota pláště přemostění
====
Toto nastavení řídí hustotu spodní strany tisku, kde překlenuje mezeru. Při 100% hustotě jsou linie umístěny přímo vedle sebe. Při nižších hustotách jsou linie rozmístěny dále od sebe.

![Při 100% hustotě jsou linie umístěny přímo vedle sebe](../../../articles/images/bridge_skin_density_100.png)
![Při hustotě 50% existují mezi liniemi určité mezery](../../../articles/images/bridge_skin_density_50.png)

Při ladění tohoto nastavení jsou při hře dva hlavní efekty: přilnavost mezi liniemi a chlazení.

Při rozmístění linií pláště přímo vedle sebe se ty k sobě přilepí. Díky tomu bude spodní strana přemostěné mezery vypadat lépe, protože povrch bude místo pruhování, spojitý. Kromě toho může druhá linie při přemostění trochu spočívat na první linii, což mírně snižuje prověšení přemostění.

Existuje však další efekt: chlazení. Když jsou linie rozmístěny dále od sebe, budou se moci rychleji ochladit a pak se ani neklesnou. To samozřejmě platí pouze při zapnutém ventilátoru, takže u materiálů s vysokou teplotou tato strategie nefunguje.

Který z těchto vlivu je silnější, závisí na viskozitě materiálu, rychlosti tuhnutí a rychlosti ventilátoru. Vždy je třeba provést určité úpravy.

**Pokud je [Tok při tisku pláště přemostění](bridge_skin_material_flow.md) menší než 100%, bude mezi liniemi také mezera, i když je hustota 100%, protože pak budou linie tenčí.**