This setting determines the angle of the slope at which the conical support gets printed.

![An angle of 30 degrees](../images/support_conical_enabled.png)
![An angle of 10 degrees](../images/support_conical_angle_10.png)
![An angle of -10 degrees, causing the base to be wider](../images/support_conical_angle_neg10.png)

The conical support angle is the most major trade-off between the stability of support and how much support is generated.

Using a large angle will make the support very thin for a large portion of its height. This saves a lot of support material and printing time. When lots of support material is needed, this can save a lot of time and material, as upwards to half of the support is left out. However, since the support becomes very thin at the bottom, the support may also become less stable, increasing the chance of the print to fail. You can increase the [minimum width](support_conical_min_width.md) to guard against this.

Using a negative angle will make the support wider towards the bottom, shaped like a volcano. If your print has tiny features high up that need supporting, they will normally produce very tall [towers](../support/support_use_towers.md) that are prone to falling over during the print. With a negative angle these tall, thin support structures will be made wider at the bottom. This gives them some added stability. However, it will take longer to print this support since it requires more material. An angle of about -5° is normally enough to give even the tallest, thinnest support structures enough stability. If your material tends to ooze a lot during travel moves, a greater negative angle will be required because the structure will get pushed more due to blobs on the support.