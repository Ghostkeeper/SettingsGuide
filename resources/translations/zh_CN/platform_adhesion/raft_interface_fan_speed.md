Raft 中间风扇速度
====
<!--if cura_version<5.0:此设置配置打印Raft中间层时的风扇速度。打印中间层时的风扇速度可与底层和顶层分开配置。-->
<!--if cura_version>=5.0-->此设置配置打印Raft中间层们时的风扇速度。打印中间层们时的风扇速度可与底层和顶层分开配置。<!--endif-->

![中间层位于Raft中的位置](../images/raft_dimensions_simplified.svg)

单独配置中间 <!--if cura_version<5.0:层--><!--if cura_version>=5.0-->层们<!--endif--> 的风扇速度非常有用，因为降低风扇速度可以提高床层附着力并减少翘曲。增加风扇速度可以提高曲面的平滑度，但这对于中间<!--if cura_version<5.0:层--><!--if cura_version>=5.0-->层们<!--endif-->来说不是问题。因此，将风扇速度设置为稍低于顶层的速度是很有用的。
