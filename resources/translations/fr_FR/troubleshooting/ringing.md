Ondulations
====
Les ondulations (parfois appelé "ghosting") est un effet où des ondulations apparaissent sur des surfaces par ailleurs plates à proximité de petits détails de cette surface. Les ondulations commencent à se produire juste après l'impression des petits détails.

![Ondulations sur la surface](../../../articles/images/ringing.jpg)

Causes
----
Les ondulations sont causées par les vibrations de votre imprimante 3D. Essayer d'éviter les ondulations, c'est réduire ces vibrations. Elles sont particulièrement prononcées si la tête d'impression se déplace dans l'une des fréquences de résonance du cadre de votre imprimante.

C'est l'une des choses que les imprimantes 3D plus coûteuses essaient généralement d'éviter avec un cadre plus rigide qui vibre moins. Elles ont un portique plus solide avec des barres et des tiges en acier trempé, ou fournissent un cadre entièrement fermé fait d'un matériau très rigide. Mais comme cela coûte cher, les modèles d'imprimantes 3D bon marché n'ont pas les moyens d'empêcher les vibrations. Les imprimantes équipées d'un tube Bowden ne présentent pas non plus autant d'ondulations, car la tête d'impression est beaucoup plus légère que celle d'une tête d'impression à entraînement direct (puisque le lourd moteur d'alimentation repose sur la tête d'impression).

Bien que les ondulations se manifeste horizontalement, les vibrations ne sont pas toujours horizontales. La vibration du plateau d'impression de haut en bas par rapport à la buse est également un effet très important, car la goutte de plastique est écrasée et devient plus large lorsque le plateau d'impression vibre plus près, ou plus fine lorsqu'elle vibre plus loin.

Solutions matérielles
----
Avant d'ajuster vos réglages dans Cura, il est bon de voir d'abord si vous pouvez améliorer votre matériel pour éviter les ondulations. Cela peut permettre d'améliorer globalement les résultats de l'impression sans avoir à sacrifier d'autres qualités de l'impression comme la résistance ou la productivité. Voici quelques éléments à prendre en considération :
* Ajoutez des amortisseurs sous votre imprimante. Vous pouvez utiliser des pieds en caoutchouc ou simplement placer l'imprimante sur un bloc de mousse souple. Cela empêchera les vibrations si la table vibre, et empêchera également l'imprimante de faire vibrer la table. Cela réduira le retour d'information que l'imprimante vibrante reçoit de la table, ce qui contribue à réduire les vibrations à haute fréquence.
* Serrer les courroies d'entraînement du portique. Si ces courroies ne sont pas tendues, l'élasticité de leur caoutchouc permet à la tête d'impression de vibrer.
* Si votre tête d'impression est équipée d'attaches flexibles, comme un tube Bowden, pensez à les fixer de manière à ce qu'elles ne puissent plus osciller. Les attaches fonctionnent bien pour les tubes Bowden si vous pouvez les attacher à quelque chose.
* Ajoutez plus de masse au cadre de votre imprimante 3D. Il sera ainsi plus difficile de déplacer le cadre en raison de son inertie accrue, et il sera donc plus difficile de le faire vibrer.
* Augmentez la rigidité du cadre de votre imprimante 3D avec des renforts ou des barres transversales supplémentaires. Vous pourriez les fabriquer avec des matériaux durables comme l'acier, mais si ce n'est pas possible, vous trouverez peut-être dans une quincaillerie un produit qui s'adapte avec un minimum d'ajustements. Vous pouvez également envisager d'imprimer ces renforts et ces traverses en 3D, mais sachez que la plupart des plastiques ne supportent pas bien l'application d'une force soutenue.

Les solutions de Cura
----
Si les solutions matérielles ne sont pas envisageables, vous pouvez également réduire l'effet d'ondulation grâce à certains ajustements des paramètres de Cura.

Comme les vibrations sont causées par l'accélération de la tête d'impression, les améliorations les plus importantes visent à réduire ces accélérations.
* La réduction de la [vitesse d'impression](../speed/speed_print.md)  maximale réduit la durée des accélérations.
* La réduction de la [vitesse d'accélération](../speed/acceleration_print.md) réduit directement l'accélération et diminue la force des vibrations.
* En impression 3D, [la saccade ou jerk](../speed/jerk_print.md) est un terme industriel qui désigne les changements instantanés de vitesse dans les virages. Cela signifie qu'il s'agit essentiellement d'essayer d'accélérer à l'infini afin d'éviter de devoir trop ralentir dans chaque virage. Cela entraîne des accélérations très élevées pendant de courtes périodes dans chaque virage. La réduction de la secousse peut alors aussi contribuer à réduire les vibrations. Au lieu d'une brève et forte accélération, elle accélère plus lentement et plus longtemps, ce qui réduit les vibrations à haute fréquence mais augmente les vibrations à basse fréquence.

Ces ajustements feront que votre impression prendra plus de temps. Mais vous pouvez aussi éviter les ondulations d'autres façons, en empêchant le type de mouvements qui les provoquent :
* Désactivez la technique de [remplissage des espaces](../shell/fill_perimeter_gaps.md) et n'[imprimez pas de parois fines](../shell/fill_outline_gaps.md), car ces techniques utilisent parfois de très petits segments de ligne et des déplacements supplémentaires. Si un mur est imprimé par la suite, l'imprimante vibrera encore un peu.
* Si votre imprimante déplace la plaque de construction de haut en bas plutôt que la tête d'impression, n'utilisez pas de [Retrait en Z](../travel/retraction_hop_enabled.md). Cela fait vibrer la plaque de montage de haut en bas longtemps après que le saut ait été effectué.

Vous pouvez également imprimer les [parois intérieures avant la paroi extérieure](../shell/outer_inset_first.md). Comme l'impression des parois ne provoque généralement pas autant de vibrations que les autres parties, cela permet à l'imprimante de cesser de vibrer avant que la paroi extérieure, si importante, ne soit imprimée.

Enfin, selon la géométrie de votre portique, les vibrations sont parfois absorbées différemment dans différentes directions. Une rotation de 45 degrés de votre pièce peut également vous aider. 
