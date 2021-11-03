Lightning Infill Overhang Angle
====
Lightning infill will only support the top side of the model from the inside where it overhangs. This setting determines the angle of overhang that gets supported by lightning inside from the inside of the model.

![Le surplomb jusqu'à 30° n'est pas soutenu.]((../../../articles/images/lightning_infill_support_angle_30.png)
![Jusqu'à 70° n'est pas soutenu, laissant seulement le sommet de la sphère soutenu.](../../../articles/images/lightning_infill_overhang_angle_70.png)

Increasing this angle will reduce the amount of infill generated. Less of the top surface will get supported, if it's not a very steep overhang. This saves time and material, but may also cause the top surface to sag in places. The result could be [pillowing](../troubleshooting/pillowing.md) or generally a rougher surface.

Contrary to the parent setting [Lightning Infill Support Angle](lightning_infill_support_angle.md), this setting doesn't influence the overhang in the infill pattern itself.
