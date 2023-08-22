Raft 中间厚度
====
<!--if cura_version<5.0:此设置可调整Raft中间层的垂直厚度。-->
<!--if cura_version>=5.0-->此设置可调整Raft中间层们的垂直厚度。这只是一个层的高度，因此中间层的总高度将是此设置乘以[Raft 中间层](raft_interface_layers.md) 的值。<!--endif-->

![与Raft有关的尺寸](../images/raft_dimensions.svg)

有一个较厚的Raft层往往使它有点硬。这样可以防止打印过程中和打印后发生弯曲。在打印过程中，您可能希望Raft保持刚性，以免扭曲，这会破坏与构造板的附着力，并导致Raft与模型融合。打印后，您可能希望Raft具有弹性，以便可以更轻松地将其从模型上拆下。这是该设置需要达到的平衡。
