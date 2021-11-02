Glättungsfluss
====
Beim Glätten werden zusätzliche Linien in die Oberfläche eingebracht, was technisch gesehen eine Überextrudierung darstellt. Diese Einstellung steuert, wie viel in diesem zusätzlichen Durchgang extrudiert wird. Der Fluss ist notwendig, um Lücken in der Oberfläche zu füllen.

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
<!--screenshot {
"image_path": "ironing_flow.png",
"models": [
    {
        "script": "dial_brace.scad",
        "transformation": ["scale(0.5)"]
    }
],
"camera_position": [0, 14, 83],
"settings": {
    "layer_height": 0.2,
    "ironing_enabled": true,
    "ironing_flow": 20
},
"colours": 64
}-->
![10% fluss](../../../articles/images/ironing_enabled_enabled.png)
![20% fluss](../../../articles/images/ironing_flow.png)

Sie sollten diese Einstellung hoch genug wählen, um den Druck auf die Düse aufrechtzuerhalten. Dieser Druck muss die Lücken auf der Oberseite ausfüllen. Wenn Sie eine sehr raue Oberfläche haben (aufgrund des Pillow-Effekts oder zu schnellem drucken), müssen Sie diese Einstellung möglicherweise erhöhen.