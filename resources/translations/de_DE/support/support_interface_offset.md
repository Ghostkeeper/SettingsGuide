Horizontale Erweiterung Stützstruktur-Schnittstelle
====
Diese Einstellung bewirkt, dass die Support-Schnittstelle in alle Richtungen horizontal in den Rest des Supports erweitert wird.

<!--screenshot {
"image_path": "support_interface_offset.png",
"models": [{"script": "f.scad"}],
"camera_position": [45, 45, 133],
"settings": {
    "support_enable": true,
    "support_interface_enable": true,
    "support_offset": 2,
    "support_interface_offset": 1
},
"colours": 64
}-->
![Die Support-Schnittstelle wird in den Support erweitert](../../../articles/images/support_interface_offset.png)

Es gibt zwei Anwendungsfälle für diesen Mechanismus.
* Wenn die Support-Schnittstelle direkt an der Kante des Überhangs endet, der gestützt werden muss, kann das Material über die Kante hängen. Wenn Sie die Schnittstelle ein wenig weiter ausdehnen, wird dies verhindert.
* Einige Materialien, die typischerweise zum Drucken von Support verwendet werden, extrudieren bei niedrigen Durchflussraten schlecht oder brauchen einige Zeit, um in Gang zu kommen. Kleine Bereiche der Support-Schnittstelle passen nicht gut zu diesen Materialien. Mit dieser Einstellung können die Bereiche buchstäblich vergrößert werden, so dass mehr Platz zum Extrudieren dieser Materialien vorhanden ist.

Aufgrund technischer Beschränkungen kann die Support-Schnittstelle nicht über den Support selbst hinaus erweitert werden.