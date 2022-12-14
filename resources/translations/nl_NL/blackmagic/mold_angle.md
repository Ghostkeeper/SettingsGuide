Matrijshoek
====
Net als bij de functie [Overhang printbaar maken](../experimental/conical_overhang_enabled.md) wijzigt deze instelling de vorm zodat deze zonder support kan worden geprint. Alleen de buitencontour van de mal wordt veranderd, dus de vorm van je mal wordt niet beïnvloed.

<!--screenshot {
"image_path": "mold_angle.png",
"modellen": [
    {
        "script": "star_podium.scad",
        "transformatie": ["mirrorZ"]
    }
],
"camerapositie": [81, 129, 45],
"instellingen": {
    "mold_enabled": "Waar"
},
"kleuren": 48
}-->
![Onder een hoek van 40 graden kan de onderkant van deze mal worden geprint zonder support](../../../articles/images/mold_angle.png)

Het verkleinen van deze hoek vermindert de extreme uitsteeklengtes. Dit maakt de print betrouwbaarder. Dit verbreedt echter ook de basis van de print, wat de duur van de print aanzienlijk verlengt en het materiaalverbruik verhoogt.

Voor sommige vormen is het niet voldoende om de buitenste vorm te wijzigen om correct te printen. Ze heeft nog steeds support nodig. U kunt een soortgelijk effect bereiken door [Conische supportstructuur inschakelen](../experimental/support_conical_enabled.md) in te schakelen.

<!--screenshot {
"image_path": "mold_needs_support.png",
"modellen": [{"script": "basic_overhang.scad"}],
"camerapositie": [20, 183, 97],
"instellingen": {
    "mold_enabled": "Waar"
},
"kleuren": 32
}-->
![Deze matrijs heeft support nodig](../../../articles/images/mold_needs_support.png)