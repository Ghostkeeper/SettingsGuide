Umbral de apoyo de la piel del puente
====
Este parámetro permite ajustar la sensibilidad de la detección de las áreas puente. Las áreas puente se detectan en virtud de la porción del área de la piel que se apoya en algo de la capa anterior.

Para cada región disjunta de la piel, esto mirará cuánto de esa piel está apoyada por algo en la capa inferior. Si la región se apoya demasiado poco, se aplicará la técnica del puente a las regiones de la piel que no se apoyan.

La aplicación de la técnica del puente a la piel provoca cambios en la tasa de flujo y en la velocidad de impresión. Estos intentan ajustar la velocidad de salida del material por la boquilla, pero eso suele ser difícil de cambiar. Como resultado, habrá sobreextrusión en algunas partes de la impresión y subextrusión en otras, ya que el caudal intenta ajustarse. Por lo tanto, el ajuste de la tasa de flujo para un trozo muy pequeño de voladizo más que probablemente reducirá la calidad de la impresión en lugar de mejorarla.

Aumentar este ajuste hará que la técnica de puenteo se aplique a más partes pequeñas de voladizo, donde el puenteo es menos efectivo pero el caudal sigue interrumpido. Reducir este ajuste hará que la técnica de puenteo sólo se aplique en zonas de voladizo muy grandes. Esto no provocará tantos cambios de caudal, pero puede reducir la calidad del voladizo en las zonas de voladizo más pequeñas.