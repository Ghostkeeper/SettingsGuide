Enable Conical Support
====
If this setting is enabled, the support structure will no longer be completely vertical on the sides. The support will get a conical shape, getting either smaller or larger towards the bottom.

![The support gets smaller towards the bottom](../images/support_conical_enabled.png)
![The support gets larger towards the bottom](../images/support_conical_angle_neg10.png)

The support itself will slope with a certain [angle](support_conical_angle.md). With negative angles, the support will get larger towards the bottom, making the support significantly more stable. With positive angles, it will get smaller towards the bottom. This saves a lot of material and printing time. To prevent the support from getting unstable, a [minimum width](support_conical_min_width.md) can be defined for the support as well.

Conical support is the most powerful parameter for the weigh-off between printing time and the stability of support. There are two main use cases for conical support:
* To save material and printing time. Conical support can easily save you half of the material required for support, and by extension half of the time spent on printing it. This is especially effective if there are large volumes of support, for large and tall prints.
* To make the support more stable using a negative angle. If your print has tiny features high up that need supporting, they will normally produce very tall [towers](../support/support_use_towers.md) that are prone to falling over during the print. With conical support, these tall, thin support structures can be made wider at the bottom. This gives them some added stability. However, it will take longer to print this support since it requires more material.

When the [Support Placement](../support/support_type.md) is set to place support only on the build plate, conical support allows reaching around the model to still support the model in places that are above other parts of the model. The support will still only rest on the build plate, but due to its shape can now reach the overhang areas in corners that would otherwise not be supported.

This feature is a somewhat simpler and less intrusive version of [Tree Support](support_tree_enable.md). Tree support has many of the same advantages as conical support. However Tree Support uses a completely different algorithm and is allowed more freedom in how the support is constructed, while conical support stays more true to the ordinary support generation algorithm. This means that the settings for ordinary support tend to work better when used with conical support, but will need to be adjusted significantly for tree support. Tree support tends to save more on material and printing time while retaining print reliability.