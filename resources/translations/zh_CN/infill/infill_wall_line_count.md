额外填充壁计数
====
此设定可在填充区域周围加入许多等高线。这类似于增加[壁走线次数](../shell/wall_line_count.md)，但轮廓不会围绕皮肤，壁也将位于皮肤和填充之间。它也类似于添加[额外皮肤壁计数](../top_bottom/skin_outline_count.md)，但在填充周围而不是皮肤周围。

这些壁将使用填充的设置进行打印。

<!--screenshot {
"image_path": "infill_wall_line_count.png",
"models": [{"script": "hexasphericon.scad"}],
"camera_position": [0, 40, 136],
"settings": {
"infill_wall_line_count": 2,
"skin_outline_count": 0
},
"layer": 546,
"colours": 64
}-->
![填充周围的两个额外壁](../images/infill_wall_line_count.png)

与在皮肤周围添加额外壁相比，此设置将大大增加模型的强度并降低填充透过皮肤的可见性，但同时也会增加打印时间与材质使用量。尽管额外的皮肤壁将替换本来作为皮肤打印的材质，但此设置实际上会添加材质，除非填充密度已经为100%。

这非常类似于在整个打印件周围添加额外的壁。但是，最好在填充或皮肤周围至少添加一面额外的壁，因为这样可以防止皮肤走线在半空中结束。
