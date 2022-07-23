Ancho de línea de la pared exterior
====
El ancho de la línea de la pared exterior se puede ajustar por separado de las paredes interiores. Este ajuste indica la anchura de la línea de la pared exterior.

<!--screenshot {
"image_path": "wall_line_width_0.png",
"models": [{"script": "hive.scad"}],
"camera_position": [-31, -31, 147],
"settings": {
    "wall_line_count": 2,
    "wall_line_width_0": 0.8
},
"colours": 64
}-->
![El contorno de la pared exterior es mucho más ancho que el resto](../images/wall_line_width_0.png)

Se sabe que reducir la pared exterior a un ancho de línea ligeramente inferior al tamaño de la boquilla es beneficioso para la resistencia. La boquilla extruirá algo menos de material, pero su abertura se solapará con la pared interior adyacente. Esto hace que el material sea empujado por la pared previamente colocada en su lugar. Pero eso también hará que el plástico se fusione mejor con las paredes adyacentes. Esto permite que la pared exterior se fusione mejor con las paredes interiores, de modo que puedan combinar su resistencia. Esto mejora en gran medida la resistencia de las paredes.

La reducción del ancho de la línea de la pared exterior también permite que la boquilla imprima detalles más finos, porque la línea más fina se ajustará mejor a los detalles pequeños.

Aumentar el ancho de la línea de la pared exterior puede reducir el tiempo de impresión. Se puede conseguir una pared con un grosor similar con menos paredes interiores. La resistencia todavía se reducirá un poco porque la pared exterior no se fusionará tan bien con las paredes interiores.

<! --if cura_version>=5.0-->En piezas delgadas, el ancho de línea se ajustará automáticamente para que se ajuste al ancho local de la pieza allí. No es necesario asegurarse de que el ancho de la pieza es un múltiplo del ancho de la línea. El [Ángulo del umbral de transición de la pared](../shell/wall_transition_angle.md) determina dónde se ajusta automáticamente el ancho de línea en las esquinas agudas. El [Ancho mínimo de la línea de la pared](../shell/min_wall_line_width.md) determina hasta dónde se puede ajustar en cada dirección.<!--endif-->

<! --if cura_version<5.0:
Cómo hacer que las líneas se ajusten
----
Cuando se imprimen piezas delgadas, el ajuste de la configuración del ancho de la línea de la pared es una herramienta importante para obtener piezas precisas y fuertes. Cura sólo dibujará siempre contornos completos, por lo que si un contorno no se ajusta caerá un hueco en las paredes, lo que compromete enormemente la resistencia y la precisión de la pieza.

Cura intentará rellenar esos huecos entre paredes si [Rellenar huecos entre paredes](../shell/fill_perimeter_gaps.md) está activado, pero esa técnica es menos que ideal para formas arbitrarias y a menudo lleva mucho tiempo de impresión. Cuando dos paredes se solapan, la función [Compensar solapamientos de pared](../shell/travel_compensate_overlapping_walls_enabled.md) reducirá el ancho de la línea de la pared para asegurarse de que la pieza es dimensionalmente precisa, pero esto incurre en cambios de flujo que reducen la calidad y la fuerza de la impresión también.

Para un ajuste ideal, es necesario que la pieza sea un múltiplo exacto del ancho de la línea de la pared para que las paredes encajen con precisión dentro de la pieza. Si conoce el ancho de su pieza, esto se puede hacer fácilmente ajustando el ancho de las paredes. Primero, vea cuántos contornos quiere ajustar para que las líneas sigan teniendo un ancho razonable. Entonces podrá ver cuánto necesita ajustar el ancho de la línea de la pared para que las líneas encajen correctamente. Tenga en cuenta que puede ajustar el [Ancho de línea de la pared exterior](wall_line_width_0.md) y el [Ancho de línea de la pared interior](wall_line_width_x.md) por separado. Cuente cuidadosamente cuántas veces se dibujará cada tipo de pared para predecir el efecto de cambiar el ancho de la línea de pared.

Ajustar las líneas de pared es una habilidad importante para la impresión 3D que distingue a los operadores expertos de impresoras 3D del resto. Se requiere algo de práctica.