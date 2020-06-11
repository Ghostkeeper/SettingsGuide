Longueur de la purge de la matière
====
Si l'imprimante doit changer le filament qui passe par une certaine buse, elle doit évacuer les restes de matière qui se trouvaient encore dans la chambre de la buse. Ce réglage détermine la quantité de matière utilisée pour rincer la matière précédente.

Cela ne s'applique qu'au moment où l'on passe à un autre type de matériau. Si le même type de matériau est rechargé (par exemple parce que la bobine précédente était vide), une [longueur différente](material_end_of_filament_purge_length.md) est utilisée.

**Ce paramètre n'est actuellement jamais visible dans l'interface de Cura. Il ne peut être défini que par les profils. Il n'est pas non plus utilisé par Cura pendant le tranchage. Cependant, les imprimantes qui comprennent le format de fichier de matériau de Cura peuvent l'utiliser pour configurer correctement leur procédure de changement de filament** Par un script de post-traitement, la commande `M600` peut être insérée dans l'impression, ce qui déclenchera un changement de filament.
