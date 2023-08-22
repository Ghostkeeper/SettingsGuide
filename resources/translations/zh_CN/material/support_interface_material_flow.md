支撑接触面流量
====
此设置仅调整支撑接触面的流量速率。支撑接触面的流量速率可以与支撑的其余部分的流量速率分开调节。

调整支撑接触面过程的流量速率仅是解决挤出速率或模型与支撑之间的粘附问题的一种权宜之计。通过调整支撑界面的[走线宽度](../resolution/support_interface_line_width.md)或[行距](../support/support_roof_line_distance.md)也可以达到同样的效果，但调整流量速率可能更直观。

如果挤出速率有问题，最好查看[打印速度](../speed/speed_support_interface.md)、[温度](material_print_temperature.md)和[走线宽度](../resolution/support_interface_line_width.md)。也许在支撑接触面和层上的其他结构的流量速率之间存在太大的差异。可能是走线宽度太细，无法正确挤出。如果使用[不同材质](../support/support_interface_extrider_nr.md)打印界面，则常见的问题是打印界面的材料没有足够的时间开始正常流动。这可以通过使用[装填塔](../dual/prime_tower_enable.md)或增加[支持接触面的面积](../support/support_interface_offset.md)来解决。

如果支撑物太好地粘在模型上，调整[走线宽度](../resolution/support_interface_line_width.md)通常会更有效，因为它还可以使线更靠近以实现相同的支撑物填充密度。
