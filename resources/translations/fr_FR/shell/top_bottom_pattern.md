Motif du dessus/dessous
===

Ce paramètre vous permet de choisir comment les surfaces supérieure et inférieure se remplissent de matériau. Plusieurs motifs d'impression différents sont disponibles, mais les motifs sont ici plus limités que pour le remplissage. Seuls les motifs qui créent des couches solides sont disponibles.

Lignes
---
![Lignes](../../../articles/images/top_bottom_pattern_lines.png)

Le schéma de base trace des lignes droites sur la surface. Ces lignes sont orientées par défaut de telle sorte qu'elles soient bien soutenues par le remplissage et le support. La direction des lignes alterne entre les couches.
* Fournit une belle qualité de surface.
* Très rigide dans les directions où les lignes sont tracées.
* Adhère fortement aux murs, créant des parties relativement solides.

Concentrique
----
![Concentrique](../../../articles/images/top_bottom_pattern_concentric.png)

Le motif concentrique continue à dessiner des contours vers l'intérieur du modèle.
* Egalement fort dans toutes les directions.
* Empêche la création de poches d'air et d'espaces. Il est plus facile de créer des objets étanches avec ce modèle.
* Grande qualité de surplomb, car les lignes ont tendance à très bien se recouper.
* Si la pièce est circulaire, cela peut créer un point désagréable au centre où les contours convergent.
* La qualité de la surface est loin d'être idéale.

Zigzag
---
![Zigzag](../../../articles/images/top_bottom_pattern_zigzag.png)

Le motif en zigzag est très similaire au motif des lignes, mais au lieu de terminer les lignes dans les murs, il continuera à s'extruder vers la ligne de peau suivante.
* Fournit une grande qualité de surface.
* Très rigide dans les directions où les lignes sont tracées.
* Garde le taux d'extrusion plus constant, ce qui améliore la consistance de la surface pour les matériaux qui s'extrudent plus difficilement.
* Ne colle pas aussi bien aux murs que le dessin des lignes. L'effet du [pourcentage de chevauchement de la couche extérieure](skin_overlap.md) est réduit. Cela rend la pièce plus faible et réduit la qualité des débordements.


