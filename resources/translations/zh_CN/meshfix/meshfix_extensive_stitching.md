广泛缝合
====
Cura需要知道模型内部的位置，以便用材质填充模型。如果模型的表面不是精确封闭的或具有内壁，则模型内部所在的位置可能不明确。

模型不是流形的一种常见情况是：模型的一个额外部分附加到一个原本闭合的零件。使用并非为制造而设计（仅用于数字渲染）的CAD软件（如Blender或SketchUp）编辑网格时，这是很常见的。你可以在下面的图片中看到一个例子。

<!--screenshot {
"image_path": "meshfix_extensive_stitching_xray.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"layer": -1
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_disabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
"meshfix_extensive_stitching": false
},
"colours": 32
}-->
<!--screenshot {
"image_path": "meshfix_extensive_stitching_enabled.png",
"models": [{"script": "external_attachment.py"}],
"camera_position": [62, 87, 68],
"settings": {
"meshfix_extensive_stitching": true
},
"colours": 32
}-->
![X射线视图在内部显示了一个额外的曲面](../images/meshfix_extensive_stitching_xray.png)
![禁用此设置后，仅打印正确关闭的体积](../images/meshfix_extensive_stitching_disabled.png)
![启用此设置后，将正确附加额外的部分](../images/meshfix_extensive_stitching_enabled.png)

如果网格中的间隙没有正确地无缝连接，则此设置可使Cura更好地尝试闭合网格中的间隙。这会增加良好打印的机会，但会增加切片时间，有时可能会将错误的曲面连接在一起。
