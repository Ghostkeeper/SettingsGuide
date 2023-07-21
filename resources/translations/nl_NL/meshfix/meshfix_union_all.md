Overlappende Volumes Samenvoegen
====
Normaal gesproken, wanneer een model meerdere lichamen bevat die elkaar kruisen, wordt het lichaam dat zich in beide lichamen bevindt niet gevuld. Deze instelling zorgt ervoor dat Cura de interne structuren negeert en gewoon alles invult, ongeacht hoeveel lagen er rond het lichaam zijn.

<!--screenshot {
"image_path": "meshfix_union_all_shell.png",
"modellen": [{"script": "intersecting_cubes.py"}],
"camerapositie": [34, 86, 132],
"laag": -1,
"kleuren": 128
}-->
<!--screenshot {
"image_path": "meshfix_union_all_disabled.png",
"modellen": [{"script": "intersecting_cubes.py"}],
"camerapositie": [34, 86, 132],
"instellingen": {"meshfix_union_all": false},
"laag": 300,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "meshfix_union_all_enabled.png",
"modellen": [{"script": "intersecting_cubes.py"}],
"camerapositie": [34, 86, 132],
"instellingen": {"meshfix_union_all": true},
"laag": 300,
"kleuren": 64
}-->
![Een mesh met twee elkaar kruisende kubussen](../../../articles/images/meshfix_union_all_shell.png)
![Niet alle volumes samengevoegd](../../../articles/images/meshfix_union_all_disabled.png)
![Samenvoegen heeft het gat verwijderd](../../../articles/images/meshfix_union_all_enabled.png)

Technisch gezien verandert deze instelling de regel van [Even-Oneven](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) in [Nonzero](https://en.wikipedia.org/wiki/Nonzero-rule). Normaal gesproken wordt een volume gevuld wanneer het wordt omgeven door een oneven aantal lagen. Als deze instelling is ingeschakeld, wordt deze gevuld als deze wordt omgeven door een niet-nul aantal lagen.

**Dit werkt alleen voor bodies binnen hetzelfde model. Als je meerdere bestanden hebt geladen en ze overlappen elkaar in Cura, heeft deze instelling geen effect. Vergelijk de instelling Mesh Overlap verwijderen om problemen op te lossen met meerdere afzonderlijke meshes die elkaar overlappen.**