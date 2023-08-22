打印平台附着挤出器
====
如果要打印额外的构造板粘附结构，如Brim或Raft，则此设置将确定打印这些结构时使用的挤出机。

* 当使用无法很好地粘附到构造板的材料进行打印时，使用粘附良好的材料进行打印的筏板可能会很有用。
* 如果您只使用一个挤出机进行打印，并且它不是第一个挤出机，则此设置不会自动调整为使用与您的模型相同的挤出机。然后，您的打印仍将使用多个挤出机。

当使用Skirt或Brim时，[Skirt/Brim挤出器](skirt_brim_extruder_nr.md) 完全覆盖此设置，尽管默认情况下它们应该相同。当使用Raft时，各个组件可以指定不同的挤出机，分别是：[Raft底层挤出器](raft_base_extruder_nr.md), [Raft中间挤出器](raft_interface_extruder_nr.md) and [Raft顶层挤出器](raft_surface_extruder_nr.md).
