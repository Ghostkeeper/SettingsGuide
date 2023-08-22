Raft中间打印加速度
====
<!--if cura_version<5.0:该设置配置打印Raft的中间层时打印头的加速率。Raft底层、中层和顶层的加速度可独立配置。-->
<!--if cura_version>=5.0-->该设置配置打印Raft的中间层们时打印头的加速率。Raft底层、中层和顶层的加速度可独立配置。<!--endif-->

![中间层位于Raft中的位置](../images/raft_dimensions_simplified.svg)

由于Raft通常由长线段组成，因此增加加速度通常对打印时间的影响很小。不过在线的末端通过角落时，增加加速度将节省一点时间时。

增加加速率将导致打印机在打印Raft的中间<!--if cura_version<5.0:l层--><!--if cura_version>=5.0-->层门<!--endif--> 时振动更大。这略微增加了将Raft从构造板上拉下的风险。
