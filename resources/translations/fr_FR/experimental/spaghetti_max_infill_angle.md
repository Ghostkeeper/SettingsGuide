Angle maximal de remplissage en spaghettis
====
Ce paramètre configure l'angle de surplomb maximal que le matériau atteindra lorsque le matériau de remplissage sera déposé à côté de lui. Si un endroit ne peut être rempli avec la densité appropriée en raison de cette limite, des [marches supplémentaires](spaghetti_infill_stepped.md) seront introduites le long de la hauteur du volume de remplissage pour s'assurer que ces endroits sont correctement atteints.

Si le remplissage de spaghetti est destiné à être utilisé comme remplissage flexible, ce paramètre devrait probablement être fixé à un niveau assez élevé. Si vous augmentez ce réglage, il faudra introduire davantage de marches pour atteindre les toits peu profonds. Comme le remplissage spaghetti n'a pas tendance à s'étendre très loin dans les directions horizontales, l'ajout de marches supplémentaires aide à pousser le matériau sous ces toits peu profonds.

Si le spaghetti de remplissage est destiné à être utilisé avec un matériau coulé, ce réglage peut être considérablement abaissé. Comme le matériau coulé est liquide, il peut atteindre de très grandes distances sous les surfaces. Cependant, ne le réglez pas encore à 0°, car la plupart des matériaux de coulée ont une certaine viscosité. Vous pouvez toujours en couler sous certains toits peu profonds afin de vous assurer que le matériau coulé suit complètement sa coque. 
