Tête de machine et polygone de ventilateur
====
Ce réglage indique à Cura quelle est la forme de votre tête d'impression, vue d'en haut. Cette fonction est nécessaire pour éviter les collisions lors de l'impression en mode [un à la fois](../blackmagic/print_sequence.md).

![Dimensions de la tête d'impression](../images/head_dimensions_fr.svg)

Ce paramètre contient une liste de coordonnées qui forment un polygone. Les coordonnées sont relatives à la "position" de la tête, par rapport à laquelle les buses sont également positionnées de manière relative.

Cura l'utilise pour créer une zone de collision autour des objets que vous imprimez en mode "un à la fois". Cette zone de collision vous empêche de placer les objets trop près les uns des autres de sorte qu'ils ne puissent pas être imprimés sans que la tête d'impression ne heurte le modèle précédemment imprimé. La zone de collision n'a cependant pas la même forme que la tête d'impression elle-même : il s'agira d'une coque convexe autour de la tête d'impression afin d'éviter les collisions lors des déplacements. Elle sera également rétrécie pour être symétrique. Par exemple, si la buse se trouve plus à gauche de la tête d'impression (comme dans l'image ci-dessus), la zone de collision sera rétrécie de manière à ce qu'un autre objet puisse être placé près du côté droit des objets précédemment imprimés. L'ordre dans lequel ces objets sont imprimés sera alors ajusté de manière à ce qu'ils puissent être imprimés sans collision.

*Comme il s'agit d'un réglage machine, il ne figurera normalement pas dans la liste des réglages normaux. Cependant, la taille de la tête d'impression peut être grossièrement notée dans la boîte de dialogue des paramètres de l'imprimante, qui se trouve dans la liste des imprimantes ajoutées dans la boîte de dialogue des préférences. Vous ne pouvez y spécifier que la position des côtés gauche, droit, supérieur et inférieur de la tête d'impression.*
