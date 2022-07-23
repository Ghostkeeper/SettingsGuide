Pasos de relleno necesarios
====
El relleno gradual reduce la cantidad de relleno utilizado, reduciendo la densidad de relleno en las capas inferiores. Esto ahorra tiempo de impresión y material, sin reducir mucho la calidad de la superficie. El propósito principal del relleno cuando se imprime para obtener calidad visual es apoyar la superficie superior. Esta característica enfoca el relleno a ese propósito solamente.

Este ajuste indica en cuántos pasos se reduce la densidad del relleno. En cada paso, la densidad de relleno se reduce a la mitad. Por ejemplo, comenzando con un porcentaje de relleno del 20% y dos pasos graduales de relleno, la densidad de relleno de las partes inferiores será del 10% y del 5%, respectivamente.

<!--screenshot {
"image_path": "gradual_infill_disabled.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
    "wall_line_count": 0,
    "bottom_layers": 0,
    "gradual_infill_steps": 0
},
"colours": 16
}-->
<!--screenshot {
"image_path": "gradual_infill_step_height_large.png",
"models": [{"script": "curved_top.scad"}],
"camera_position": [0, 137, -62],
"settings": {
    "wall_line_count": 0,
    "bottom_layers": 0,
    "gradual_infill_steps": 3,
    "gradual_infill_step_height": 5
},
"colours": 16
}-->
![Relleno normal](../images/gradual_infill_disabled.png)
![3 pasos de relleno gradual](../images/gradual_infill_step_height_large.png)

**La marca de verificación "Relleno gradual" en el modo recomendado establece esta configuración a 5 pasos y aumenta la densidad de relleno al 90%. Esto provoca una densidad muy alta en la parte superior (90%) y una densidad muy baja en la parte inferior de su impresión (2,8%).**