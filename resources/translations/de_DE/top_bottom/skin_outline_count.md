Linienanzahl der zusätzlichen Außenhaut
====
Wenn Sie die Ober- und Unterseite mit dem Linienmuster drucken, kann der äußere Rand der Außenhautbereiche noch mit einigen konzentrischen Linien gedruckt werden. Das ist etwas anderes als das Drucken einer zusätzlichen Wand, denn die zusätzliche Wand der Außenhaut wird auch zwischen die Außenhaut und die Füllung gelegt.

<!--screenshot {
"image_path": "skin_outline_count_0.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 0},
"layer": 115,
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_outline_count_2.png",
"models": [
    {
        "script": "stamp.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 2},
"layer": 115,
"colours": 64
}-->

![Keine zusätzlichen Außenhautkonturen.](../../../articles/images/skin_outline_count_0.png)
![Zwei zusätzliche Außenhautkonturen](../../../articles/images/skin_outline_count_2.png)

Normalerweise können die Linien der Außenhaut innerhalb der dünnen Füllung enden. Ihre Endpunkte hängen dann ein wenig durch. Wenn es zusätzliche Wände der Außenhaut gibt, druckt der Drucker zunächst einen Rand um die Außenhaut, an dem die normalen Außenhautlinien ansetzen können. Die Außenhaut hängt dann an den Endpunkten nicht so stark durch. Letztendlich wird dadurch die Qualität der Oberseiten etwas verbessert.