Modo de peinado
====
El peinado es la práctica de evitar cruzar las paredes de la impresión cuando se viaja de un lugar a otro. Cruzar las paredes tiende a dejar una cicatriz en la superficie donde una boquilla caliente salió o entró en el volumen de la impresión, por lo que es generalmente indeseable.

El peinado solo hace que la boquilla evite las paredes cuando viaja por el interior de la malla. Sin embargo, también permite la función [Avoid Printed Parts While Traveling](travel_avoid_other_parts.md), que hace que la boquilla evite los objetos mientras está fuera del volumen también.

<!--screenshot {
"image_path": "retraction_combing_off.png",
"models": [
    {
        "script": "safety_lock.scad",
        "scad_params": ["length=40"]
    }
],
"camera_position": [0, 0, 120],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_combing": "off"},
"minimum_layer": 2,
"colours": 64
}-->
<!--screenshot {
"image_path": "retraction_combing_on.png",
"models": [
    {
        "script": "safety_lock.scad",
        "scad_params": ["length=40"]
    }
],
"camera_position": [0, 0, 120],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_combing": "all"},
"minimum_layer": 2,
"colours": 64
}-->
![Peinado desactivado, el movimiento de desplazamiento cruza las paredes de la huella](../images/retraction_combing_off.png)
![Peinado activado, se realiza un desvío para evitar cruzar las paredes](../images/retraction_combing_on.png)

Si hay un camino a través del objeto desde la ubicación inicial hasta la final sin chocar con ninguna pared, este camino se tomará sin hacer una retracción. Si la ubicación inicial y la final están en caminos completamente separados, la boquilla se moverá primero a la posición en la que las dos partes estén más juntas, luego opcionalmente se retraerá (si [retraction_enable.md)), viajará a la ruta objetivo, opcionalmente se desretraerá, y luego se moverá a través de la nueva parte hasta su destino final. En ambas partes evitará chocar con las paredes mientras se desplaza por el interior. Al viajar de una parte a otra sólo evitará las partes cuando el ajuste [Evitar partes impresas mientras viaja](travel_avoid_other_parts.md) esté activado.

El objetivo del peinado es evitar atravesar las paredes del objeto, reduciendo la cantidad de cicatrices en la superficie. También reducirá el encordado que es visible en el exterior, ya que mientras se realiza el movimiento de desplazamiento seguirá rezumando, pero este rezumado se sitúa en el interior del modelo. Sin embargo, el peinado también aumentará la longitud del movimiento de desplazamiento. A veces es necesario dar un gran rodeo.

Estas son las opciones en el desplegable de este ajuste:
* **Apagado**: El peinado está desactivado. Los movimientos de desplazamiento siempre irán directamente a su ubicación de destino. Si este no choca con ninguna pared, no se retraerá.
* **Todos**: La boquilla no chocará con ninguna pared mientras se desplaza por el interior de la impresión, como se ha descrito anteriormente.
<!--si cura_version >= 4.12-->* **No en la superficie exterior**: Además de rodear las paredes, la boquilla evitará también la capa más alta y la más baja del forro. Estas son las capas visibles donde se podría ver una cicatriz en la superficie si la boquilla pasara por encima de ellas. Si no es posible evitar la superficie, se hará una retracción.
* **No en el forro**: La boquilla evitará golpear cualquier forro, si es posible. Aunque esta opción todavía está disponible desde versiones anteriores de Cura, provoca retracciones innecesarias y recorridos más largos en comparación con No en la superficie exterior, porque evita las capas de forro aunque la cicatriz no sería visible en el exterior.<!--endif-->
<!--if cura_version < 4.12:* **No en el forro**: La boquilla evitará golpear el forro Esto puede reducir las cicatrices en la parte superior de la impresión haciendo que la boquilla vaya a lo largo de las paredes en lugar de cortar a través del forro. Sin embargo, en algunos casos la boquilla no podrá escapar y tendrá que hacer una retracción, donde de otra manera habría cortado el forro.-->
* **Relleno interior**: El modo más estricto de todos, este sólo permite peinar a través del relleno. Esto hace que evite golpear las paredes interiores así como las exteriores, y también evita golpear el forro. Si la boquilla golpea las paredes interiores, a veces puede seguir siendo visible en el exterior porque el radio exterior de la boquilla puede ser más ancho que las paredes. Esto evita ese efecto. Sin embargo, tendrá que hacer aún más retracciones porque a menudo no habrá un camino disponible.