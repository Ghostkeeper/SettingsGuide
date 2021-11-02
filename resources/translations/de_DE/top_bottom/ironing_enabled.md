Glätten aktivieren
====
Durch das Glätten wird der Drucker veranlasst, einen weiteren Durchgang über die Oberseite zu machen, um sie besonders glatt zu machen. Dieser zusätzliche Durchgang hat eine sehr geringe Linienbreite und druckt besonders langsam.

<!--screenshot {
"image_path": "ironing_enabled_disabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true
},
"colours": 64
}-->
![Ein normaler Druck, von der Oberseite aus gesehen](../../../articles/images/ironing_enabled_disabled.png)
![Beachten Sie die dünnen Linien auf der Oberseite, wenn Glätten aktiviert ist..](../../../articles/images/ironing_enabled_enabled.png)


Durch das Glätten wird ein Linienmuster auf die Oberseite des Drucks gedruckt. Dies hat zwei wesentliche positive Auswirkungen:
* Es schmilzt die Oberfläche wieder an, indem es mehrmals mit einer heißen Düse darüber fährt. Daher kommt auch der Name "Bügeln". Da die Bewegungsgeschwindigkeit so gering und die Linienbreite so klein ist, heizt die Düse die Oberfläche stark auf. Der flache Teil der Düse streicht sie dann glatt.
* Er füllt die Lücken in der Oberfläche auf. Die Bewegung erfolgt auf der gleichen Höhe wie die Schicht selbst. Der Fluss ist geringer als bei einer vollen Schicht, ist aber immer noch vorhanden. Theoretisch kann der Fluss nirgendwo hin, aber in der Praxis hält er den Druck in der Düsenkammer aufrecht. Immer wenn die Düse über eine Unebenheit in der Oberfläche fährt, fließt das Material in der Düse in diesen Spalt.

Das Glätten bringt jedoch auch einige Nachteile mit sich:
* Es verlängert die Druckzeit erheblich.
* Wenn das Muster Unterbrechungen aufweist (weil es zu verschiedenen Teilen fahren muss), hinterlässt es eine sichtbare Linie zwischen dem Teil, der vorher geglättet wurde, und dem Teil, danach. Das kann manchmal vermieden werden, indem das [Glättungsmuster](ironing_pattern.md) auf ein anderes Muster eingestellt wird, z. B. Konzentrisch.
* Abgeschrägte Flächen oder Oberflächen mit vielen Details können ebenfalls geglättet werden, was den Topografie-Effekt verstärkt. Die Grenzen zwischen den Schichten werden stärker ausgeprägt. Dies kann verhindert werden, indem Sie [Nur oberste Schicht glätten](ironing_only_highest_layer.md) aktivieren.
