自动温度
====
打印速度较快时，最好在稍高的温度下打印。这使得热塑性塑料更易流动，从而允许其更快地流出喷嘴开口。该设置根据材料流出喷嘴的平均流速自动调整温度。

要了解必须调整多少温度，请参考[流量温度图](material_flow_temp_graph.md)。流速的计算单位为立方毫米/秒。将其代入流动温度关系式中得到特定温度。该温度将被用作打印温度。启动此设定后，将不再使用普通的[打印温度](../material/material_print_temperature.md) 设定，而改用根据流量计算的温度。

此设定的目的是在打印中有较大的流量变化时，达到较佳的打印品质，减少挤出过度和挤出不足。一种常见的情况是皮肤与填充之间的边界。因为皮肤的印刷通常比填充慢得多，所以存在大量填充的层应该在稍高的温度下印刷，以便在填充的打印期间材料可以适当地挤出。

对于许多打印机，当在短时间内有许多温度变化时，调节打印机喷嘴中的温度的PID调节器倾向于过度反应。使用此设定时，可能会导致打印温度极不准确。

** 此设置当前在Cura的界面中不可见，无法激活。**