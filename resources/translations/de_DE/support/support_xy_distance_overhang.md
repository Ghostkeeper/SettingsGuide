X/Y-Mindestabstand der Stützstruktur
====
Wenn der Z-Abstand des Supports gegenüber dem X/Y-Abstand bevorzugt wird, darf der horizontale Abstand zwischen Support und Modell kleiner werden als die Einstellung [X/Y-Abstand der Stützstruktur](support_xy_distance.md), um den erforderlichen [Z-Abstand der Stützstruktur](support_z_distance.md) zu erfüllen.

Diese Einstellung definiert einen minimalen X/Y-Abstand, der unabhängig vom Z-Abstand eingehalten werden muss. Dieser minimale X/Y-Abstand hat wiederum Vorrang vor dem Z-Abstand.

![Der minimale X/Y-Abstand kommt zum Tragen, wenn der Z-Abstand einen sehr kleinen X/Y-Abstand zur Folge hätte.](../../../articles/images/support_z_overrides_xy.svg)

Wenn Sie diese Einstellung erhöhen, verringert sich die Wahrscheinlichkeit, dass die Stütze das Modell seitlich trifft und dort eine unnötige Narbe hinterlässt. Außerdem lässt sich der Support dann leichter entfernen. Beachten Sie jedoch, dass dies nur bei mittelstarken Überhängen zum Tragen kommt, bei denen der Überhang normalerweise ohnehin gestützt werden muss. Eine Erhöhung dieser Einstellung führt auch dazu, dass der Überhang stärker durchhängt, wodurch sich seine Oberflächenqualität verringert.