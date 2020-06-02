Vitesse d’impression de la couche initiale
====
Ce paramètre permet d'ajuster la vitesse d'impression de la couche inférieure du modèle.

Le réglage de ce paramètre permet d'ajuster la vitesse des mouvements d'extrusion dans la première couche, mais pas les mouvements de déplacement. Pour cela, ajustez le paramètre [Vitesse de déplacement de la couche initiale](speed_travel_layer_0.md). Même si les parois, la peau et le support peuvent normalement être imprimés à des vitesses différentes, ils ne le peuvent pas pour la couche initiale. Tous seront imprimés à la vitesse indiquée dans ce paramètre. Par défaut, ce paramètre influence le paramètre [Vitesse d'impression de la jupe/bordure](skirt_brim_speed.md), mais il peut toujours être ajusté séparément. La [vitesse de la couche de base du radeau](../platform_adhesion/raft_base_speed.md) n'est pas affectée.

La réduction de la vitesse d'impression de la couche initiale améliorera l'adhérence entre le modèle et le plateau d'impression. En effet, le matériau reste plus chaud plus longtemps et peut ensuite s'écouler plus longtemps. Cela réduit les contraintes internes dans le matériau et augmente la surface de contact, deux facteurs qui augmentent l'adhérence.
