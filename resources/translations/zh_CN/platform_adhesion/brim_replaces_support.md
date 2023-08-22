Brim 替换支撑
====
如果启用此设置，Brim将继续跟随支撑下方的模型，而不是围绕支持面。然后，在下一层中，将支撑物打印在Brim的顶部。支撑周围仍将有Brim。

<!--screenshot {
"image_path": "brim_replaces_support_disabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 100, -136],
"settings": {
"adhesion_type": "brim",
"support_enable": true,
"brim_replaces_support": false
},
"colours": 64
}-->
<!--screenshot {
"image_path": "brim_replaces_support_enabled.png",
"models": [{"script": "castle.scad"}],
"camera_position": [0, 100, -136],
"settings": {
"adhesion_type": "brim",
"support_enable": true,
"brim_replaces_support": true
},
"colours": 64
}-->
![禁用时，brim围绕支撑](../images/brim_replaces_support_disabled.png)
![启用时，brim在支撑下方](../images/brim_replaces_support_enabled.png)

启用此设置将使Brim更好地跟随模型。因此，模型可以更好地保持在构造板上，从而防止翘曲。

在某些情况下，这将减少一些支撑件的Brim的总宽度。然而，在这些情况下，支撑将足够接近模型，Brim与模型的Brim合并，因此几乎不会有粘附的问题。
