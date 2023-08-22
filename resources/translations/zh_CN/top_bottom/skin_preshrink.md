皮肤移除宽度
====
此设置将移除非常薄的皮肤线条，并将其用填充替代。

只有当皮肤旁边有填充时才会移除皮肤，因此它不会移除打印的最顶部或底部的皮肤，即使它非常薄。

<!--screenshot {
"image_path": "skin_preshrink_original.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_preshrink": 0,
"top_skin_preshrink": 0,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
<!--screenshot {
"image_path": "skin_preshrink_shrunk.png",
"models": [{"script": "stature_symmetrical.scad"}],
"camera_position": [104, -7, 4],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"bottom_skin_preshrink": 1,
"top_skin_preshrink": 1,
"max_skin_angle_for_expansion": 89
},
"colours": 32
}-->
![不移除任何皮肤](../images/skin_preshrink_original.png)
![细小线条已被移除](../images/skin_preshrink_shrunk.png)

皮肤通常会在垂直接近物体顶部或底部的任何位置生成。不是所有地方都需要这样做。垂直的墙壁通常足够坚固，因此，虽然垂直的墙壁旁边通常应该有皮肤，但此设置允许您忽略它。这样可以节省打印时间和材料。

对于大多数打印，将其设置为1或2个走线宽度有助于减少打印时间。此外，如果皮肤变得太薄而无法打印，Cura将在皮肤本应存在的地方留下一个缺口（但太小了）。填充无法正确连接到墙壁。如果打开了[填充壁之间空隙](../shell/fill_perimeter_gaps.md)，这些空隙将被填充，但这种填充方法比普通的皮肤需要更长的打印时间。至少将此值设置为[走线宽度（顶层/底层）](../resolution/skin_line_width.md) 可防止出现这种情况。

如果过多增加此值，则会在填充暴露的顶部和底部表面中出现间隙。特别需要注意的是，有着很薄边缘的模型应该有一层薄薄的皮肤。

<!--screenshot {
"image_path": "skin_preshrink_problem_screenshot.png",
"models": [{"script": "thin_ridge.scad"}],
"camera_position": [64, 0, 100],
"settings": {
"wall_line_count": 3,
"top_skin_preshrink": 5
},
"colours": 64
}-->
![这些皮肤块被移除，暴露出填充物。](../images/skin_preshrink_problem.svg)
![在层视图中也可以看到填充](../images/skin_preshrink_problem_screenshot.png)
