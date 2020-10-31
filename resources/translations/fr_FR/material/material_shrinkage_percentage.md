Taux de contraction (Scaling Factor Shrinkage Compensation)
====
<!--if cura_version >= 4.8-->Ce réglage permet de mettre à l'échelle le modèle avant de le découper automatiquement. L'objectif est de compenser tout rétrécissement qui se produit lorsque l'impression refroidit à température ambiante. En rendant l'impression légèrement plus grande que ce qui est souhaitable, le résultat final pourrait être plus précis par rapport aux dimensions originales du modèle d'entrée. Ce facteur d'échelle est appliqué de la même manière à toutes les dimensions (X, Y et Z).

La scène entière est mise à l'échelle à partir de son centre. Lors de l'impression de plusieurs modèles, tous sont mis à l'échelle à partir du même point d'origine. Cela vous permet de positionner ces modèles très près les uns des autres, sans qu'ils ne se chevauchent lors de l'impression finale. Les zones de collision des modèles sont mises à l'échelle, de sorte que vous pouvez voir exactement où votre impression va se terminer. Cela vous évitera également de placer les modèles dans la scène à des endroits où ils entreraient en collision avec des éléments de l'impression ou de l'imprimante, comme la tour d'impression ou les clips du plateau d'impression.

Un facteur de 100 % n'entraînera aucune mise à l'échelle. Un facteur d'échelle légèrement supérieur à 100 % est approprié pour de nombreux matériaux d'ingénierie tels que l'ABS ou le polypropylène. Un facteur d'échelle inférieur à 100 % indiquerait que le matériau se développe en refroidissant, comme une mousse peut-être.

Les données purement chimiques sur le rétrécissement d'un matériau entre la température d'impression et la température ambiante ne suffisent pas à prédire une bonne valeur pour ce paramètre, car le processus d'impression influence également le rétrécissement. Lorsqu'il est extrudé en ligne, le plastique est étiré dans le sens de la longueur de la ligne, et se rétrécit davantage dans cet axe. Le rétrécissement n'est pas uniforme, mais ce réglage n'applique qu'un facteur d'échelle uniforme dans toutes les directions. Pour obtenir des résultats précis, vous devez appliquer le facteur d'échelle sur l'axe qui est le plus important pour votre application. S'il y a beaucoup de longues lignes droites le long de la dimension la plus importante, le facteur d'échelle devra être plus important.

Si le facteur d'échelle est supérieur à 100,5 % et que vous imprimez quelque chose de grand, Cura affichera un avertissement que vous pourriez commencer à avoir de la [déformation](../troubleshooting/warping.md).<!--endif-->

<!--if cura_version < 4.8:This is a descriptive setting, letting Cura know how much the material shrinks when it cools down from the printing temperature to room temperature.

This setting is currently not used for slicing. It is currently only used to display a warning to the user when printing large things if the shrinkage ratio is larger than 0.5%.
-->

*Ce paramètre n'est pas visible dans la liste des paramètres. Il s'agit seulement d'un réglage interne qui doit être écrasé par le profil matériau.*
