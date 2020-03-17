Pause d'essuyage
===

Avec ce réglage, la buse peut être mise en pause brièvement juste après la fin de la procédure d'essuyage.

La procédure d'essuyage est suffisamment longue pour un mouvement en mouvement. La buse se déplace sur le côté du volume du bâtiment et effectue un mouvement de va-et-vient, puis doit retourner à l'impression. Pendant ce temps, il y aura beaucoup de suintement et une [rétraction plus longue](./wipe_retraction_amount.md) peut être nécessaire. Après la rétraction, il y aura une période de temps après laquelle l'écoulement de la buse devra toujours commencer. Cette pause permet à la chambre de buse de revenir à la pression lorsque le matériau n'est pas rétracté à nouveau, permettant à la première ligne d'être imprimée correctement sans sous-extrusion importante.

Une pause trop longue provoquera l'apparition d'une goutte à l'emplacement de la buse. En fonction de la [commande d'impression](../infill/infill_before_walls.m), cela peut ne pas être significatif car le point peut apparaître à l'intérieur de l'impression où il n'est pas visible. Cependant, le matériau utilisé pour ce point ne sera pas utilisé pour les lignes imprimées suivantes, ce qui entraînerait une sous-extrusion à cet endroit. Ce paramètre nécessite un réglage soigneux.
