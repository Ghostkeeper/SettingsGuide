Distance X/Y minimale des supports
===

Si la distance Z du support est préférée à la distance X/Y, la distance horizontale entre le support et le modèle peut devenir plus petite que le paramètre [Support X/Y Distance](./support_xy_distance.md) pour satisfaire à la [Support Z Distance](./support_z_distance.md) requise.

Ce paramètre définit une distance X/Y minimale qui doit être respectée quelle que soit la distance Z. Cette distance X/Y minimale est de nouveau prioritaire par rapport à la distance Z.

![La distance minimale X/Y est prise en compte si la distance Z signifie que la distance X/Y deviendrait très petite](../images/support_z_overrides_xy_fr.svg)

En augmentant ce paramètre, on réduit le risque que le soutien frappe le modèle sur le côté, laissant une cicatrice là où elle n'est pas nécessaire. Cela facilite également le retrait du support. Gardez toutefois à l'esprit que cette option n'est efficace que pour les porte-à-faux de hauteur moyenne, là où le porte-à-faux doit normalement être soutenu, et qu'elle est donc censée toucher le support à cet endroit. En augmentant ce réglage, le porte-à-faux s'affaisse davantage, ce qui réduit sa qualité de surface.
