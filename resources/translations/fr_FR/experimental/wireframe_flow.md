Débit de l'impression filaire
===

Ce réglage permet de régler le débit pendant l'impression avec la technique de l'impression au fil de fer. Cela sert simplement de multiplicateur sur la largeur de ligne et la hauteur de couche. Il détermine directement la quantité de matériau utilisée pour l'impression au fil de fer.

Ce réglage permet d'ajuster le débit pour l'ensemble de l'impression, mais le débit peut également être ajusté séparément pour les [parties horizontales](wireframe_flow_flat.md) ou les [connexions](wireframe_flow_connection.md).

L'impression filaire n'utilise pas la largeur de ligne ou la hauteur de couche pour déterminer la distance entre les lignes et les couches. Elle utilise uniquement la [hauteur](wireframe_height.md) et la [distance d'insertion](wireframe_roof_inset.md). Ainsi, au lieu d'ajuster le flux de l'impression au fil de fer, vous pouvez tout aussi bien ajuster les paramètres [Hauteur de la couche](../resolution/layer_height.md) ou [Largeur de ligne](../resolution/line_width.md), ou le [Débit](../material/material_flow.md). Cela aura le même effet. Toutefois, ces paramètres permettent de créer un profil d'impression avec un flux correct pour l'impression à fil sans influencer la qualité d'impression des impressions normales qui n'utilisent pas l'impression à fil.

L'augmentation du débit rend les fils plus épais. Cela rend le cadre plus rigide une fois qu'il est solidifié. Cependant, cela augmente également la masse thermique du cadre, ce qui rend la solidification des fils plus longue. Les fils s'affaissent et la fiabilité de l'impression s'en trouve réduite, car les fils peuvent alors ne plus se connecter correctement.
