Dichtheid kruisvulling afbeelding
====
Met deze instelling kunt u een afbeelding opgeven die de dichtheid op verschillende punten in de vulling weergeeft. De dichtheid van de vulling varieert op bepaalde plaatsen, afhankelijk van de helderheid van de afbeelding. Dit werkt alleen voor het [Vulpatroon](../infill/infill_pattern.md) omdat dit patroon de dichtheid kan aanpassen zonder lijnen te knippen, wat zou resulteren in een onderbroken doorvoer en een lagere sterkte.

<!--screenshot {
"image_path": "cross_infill_density_image.png",
"modellen": [{"script": "hexagonal_prism.scad"}],
"camera_positie": [0, 0, 180],
"instellingen": {
    "top_lagen": 0,
    "infill_pattern": "cross_3d",
    "infill_sparse_density": 101,
    "cross_infill_density_image": "{root}/resources/articles/images/cross_infill_density_image_mask.png"
},
"kleuren": 32
}-->
![De dichtheid van de vulling varieert over het object](../../../articles/images/cross_infill_density_image.png)
![Het afbeeldingsbestand dat is gebruikt om het patroon te maken](../../../articles/images/cross_infill_density_image_mask.png)

Het pad naar de afbeelding wordt gespecificeerd als een lokaal pad, bijvoorbeeld `C:\Projects\3D Printing\infill_density.png` op Windows of `/home/ghostkeeper/3d_printing/infill_density.png` op Unix. Ondersupportde bestandsindelingen zijn JPG, PNG, TGA, BMP, PSD, GIF, HDR en PIC. De afbeelding wordt over het object geschaald zodat het precies binnen het selectiekader van het object past. De helderheid van de afbeelding bepaalt de dichtheid van de vulling:
* Als de afbeelding zwart is, wordt de [Dichtheid Vulling](../infill/infill_sparse_density.md) gebruikt.
* Als de afbeelding wit is, neigt de vuldichtheid naar 0%.

De dichtheid van de opvulling zal nooit hoger zijn dan de waarde die is opgegeven in de instelling [Lijnafstand Vulling](../infill/infill_line_distance.md). Het kan alleen worden verminderd. Het patroon is ook beperkt in waar het zijn dichtheid kan verminderen. Hoewel wordt geprobeerd de gewenste infill-dichtheid zo goed mogelijk te benaderen, is dit niet altijd mogelijk. Wanneer de infill-dichtheid erg laag is, zijn er bijzonder weinig mogelijkheden om de infill aan te passen, waardoor de print de afbeelding zeer losjes volgt. Op plaatsen waar de infill-dichtheid hoog is, wordt het beeld zeer nauwkeurig getraceerd. De geselecteerde dichtheid is ook sterk gekwantificeerd. De dichtheid kan alleen worden verdubbeld of gehalveerd, maar Cura [dither](https://en.wikipedia.org/wiki/Dither) het patroon voor een grotere effectieve nauwkeurigheid.

Met deze instelling kunt u uw vulling zeer breed aanpassen. Omdat het kruisvulpatroon voornamelijk wordt gebruikt voor flexibele materialen, wordt deze instelling gebruikt om zeer specifieke zachtheids- of hardheidsbeperkingen te bereiken. U kunt bijvoorbeeld een schoenzool printen met aangepaste zachtheid om beter bij de voet te passen, of een mechanisch apparaat dat op bepaalde plaatsen moet buigen.

**Deze instelling vertaalt zich niet goed in Cura-projectbestanden. Het projectbestand slaat het pad naar de afbeelding op als een instellingswaarde, maar niet de afbeelding. Als het projectbestand op een andere computer wordt geopend, wordt de dichtheidsafbeelding waarschijnlijk niet hersteld.**