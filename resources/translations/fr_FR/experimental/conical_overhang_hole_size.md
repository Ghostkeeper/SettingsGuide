Surface maximale des trous en porte-à-faux
====
Étant donné que [Rendre le porte-à-faux imprimable](conical_overhang_enabled.md) supprime tout type de surplomb, tous les ponts seront automatiquement abaissés, fermant le surplomb en dessous. Cependant, si le surplomb est fermé de tous les côtés, il continuera à être abaissé jusqu'à ce que le surplomb fermé soit complètement rempli. En effet, tous les trous orientés vers le bas seront complètement remplis, même si le surplomb qui doit être retiré n'est qu'un petit point tout en haut.

Pour éviter cet effet, ce paramètre permet au surplomb de rester ouvert s'il est fermé de tous les côtés et plus petit qu'une certaine surface. Cela ne s'applique qu'aux trous. Les surplombs réguliers sur l'extérieur du modèle sont toujours étendus vers le bas pour conserver un angle raisonnablement imprimable.

![Un petit point en haut est autorisé à rester en surplomb, afin que ce trou ne soit pas rempli](../images/conical_overhang_hole_size.png)

Il est assez sûr de régler ce paramètre à plusieurs dizaines de millimètres carrés pour la plupart des modèles. S'il est réglé trop bas, le modèle sera modifié davantage, pour supporter des surplombs qui sont vraiment trop petits pour nécessiter un quelconque support. En revanche, s'il est réglé trop haut, il y aura des zones de surplomb importantes qui pourraient être difficiles à combler.

S'il y a de grandes zones de surplomb en raison de ce paramètre, il est préférable de commencer par [régler le pontage] (bridge_settings_enabled.md) avant d'essayer de modifier le modèle pour supprimer le surplomb.
