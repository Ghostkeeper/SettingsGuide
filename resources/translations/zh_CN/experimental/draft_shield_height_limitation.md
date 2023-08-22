防风罩限制
====
防风罩可以朝向模型的整个高度打印，也可以仅打印到特定高度。此设置允许您选择防风罩的高度。

<!--screenshot {
"image_path": "draft_shield_enabled.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
"draft_shield_enabled": true
},
"colours": 32
}-->
<!--screenshot {
"image_path": "draft_shield_height_limitation.png",
"models": [{"script": "headphone_hook.scad"}],
"camera_position": [-56, 139, 305],
"settings": {
"draft_shield_enabled": true,
"draft_shield_height_limitation": "limited",
"draft_shield_height": 20
},
"colours": 32
}-->
![防风罩与模型的高度相同](../images/draft_shield_enabled.png)
![防风罩高度限制为20毫米](../images/draft_shield_height_limitation.png)

打印件的底面往往对温度波动最敏感。如果房间很冷，这是大部分翘曲发生的地方，这种翘曲会导致打印件脱离构造板。使用此设定，您可以选择将防风罩的高度限制为特定高度。这样可以节省一些时间和材料。然后，防风罩仍将保护印刷品的底侧，并且还将阻挡由于热空气上升而引起的空气对流（在一定程度上）。

防风罩的打印高度永远不会超过对象本身。
