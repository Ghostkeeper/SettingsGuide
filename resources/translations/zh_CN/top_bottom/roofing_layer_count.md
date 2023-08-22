顶部表面皮肤层
====
顶层可以使用不同于其他层的设定进行打印。该设置确定需要单独打印部分的大小。有多少层需要分别设定。

<!--screenshot {
"image_path": "roofing_layer_count.png",
"models": [
{
"script": "question_stick_clip.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, -90, 60],
"settings": {
"wall_line_count": 0,
"skin_outline_count": 0,
"roofing_layer_count": 1,
"speed_roofing": 10,
"cool_min_layer_time": 1,
"roofing_extruder_nr": 1
},
"colour_scheme": "speed",
"colours": 32
}-->
![顶部最上层的打印速度（蓝色）比皮肤的其他部分（绿色）慢](../images/roofing_layer_count.png)

一些设置可以显著提高顶层的打印质量，但比较费时，因为设置会应用在顶部的所有皮肤层上。类似的效果可以通过只对最顶层一或两个层的速度进行调整，其余的皮肤则以更快的速度打印。这样就不会对打印时间有太大的负面影响。

可以对顶层进行设置的选项如下：
* [顶部皮肤挤出机](roofing_extruder_nr.md)
* [顶部表层流量](../material/roofing_material_flow.md)
* [顶部表面皮肤速度](../speed/speed_roofing.md)
* [顶部表面皮肤加速度](../speed/acceleration_roofing.md)
* [顶部表面皮肤抖动速度](../speed/jerk_roofing.md)
* [顶部表面皮肤线宽](roofing_line_width.md)
* [顶部表面皮肤图案](roofing_pattern.md)
* [顶部表面皮肤走线方向](roofing_angles.md)

为了获得更好的顶层效果，可以尝试降低速度并增加抖动速度。

以不同颜色打印顶面时(使用[顶部皮肤挤出机](roofing_extruder_nr.md) 设置), 通常不能只打印一层。否则原始颜色仍会渗出。
