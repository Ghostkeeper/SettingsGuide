Spaghetti Maximum Infill Angle
====
This setting configures the maximum overhang angle under which the material will reach when the infill material is deposited next to it. If a spot won't be filled with the proper density due to this limit, additional [steps](spaghetti_infill_stepped.md) will be introduced along the height of the infill volume to make sure those places are properly reached.

If the spaghetti infill is intended to be used as flexible infill, this setting should probably be set fairly high. Increasing this setting will cause more steps to be introduced to reach under shallow roofs. Since spaghetti infill doesn't tend to expand very far in horizontal directions, adding additional steps helps to push material underneath those shallow roofs.

If the spaghetti infill is intended to be used with a cast material, this setting may be lowered significantly. Since the cast material is liquid, it can reach very far underneath surfaces. Do not set it to 0° yet though, since most casting material has some viscosity. You may still want to cast some underneath some shallow roofs in order to make sure the cast follows its shell completely. 