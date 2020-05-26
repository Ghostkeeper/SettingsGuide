Topografie nebo schodiště
====
Efekt "topografie" se dosáhne, když je šikmá horní nebo spodní plocha potištěna malým množstvím vrstev, takže hranice mezi vrstvami jsou dostatečně rozloženy, aby byly snadno viditelné. Je pojmenována po [topografických mapách](https://en.wikipedia.org/wiki/Topographic_maps), kde jsou rozdíly v nadmořské výšce obecně naznačeny vrstevnicemi.

![Můžete jasně vidět okraje vrstev](../../../articles/images/topography.jpg)

Tento efekt je při 3D tisku všudypřítomný a je to jeden z nejjednodušších způsobů, jak rozpoznat, že objekt byl vytištěn ve 3D. Tomu lze zabránit, ale jeho zabránění obecně výrazně snižuje produktivitu.

Výška vrstvy
----
Protože efekt topografie nastává, když jsou hranice mezi vrstvami velmi daleko od sebe, je možné se tomuto efektu vyhnout snížením [výšky vrstvy](../resolution/layer_height.md). Když je výška vrstvy snížena, menší vertikální přírůstky mezi vrstvami také povedou k menším horizontálním krokům, což snižuje efekt topografie. Snížení výšky vrstvy však výrazně prodlužuje dobu tisku.

Namísto snižování výšky vrstvy pro celý tisk můžete také výšku vrstvy snižovat pouze pro malé svahy tisku pomocí funkce [Použít adaptivní vrstvy](../experimental/adaptive_layer_height_enabled.md). To výrazně snižuje účinek topografie při minimálním dopadu na dobu tisku. Je však obtížnější upravit tisk pro jiné kvality, než jaké jsou uvedeny výše, protože nastavení obecně závisí na výšce vrstvy.

Úpravy modelu
----
Můžete také zvážit otočení modelu, aby v tisku nebyly žádné mělké svahy. Ale obvykle to znamená, že pro váš model budete tisknout mnohem více podpěr, což také snižuje produktivitu a převisy nemusí vypadat tak dobře.
