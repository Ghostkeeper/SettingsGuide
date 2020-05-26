Direction de ligne de remplissage du support
====
Le modèle de support est normalement orienté de telle sorte que les lignes sont perpendiculaires à la plupart des choses qu'il supporte. De cette façon, la distance que le matériau supporté doit franchir est réduite au minimum. Avec ce réglage, l'orientation des lignes de support peut être personnalisée.

![Un angle de 0°](../../../articles/images/support_infill_angle_0.png)
![Un angle de 30°](../../../articles/images/support_infill_angle_30.png)

Si les [Directions de la ligne supérieure/inférieure](../shell/skin_angles.md) ont été ajustées, il est sage de régler l'angle du support en conséquence, de sorte qu'il soit toujours perpendiculaire aux lignes de la face inférieure de l'impression. Cela permet à ces lignes du bas de reposer correctement sur le support, plutôt que de tomber entre les lignes du support. Ceci est particulièrement important pour les lignes et les zigzags [Motif du support](support_pattern.md) où il y a de longues lignes droites entre les lignes de support qui n'offrent aucun support.

<!--if cura_version >= 4.3-->**Ce paramètre permet de saisir plusieurs angles, qui alternent de manière similaire au paramètre [Sens de ligne de remplissage](../infill/infill_angles.md).**<!--endif-->
