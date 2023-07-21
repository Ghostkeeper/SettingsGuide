Raft effenen
====
Met deze instelling kunnen de binnenhoeken van het raft gladder worden gemaakt. De instelling specificeert de straal van een boog. Alle binnenhoeken die scherper zijn dan de opgegeven boogradius, worden afgevlakt om de boogradius te behouden.

<!--screenshot {
"image_path": "raft_smoothing_0mm.png",
"modellen": [{"script": "question_stick_clip.scad"}],
"camerapositie": [0, 97, 191],
"instellingen": {
    "adhesion_type": "raft",
    "raft_smoothing": 0
},
"laag": 509,
"kleuren": 64
}-->
<!--screenshot {
"image_path": "raft_smoothing_5mm.png",
"modellen": [{"script": "question_stick_clip.scad"}],
"camerapositie": [0, 97, 191],
"instellingen": {
    "adhesion_type": "raft",
    "raft_smoothing": 5
},
"laag": 509,
"kleuren": 64
}-->
![Niet gladmaken](../../../articles/images/raft_smoothing_0mm.png)
![straal van 5 mm](../../../articles/images/raft_smoothing_5mm.png)

De technische term hiervoor is [morfologische sluiting](https://en.wikipedia.org/wiki/Closing_\(morphology\)). Alle gaten kleiner dan de opgegeven straal worden gesloten. De scherpe binnenhoeken worden daardoor verzacht.

De functie van deze instelling is om het raft stijver te maken. Als meerdere delen door dunne verbindingen met elkaar zijn verbonden, kan het raft op deze punten buigen. Dit maakt het minder stijf en minder bestand tegen vervorming. Als u deze instelling verhoogt, sluiten de afzonderlijke onderdelen beter op elkaar aan, waardoor het raft stabieler wordt. Het oppervlak van het raft wordt groter, waardoor het raft beter blijft plakken. Daarnaast heeft het raft een kleinere totale omtrek, waardoor er minder plekken zijn waar het kan kromtrekken. De vertraging zou daarom over het geheel genomen minder moeten zijn.

Het totale volume van het raft wordt echter ook vergroot. Dit gebruikt meer materiaal en duurt langer om te printen, vooral omdat het raft meestal erg langzaam print.