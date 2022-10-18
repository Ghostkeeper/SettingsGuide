Desviación máxima del área de extrusión
====
Cuando se imprimen líneas con anchos variables, es común tener una línea que debe hacerse gradualmente más delgada hacia uno de sus puntos finales. Este ajuste determina el tamaño del paso en el que estas líneas se hacen más finas o más anchas, controlando lo cerca que deben permanecer las líneas del área que deberían cubrir idealmente.

<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_high.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.5,
	"meshfix_maximum_extrusion_area_deviation": 2000
},
"colour_scheme": "line_width",
"colours": 128
}-->
<!--screenshot {
"image_path": "meshfix_maximum_extrusion_area_deviation_low.png",
"models": [{"script": "twisted_triangular_hole.scad"}],
"camera_position": [0, 0, 60],
"settings": {
	"meshfix_maximum_resolution": 0.05,
	"meshfix_maximum_extrusion_area_deviation": 20
},
"colour_scheme": "line_width",
"colours": 128
}-->
![Resolución más baja cuando se permite una desviación alta](../images/meshfix_maximum_extrusion_area_deviation_high.png)
![Suavizar el ancho de línea cuando se requiere una desviación baja](../images/meshfix_maximum_extrusion_area_deviation_low.png)

Los comandos de g-code no pueden ordenar a la impresora que imprima una línea con un ancho variable. Debe imprimir líneas con una anchura fija. Cura puede dividir una línea en múltiples segmentos con un ancho que cambia gradualmente. Sin embargo, esto añade muchos segmentos de línea a la impresión. La CPU de la impresora puede no ser capaz de seguir el ritmo de todas estas instrucciones durante la impresión. Con este ajuste, se elige el nivel de detalle de los segmentos de línea de ancho variable. Una mayor resolución (reducción de la desviación) resulta en líneas más precisas en teoría, pero también aumenta la cantidad de instrucciones en gran medida.

Aunque en la vista de capas queda bien que el ancho de una línea cambie gradualmente, esto no tiene prácticamente ningún efecto en la impresión real. Las impresoras 3D físicas no ajustan su velocidad de flujo con la suficiente precisión como para ver alguna mejora al aumentar la resolución aquí. En circunstancias normales, este ajuste debería ser lo suficientemente alto como para que nunca sea un factor limitante en la resolución del g-code. De esta manera, se minimiza la posibilidad de que el búfer se quede corto.