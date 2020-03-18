Flux en spaghettis
===

Ce réglage permet d'ajuster directement la densité de la garniture de spaghettis.

Normalement, lors de l'impression d'un remplissage, le réglage [densité de remplissage](../infill/infill_sparse_density.md) n'affecte que la [distance entre les lignes de remplissage](../infill/infill_line_distance.md). Comme la [largeur de la ligne de remplissage](../resolution/infill_line_width.md) reste la même mais que les lignes sont plus rapprochées, l'augmentation de la densité de remplissage a pour effet qu'une plus grande partie du volume de remplissage est remplie de matériau à la fin.

Cela fonctionne différemment si [spaghetti infill](./spaghetti_infill_enabled.md) est activé. La distance entre les lignes de remplissage permet non seulement d'ajuster la distance entre les lignes de remplissage, mais la largeur de la ligne sera également ajustée afin d'obtenir la densité souhaitée, comme spécifié par ce paramètre. Ce paramètre spécifie exactement la fraction du volume total de remplissage qui sera remplie de matériau. Si l'on augmente ce paramètre, les lignes deviennent plus larges.

Lorsque l'on utilise des spaghettis pour produire des remblais souples, ce réglage détermine essentiellement la rigidité du matériau de remplissage. En réduisant le débit, on obtient un matériau de remplissage plus souple, tandis qu'en augmentant le débit, on obtient un matériau de remplissage plus rigide. Cependant, une réduction excessive du débit empêche le matériau de remplissage d'être également réparti. Il aura tendance à tomber vers le bas du volume et à produire des tas de spaghettis qui n'ajouteront pas à la rigidité du dessus. 

Lorsque l'on utilise un remplissage de spaghettis pour couler du matériau, ce réglage devrait probablement être proche de 100% afin de remplir complètement le modèle de matériau. Cependant, vous pouvez toujours l'ajuster légèrement si votre matériau a tendance à se contracter ou à se dilater en prenant.

**Ce paramètre est toujours multiplié par le paramètre [Débit de remplissage](../material/infill_material_flow.md).**


