This setting will transform your model such that it doesn't have any overhang any more. It will place extra material underneath any overhang and print that as if it were part of the model.

![A tower with some overhanging pieces](images/conical_overhang_enabled_disabled.png)
![The overhang is made printable](images/conical_overhang_enabled_enabled.png)

Underneath all overhanging pieces some material is placed that gradually grows smaller further downwards. In many cases the overhang will be sloped towards the object itself. The slope at which the overhang is made to grow towards the object is determined by the [model angle](conical_overhang_angle.md).

This setting can be an easy way to prevent needing any support. It is particularly effective when printing models with somewhat rough surfaces or relief on the sides. Those small pieces of overhang would normally droop down and produce loose strands of disconnected plastic strings. They might be supported with some support, but this can be costly in printing time and will still leave some scarring. If this setting is enabled, the overhang will be smoothed down towards the model. It'll appear as if that was how it was intended to be printed.

If the overhang protrudes farther from the main body than its width, this might still produce some overhang in the form of a line. This happens because the protrusion is then shrunk infinitely thin, causing it to disappear. If this occurs, you can consider whether it might still be necessary to print support. In the case of the images above, this happens with the small blocks on the side of the tower, but it is so small that simple bridging will likely allow it to hang over fine.