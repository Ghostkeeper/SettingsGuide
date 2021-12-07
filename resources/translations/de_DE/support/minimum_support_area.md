Mindestbereich Stützstruktur
====
Diese Einstellung legt eine Mindestgröße für Support-Stücke fest. Wenn ein Support-Stück in einer bestimmten Schicht weniger Fläche hat als der Wert dieser Einstellung, wird der Support dort weggelassen.

<!--screenshot {
"image_path": "minimum_support_area_0.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
    "support_enable": true,
    "minimum_support_area": 0
},
"colours": 64
}-->
<!--screenshot {
"image_path": "minimum_support_area_10.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 190, 47],
"settings": {
    "support_enable": true,
    "minimum_support_area": 10
},
"colours": 64
}-->
![Keine Filterung nach Fläche (Mindestfläche ist 0)](../../../articles/images/minimum_support_area_0.png)
![Kleine Teile des Supports werden weggelassen](../../../articles/images/minimum_support_area_10.png)

Diese Einstellung gibt es, weil dünne Support-Säulen leicht umkippen können. Außerdem unterstützen sie in der Regel kleine Elemente, die ohne Support wahrscheinlich gut gedruckt werden würden. Wenn der Support umkippt, werden viele Blobs auf dem Druck hinterlassen. Daher ist es vielleicht besser, diese dünnen Säulen wegzulassen. Mit dieser Einstellung können Sie den Support anhand der Querschnittsfläche des Pfeilers herausfiltern.

Durch die Vergrößerung der Fläche wird weniger Support gedruckt, was den Zeit- und Materialverbrauch leicht reduziert. Vor allem aber wird die Zuverlässigkeit des Drucks verbessert, da die Gefahr des Umkippens von Support-Säulen geringer ist. Allerdings entfällt dadurch auch der Support für kleine Merkmale in Ihrem Druck, so dass sich die Überhangqualität für diese Teile verschlechtern kann.

Bei einigen Formen kann dies den unangenehmen Nebeneffekt haben, dass der obere Teil des Supports entfernt wird, wenn der obere Teil unter den Schwellenbereich fällt, der untere Teil jedoch nicht. Dies kann dazu führen, dass Teile nicht unterstützt werden, von denen man normalerweise erwarten würde, dass sie unterstützt werden.

<!--screenshot {
"image_path": "minimum_support_area_problem.png",
"models": [{"script": "overhang_bridging_cooling.scad"}],
"camera_position": [117, 0, 15],
"settings": {
    "support_enable": true,
    "minimum_support_area": 50
},
"colours": 64
}-->
![Die Spitze des Bogens wird nicht unterstützt, weil die Fläche auf diesen Schichten zu klein ist](../../../articles/images/minimum_support_area_problem.png) 