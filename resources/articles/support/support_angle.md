The overhang angle influences how much material is placed down to support the print. The angle indicates the minimum angle that gets supported.

**Reducing the value of this setting generates more support.**

![A low overhang angle generates more support](../images/support_angle_low.png)
![A high overhang angle generates less support](../images/support_angle_high.png)
![The supported areas are indicated in red](../images/support_angle_prepare_mode.png)

Reducing this setting makes the printer support more of the printed part, even surfaces that are steeper and won't sag much during printing. If the support is supporting parts that don't need to be supported, it'll increase the printing time and material usage unnecessarily and also create scars where the support touched the print.

However reducing the support angle is sometimes necessary to prevent the material from sagging too much. It generally improves the dimensional accuracy of the final part and makes the overhangs look better too.

Whenever working with support, it's a good idea to preview what the support looks like in the Preview stage. There you can see where it will actually generate support. Adjusting this setting is then one of the tools at your disposal to filter where precisely it will generate support.