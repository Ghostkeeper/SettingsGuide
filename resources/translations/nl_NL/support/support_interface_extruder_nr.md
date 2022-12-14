Extruder Verbindingsstructur
====
Als uw printer is uitgerust met meerdere extruders, kunnen de lagen waar de support het model raakt, worden geprint met een andere extruder dan het hoofdgedeelte van de support. Met deze instelling kunt u kiezen welke extruder wordt gebruikt voor de supportstructuur.

<!--screenshot {
"image_path": "support_interface_extruder_nr.png",
"modellen": [
    {
        "script": "question_stick_clip.scad",
        "transformatie": ["roterenY(90)"],
        "object_settings": {"extruder_nr": 1}
    }
],
"camerapositie": [134, 134, 113],
"instellingen": {
    "support_enable": waar,
    "support_interface_enable": waar,
    "support_use_towers": false,
    "support_extruder_nr": 3,
    "support_interface_extruder_nr": 2
},
"color_scheme": "materiaal_kleur",
"kleuren": 64
}-->
![De supportstructuur is in rood geprint, maar het hoofdgedeelte is in wit geprint.](../../../articles/images/support_interface_extruder_nr.png)

Sommige materialen zijn beter geschikt voor printsupport dan andere. Ze hechten bijvoorbeeld niet chemisch aan de bouwstof en zijn daardoor makkelijker te verwijderen, of ze lossen op in water of alcohol. Dergelijke materialen zijn echter vaak duur en het printen duurt langer. Met deze instelling kunt u de supportstructuur printen met een andere extruder dan de hoofdeenheid, zodat het grootste deel van de support nog steeds snel en/of met goedkopere materialen wordt geprint, maar toch de voordelen heeft van het gespecialiseerde supportmateriaal.

Als u oplosbare materialen gebruikt om de supportstructuur te printen, maar onoplosbare materialen om de supportvulling te printen, denk er dan aan dat de vulling mogelijk niet uit holtes kan worden verwijderd als het fysiek niet mogelijk is om de supportvulling te vervangen door een kleine opening. Waar een oplosbaar materiaal normaal gesproken door een holte kan stromen, kunnen onoplosbare materialen er mogelijk niet doorheen.