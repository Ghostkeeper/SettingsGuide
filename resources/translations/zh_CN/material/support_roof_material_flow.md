支撑顶板流量
====
此设置仅调整支撑顶板的流量。支撑顶板的流量速率可以与支撑件的其余部分的流量速率分开调节。

调整支撑顶板过程中的流量仅是解决挤出速率或模型与支撑之间粘附问题的一个权宜之计。通过调整支撑顶板的[走线宽度](../resolution/support_roof_line_width.md)或[行距](../support/support_roof_line_distance.md)也可以达到同样的效果，但调整流速可能更直观。

如果挤出速率有问题，最好查看[打印速度](../speed/speed_support_roof.md)、[温度](material_print_temperature.md)和[走线宽度](../resolution/support_roof_line_width.md)。也许在支撑顶板和层上的其他结构的流量速率之间存在太大的差异。可能是走线宽度太细，无法正确挤出。如果使用[不同材质](../support/support_interface_extrider_nr.md)打印界面，则常见的问题是打印界面的材料没有足够的时间开始正常流动。这可以通过使用[装填塔](../dual/prime_tower_enable.md)或增加[support roof area](../support/support_roof_offset.md)来修复。

如果支撑物与模型粘附得太好，则调整[走线宽度](../resolution/support_roof_line_width.md)通常会更有效，因为它还可以使线更靠近以实现相同的支撑填充密度。
