Preferencia de esquina de costura
====
Con este ajuste puede controlar cómo se colocarán las costuras en relación con las esquinas de su modelo.

Generalmente hay dos opciones para colocar la costura: oculta en una esquina interior, o expuesta en una esquina exterior. Ocultar la costura en una esquina interior es generalmente preferible, ya que la costura apenas será visible allí. Pero también es posible ponerla en una esquina exterior para poder cortar la costura con un cuchillo o lijarla con un poco de papel de lija, si se puede hacer algún tratamiento posterior en la pieza.

Estas son las opciones disponibles para este ajuste y sus efectos.
* **Ninguna:** No hay preferencia por las esquinas en absoluto. La costura se elegirá para que coincida con los requisitos de [Alineación de la costura en Z](z_seam_type.md) mejor.
* **Ocultar Costura:** Esto preferirá ocultar la costura en una esquina interior. Si la alineación de la costura Z se establece en "Esquina más pronunciada", siempre se elige la esquina más interna. Si se ajusta a "Más corta", se elige una esquina interior que esté cerca de la posición actual de la boquilla al iniciar el contorno.
* **Exponer Costura:** Esto preferirá exponer la costura en una esquina exterior. Si la Alineación de la Costura Z está ajustada a "Esquina más pronunciada", siempre se elige la esquina exterior más aguda. Si se ajusta a "Más corta", se elige una esquina exterior que esté cerca de la posición actual de la boquilla al iniciar el contorno.
* **Ocultar o Exponer Costura:** Esto colocará una costura en una esquina aguda, ya sea una esquina interior o exterior, siempre y cuando no esté en una pared plana.<!--if cura_version >= 4.2 -->
* **Ocultar inteligentemente:** Esto colocará la costura en una esquina aguda igual que "Ocultar o Exponer Costura", pero las esquinas interiores se eligen más a menudo que las exteriores si hay alguna esquina interior disponible en el contorno. Si no hay esquinas interiores, se elegirá una esquina exterior.