Kreuzfülldichte Bild
====
Bei dieser Einstellung können Sie ein Bild angeben, das die Dichte an verschiedenen Stellen der Füllung angibt. Die Dichte der Füllung variiert an bestimmten Stellen in Abhängigkeit von der Helligkeit des Bildes. Dies funktioniert nur für das [Kreuz (3D)-Muster](../infill/infill_pattern.md), da dieses Muster seine Dichte anpassen kann, ohne Linien abzuschneiden, was zu einem unterbrochenen Fluss und einer geringeren Stärke führen würde.

<!--screenshot {
"image_path": "cross_infill_density_image.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
    "top_layers": 0,
    "infill_pattern": "cross_3d",
    "infill_sparse_density": 101,
    "cross_infill_density_image": "{root}/resources/articles/images/cross_infill_density_image_mask.png"
},
"colours": 32
}-->
![Die Dichte der Füllung variiert über das Objekt](../../../articles/images/cross_infill_density_image.png)
![Die zur Erstellung des Musters verwendete Bilddatei](../../../articles/images/cross_infill_density_image_mask.png)

Der Pfad zum Bild wird als lokaler Pfad angegeben, zum Beispiel `C:\Projects\3D Printing\infill_density.png` in Windows oder `/home/ghostkeeper/3d_printing/infill_density.png` in Unix. Unterstützte Dateiformate sind JPG, PNG, TGA, BMP, PSD, GIF, HDR und PIC. Das Bild wird so über das Objekt skaliert, dass es genau in die Bounding Box des Objekts passt. Die Helligkeit des Bildes bestimmt die Dichte der Füllung:
* Wenn das Bild schwarz ist, wird die [Fülldichte](../infill/infill_sparse_density.md) verwendet.
* Ist das Bild weiß, geht die Fülldichte gegen 0%.

Die Dichte der Füllung wird niemals den Wert überschreiten, der in der Einstellung [Linienabstand Füllung](../infill/infill_line_distance.md) angegeben ist. Sie kann nur reduziert werden. Das Muster ist auch darin beschränkt, wo es seine Dichte reduzieren kann. Es versucht zwar, sich der gewünschten Fülldichte so weit wie möglich anzunähern, aber das ist nicht immer möglich. Wenn die Fülldichte sehr niedrig ist, gibt es besonders wenige Möglichkeiten, die Füllung anzupassen, was dazu führt, dass der Druck dem Bild nur sehr lose folgt. An Stellen, an denen die Fülldichte hoch ist, wird das Bild sehr genau nachgezeichnet. Auch die gewählte Dichte ist stark quantifiziert. Die Dichte kann nur verdoppelt oder halbiert werden, aber Cura wird das Muster [dithern](https://en.wikipedia.org/wiki/Dither), um eine größere effektive Genauigkeit zu erreichen.

Mit dieser Einstellung können Sie Ihre Füllung sehr weit anpassen. Da das Kreuzfüllmuster hauptsächlich für flexible Materialien verwendet wird, wird diese Einstellung verwendet, um sehr spezifische Einschränkungen für die Weichheit oder Härte zu erreichen. So könnte man zum Beispiel eine Schuhsohle mit angepasster Weichheit drucken, damit sie sich besser an den Fuß anpasst, oder ein mechanisches Gerät, das sich an bestimmten Stellen biegen muss. 

**Diese Einstellung lässt sich nicht gut in Cura-Projektdateien übertragen. Die Projektdatei speichert den Pfad zum Bild als Einstellungswert, aber nicht das Bild. Wenn die Projektdatei auf einem anderen Computer geöffnet wird, wird das Bild der Dichte wahrscheinlich nicht wiederhergestellt.**