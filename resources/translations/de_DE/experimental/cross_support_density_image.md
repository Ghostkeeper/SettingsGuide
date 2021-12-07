Kreuzfülldichte Bild für Stützstruktur
====
Bei dieser Einstellung können Sie ein Bild angeben, das die Dichte an verschiedenen Stellen des Supports angibt. Die Dichte des Supports variiert an bestimmten Stellen je nach der Helligkeit des Bildes. Dies funktioniert nur für das [Kreuzmuster](../support/support_pattern.md), da dieses Muster seine Dichte anpassen kann, ohne Linien zu zerschneiden, was zu einem unterbrochenen Fluss und einer geringeren Stärke führen würde.

<!--screenshot {
"image_path": "cross_support_density_image.png",
"models": [{"script": "wide_bridge.scad"}],
"camera_position": [0, 0, 120],
"layer": 79,
"settings": {
    "support_enable": true,
    "support_pattern": "cross",
    "support_infill_rate": 100,
    "cross_support_density_image": "{root}/resources/articles/images/cross_support_density_image_mask.png"
},
"colours": 32
}-->
![Die Dichte des Supports ist an den Seiten größer](../../../articles/images/cross_support_density_image.png)
![Die zur Erstellung des Musters verwendete Bilddatei](../../../articles/images/cross_support_density_image_mask.png)

Der Pfad zum Bild wird als lokaler Pfad angegeben, zum Beispiel `C:\Projects\3D Printing\infill_density.png` in Windows oder `/home/ghostkeeper/3d_printing/infill_density.png` in Unix. Unterstützte Dateiformate sind JPG, PNG, TGA, BMP, PSD, GIF, HDR und PIC. Das Bild wird so über das Objekt skaliert, dass es genau in die Bounding Box des Objekts passt. Die Helligkeit des Bildes bestimmt die Dichte der Füllung:
* Wenn das Bild schwarz ist, wird die [Dichte der Stützstruktur](../support/support_infill_rate.md) verwendet.
* Wenn das Bild weiß ist, nähert sich die Support-Dichte 0%.

Die Support-Dichte wird niemals den in [Linienabstand der Stützstruktur](../support/support_line_distance.md) angegebenen Wert überschreiten. Sie kann nur verringert werden. Das Muster ist auch darin beschränkt, wo es seine Dichte reduzieren kann. Es versucht zwar, sich der gewünschten Support-Dichte so weit wie möglich anzunähern, aber das ist nicht immer möglich. Wenn die Support-Dichte sehr niedrig ist, gibt es besonders wenig Möglichkeiten, die Support-Dichte anzupassen, was dazu führt, dass der Druck dem Bild nur sehr lose folgt. An Stellen, an denen die Support-Dichte hoch ist, wird das Bild sehr genau verfolgt. Auch die gewählte Dichte ist stark quantifiziert. Die Dichte kann nur verdoppelt oder halbiert werden, aber Cura wird das Muster [dithern](https://en.wikipedia.org/wiki/Dither), um eine größere effektive Genauigkeit zu erreichen.

Mit dieser Einstellung können Sie Ihren Support sehr weit anpassen. Wenn bestimmte Teile Ihres Drucks zum Durchhängen neigen oder sehr genau gedruckt werden müssen, können Sie die Dichte dort lokal erhöhen, um sie besser zu unterstützen, ohne dass die Druckzeit darunter leidet oder das Entfernen des Supports erschwert wird.  

**Diese Einstellung lässt sich nicht gut in Cura-Projektdateien übertragen. Die Projektdatei speichert den Pfad zum Bild als Einstellungswert, aber nicht das Bild. Wenn die Projektdatei auf einem anderen Computer geöffnet wird, wird das Bild der Dichte wahrscheinlich nicht wiederhergestellt.**