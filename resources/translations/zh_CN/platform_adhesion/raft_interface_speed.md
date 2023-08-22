Raft 中间打印速度
====
<!--if cura_version<5.0:此设置配置Raft 中间层的打印速度。中间层的速度可以与顶层和底层的速度分开配置。-->
<!--if cura_version>=5.0-->此设置配置Raft 中间层们的打印速度。中间层们的速度可以与顶层和基层的速度分开配置。<!--endif-->

![中间层位于Raft中的位置](../images/raft_dimensions_simplified.svg)

打印中间<!--if cura_version<5.0:层--><!--if cura_version>=5.0-->层们<!--endif-->的速度越慢，材料保持热度的时间就越长，这就减少了内应力。一旦材料冷却下来，这就减少了翘曲。但是，打印速度越慢，所需时间也越长。
