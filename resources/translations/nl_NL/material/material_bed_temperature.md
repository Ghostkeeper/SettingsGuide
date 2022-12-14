Platformtemperatuur
====
Sommige printers hebben een verwarmt platform. Deze instelling bepaalt hoe warm de platform wordt.

Door de platform te verwarmen blijft het materiaal licht vloeibaar en plakkerig. Sommige materialen kristalliseren bij stollen, waardoor het materiaal sterk krimpt. Het verwarmde bed houdt het materiaal net boven deze temperatuur om deze krimp te voorkomen en de kleverigheid van de vloeibare kunststof te behouden. Dit alles om de hechting van de print op de platform te verbeteren.

Als de platform echter te warm wordt gehouden, zal de print zeer vloeibaar zijn op de plaats waar deze de platform raakt. Hierdoor geeft het materiaal een beetje mee, waardoor een [Olifantvoet](../troubleshooting/elephants_foot.md) onderaan de print verschijnt. Dit kan worden gecompenseerd met de instelling [Eerste Laag Horizontale uitbreiding](../shell/xy_offset_layer_0.md) maar beïnvloedt de maatnauwkeurigheid. De verwarming van de platform zorgt ook voor een temperatuurverschil tussen het materiaal dat bovenop de platform ligt en het materiaal verderop in het model, wat resulteert in [Warping](../troubleshooting/warping.md) wanneer het materiaal verderop begint krimpen.

Als deze instelling is ingesteld op 0 graden, geeft Cura geen instructies om de temperatuur van de platform te wijzigen, wat firmwareproblemen kan veroorzaken als er geen verwarmde platform aanwezig is.

**Als je de temperatuur van de platform in een materiaalprofiel aanpast, wordt de instelling [Standaardtemperatuur platform](default_material_bed_temperature.md) aangepast. Normaal gesproken is de temperatuur van de platform hetzelfde als de standaardtemperatuur van de platform, maar soms kan het kiezen van een andere kwaliteit leiden tot kleine aanpassingen van de temperatuur van de platform. Deze temperatuurinstelling voor de platform is de instelling die daadwerkelijk wordt gebruikt voor het printen.**