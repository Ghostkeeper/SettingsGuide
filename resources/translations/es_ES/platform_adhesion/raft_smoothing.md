Suavizado de la balsa
====
Con este ajuste, las esquinas interiores de la balsa pueden hacerse más suaves. El ajuste especifica el radio de un arco. Todas las esquinas interiores que sean más agudas que el radio del arco especificado se suavizarán para tener el radio del arco.

<!--screenshot {
"image_path": "raft_smoothing_0mm.png",
"models": [{"script": "question_stick_clip.scad"}],
"camera_position": [0, 97, 191],
"settings": {
    "adhesion_type": "raft",
    "raft_smoothing": 0
},
"layer": 509,
"colours": 64
}-->
<!--screenshot {
"image_path": "raft_smoothing_5mm.png",
"models": [{"script": "question_stick_clip.scad"}],
"camera_position": [0, 97, 191],
"settings": {
    "adhesion_type": "raft",
    "raft_smoothing": 5
},
"layer": 509,
"colours": 64
}-->
![Sin suavizado](../images/raft_smoothing_0mm.png)
![Radio de 5 mm](../images/raft_smoothing_5mm.png)

El término técnico para esto es una [operación de cierre morfológico](https://en.wikipedia.org/wiki/Closing_(morphology\)). Todos los agujeros más pequeños que el radio especificado se cerrarán. Las esquinas interiores más agudas ya no se harán tan agudas.

La función de este ajuste es hacer la balsa más rígida. Cuando se conectan varias piezas a través de conexiones finas, la balsa puede doblarse en esos lugares. Esto las hace menos rígidas y menos resistentes a la deformación. Aumentar este ajuste hará que las piezas separadas estén mejor conectadas, haciendo que la balsa sea más fuerte. La superficie de la balsa será mayor, por lo que la balsa se pegará mejor. Además, la balsa tendrá una circunferencia más pequeña en total, reduciendo los lugares donde puede comenzar el alabeo. En total, debería haber menos alabeo.

Sin embargo, el volumen total de la balsa también aumentará. Esto utiliza más material y toma más tiempo para imprimir, sobre todo porque la balsa se imprime normalmente muy lentamente. término para esto es una [operación de cierre morfológico](https://en.wikipedia.org/wiki/Closing_\(morphology\)). Todos los agujeros más pequeños que el radio especificado se cerrarán. Las esquinas interiores más agudas ya no se harán tan agudas.

La función de este ajuste es hacer la balsa más rígida. Cuando se conectan varias piezas a través de conexiones finas, la balsa puede doblarse en esos lugares. Esto las hace menos rígidas y menos resistentes a la deformación. Aumentar este ajuste hará que las piezas separadas estén mejor conectadas, haciendo que la balsa sea más fuerte. La superficie de la balsa será mayor, por lo que la balsa se pegará mejor. Además, la balsa tendrá una circunferencia más pequeña en total, reduciendo los lugares donde puede comenzar el alabeo. En total, debería haber menos alabeo.

Sin embargo, el volumen total de la balsa también aumentará. Esto utiliza más material y lleva más tiempo de impresión, especialmente porque la balsa se imprime normalmente muy lentamente.