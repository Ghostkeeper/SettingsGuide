Angle de diamètre des branches de support arborescent
====
Les branches du support des arbres sont plus larges vers le bas qu'elles ne le sont en haut. Cela garantit que les branches restent stables quelle que soit la hauteur du support. Avec ce réglage, vous pouvez contrôler la vitesse à laquelle le support s'élargit.

![La forme d'une branche avec un angle de diamètre de 5°](../../../articles/images/support_tree_branch_diameter_1_4mm_5.png)
![La forme d'une branche avec un angle de diamètre de 10°](../../../articles/images/support_tree_branch_diameter_angle_10.png)

Plus l'angle est grand, plus le bas du support de l'arbre sera large, surtout avec les grands modèles. Cela a plusieurs effets :
* Le fond plus large rend le support plus difficile à renverser. Cela augmente la fiabilité du support d'arbre.
* Le fond plus large nécessite plus de matière et de temps pour l'impression.
* L'angle du support s'ajoute à l'angle maximum (support_tree_angle.md) auquel les branches peuvent surplomber, de sorte que des valeurs très élevées peuvent également rendre le support moins solide dans certains cas.
* Les branches les plus larges ont plus de mal à naviguer dans le maillage, ce qui rend plus difficile l'accès à certaines parties du surplomb depuis la plaque de construction. Par conséquent, le support peut devoir reposer sur le modèle plutôt que sur la plaque de construction, ce qui augmente la quantité de cicatrices.
* L'évitement des collisions de l'arbre est plus difficile à calculer pour Cura, ce qui augmente le temps de tranchage. Il est possible de remédier à ce problème en augmentant le paramètre [Résolution de collision du support arborescent](support_tree_collision_resolution.md), mais cela réduit également l'intégrité structurelle du support de l'arbre.

En général, vous voudrez que l'angle soit tel que le support de l'arbre soit juste assez large pour se supporter à n'importe quelle hauteur sans devenir trop branlant.