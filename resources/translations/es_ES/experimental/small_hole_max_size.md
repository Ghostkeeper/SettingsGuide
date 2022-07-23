Tamaño máximo de agujero pequeño
====
Los detalles pequeños de la impresión son a menudo muy críticos en cuanto a las dimensiones. Este ajuste hace que los agujeros pequeños de la impresión se impriman más lentamente para conseguir una mayor precisión.

Si un orificio circular tiene un diámetro inferior al valor de este ajuste, la velocidad a la que se imprime el perímetro de ese orificio se multiplicará por un factor de la [Small Feature Speed](small_feature_speed_factor.md) (reducido, normalmente). Para los agujeros que no son circulares, se imprimirán a una velocidad diferente si la circunferencia es menor que un círculo con el diámetro especificado aquí. Vea también [Small Feature Max Length](small_feature_max_length.md); ese es el ajuste que se utilizará realmente para el corte.

Un caso de uso común para esta característica es imprimir agujeros de tornillo en dimensiones muy precisas. Durante la impresión de agujeros pequeños, el cordón tiende a ser arrastrado junto con la boquilla en la esquina. Si la esquina es muy aguda, como en el caso de los agujeros pequeños, esto tiene el efecto de hacer el agujero más pequeño. Cuando se imprime más lentamente, este tirón se reduce porque el material tiene más tiempo para asentarse y porque el tirón mecánico es simplemente menor.

El aumento de este ajuste hace que se marquen más contornos como "característica pequeña". Una mayor parte de los agujeros en la impresión se imprimirá más lentamente. Esto hace que esos agujeros se impriman con más precisión, pero aumentará el tiempo de impresión.