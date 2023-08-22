Raft 中间间距
====
此设置调整Raft中间<!--if cura_version<5.0:层--><!--if cura_version>=5.0-->层们<!--endif--> 的线间距。这与[填充走线距离](../infill/infill_line_distance.md) 设置的方式类似。其主要目的是调整Raft的刚度以及顶层得到支撑的程度。

![与Raft有关的尺寸](../images/raft_dimensions.svg)

使线条间隔较远可减少Raft的打印时间。这也使得Raft更容易弯曲，更容易折断。然而，如果线间隔很远，Raft的顶层将得不到很好的支撑。这使得Raft的表面不平坦，这降低了Raft和模型之间的附着力，也使模型的底面更凌乱。
