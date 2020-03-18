Distance de déplacement d'essuyage
====
Ce paramètre vous permet de définir la largeur des mouvements d'essuyage. La buse se déplacera sur cette distance pour [chaque mouvement d'essuyage](wipe_repeat_count.md).

Au départ, la buse sera placée juste au-delà de la brosse d'essuyage dans une [certaine coordonnée X](wipe_brush_pos_x.md). La distance indiquée dans ce réglage doit être telle que le déplacement de cette distance la place de l'autre côté de la brosse. Un déplacement trop important introduit des mouvements inutiles et peut entraîner le retour de la buse dans le volume de construction, ce qui peut l'amener à frapper inutilement le modèle si [les sauts en Z ne sont pas activés](wipe_hop_enable.md). Un déplacement insuffisant peut l'empêcher de frapper la brosse correctement.

La distance peut également être négative. La buse essuiera alors dans l'autre sens. En fonction de votre choix de [coordonnée X](wipe_brush_pos_x.md), cela peut être nécessaire pour essuyer dans la bonne direction.
