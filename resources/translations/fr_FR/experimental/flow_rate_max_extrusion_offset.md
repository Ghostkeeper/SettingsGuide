Décalage d'extrusion max. pour compensation du débit
===

La compensation du débit est une expérience similaire à la fonctionnalité [Linear Advance](http://marlinfw.org/docs/features/lin_advance.html) de Marlin. Le but de la compensation du débit est de compenser la sous-extrusion et la surextrusion lorsque le débit de la matière sortant de la buse change. Ce réglage limite la distance sur laquelle la matière sera rétractée ou poussée vers l'avant afin de compenser les changements de débit.

La compensation du débit déplacera le filament plus en avant par rapport à sa position initiale ou plus en arrière pendant l'impression. Ce réglage limite la distance sur laquelle le filament peut se déplacer par rapport à sa position initiale.

La compensation introduira des mouvements supplémentaires du filament tout au long de l'impression. Ces mouvements font que la tête d'impression ralentit de temps en temps pour déplacer le filament. Pour réduire cet effet, vous pouvez limiter la distance que le filament peut parcourir. Cela permet d'éviter que la tête d'impression ait besoin de ralentir pour que le chargeur puisse suivre. Cependant, cela rend la compensation du débit moins efficace.
