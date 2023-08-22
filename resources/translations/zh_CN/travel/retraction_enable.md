启用回抽
====
如果3D打印机停止推动材料，材料不会立即停止从喷嘴末端流出。喷嘴中有一些残余材料，它将被加压，因此它将保持流动一段时间。要真正阻止材料流动，打印机需要将材料从喷嘴开口中抽回。这对于在不拉丝的情况下进行干净的空驶是必要的。

<!--screenshot {
"image_path": "retraction_enable_disabled.png",
"models": [{"script": "wire_mount.scad"}],
"camera_position": [0, -115, 68],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_enable": false},
"minimum_layer": 2,
"colours": 64
}-->
<!--screenshot {
"image_path": "retraction_enable_enabled.png",
"models": [{"script": "wire_mount.scad"}],
"camera_position": [0, -115, 68],
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {"retraction_enable": true},
"minimum_layer": 2,
"colours": 64
}-->
![已禁用回抽](../images/retraction_enable_disabled.png)
![回抽空驶显示为浅蓝色](../images/retraction_enable_enabled.png)

当空驶期间对拉丝特别敏感时，会进行回抽。仅通过填充或从一个支撑到另一个支撑的移动通常不会回抽。通过[最大回抽计数](retraction_count_max.md)和[最小挤出距离范围](retraction_extrusion_window.md)设置，还可以限制材料的回抽频率。

回缩有显著的优点，但也有一些缺点：
* 它会大大减少拉丝。打印的不同部分之间不再有连线。
* 这将显著减少喷嘴进入零件周边时产生斑点的数量和大小。
* 需要一点时间才能抽回。
* 当回抽发生时，材料流量被中断。这会对尺寸精度、结合和挤出不足产生负面影响。
* 当回抽次数过多时，线材可能会磨损，从而妨碍进料器夹持材料。

**柔性材料更难回缩，因为拉动线材会使线材拉伸，而不是将其拉出喷嘴。使用此类材料启用回抽可能非常耗时，且效率相对较低。**
