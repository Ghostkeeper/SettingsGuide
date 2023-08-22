顶部/底部走线图案
====
该设置允许您选择填充顶/底面的方式。有几种可供选择的图案，但比填充图案有更多限制。只有创建实心层的图案才可用。

<!--screenshot {
"image_path": "top_bottom_pattern_lines.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "lines"},
"colours": 64
}-->
直线
----
![直线](../images/top_bottom_pattern_lines.png)

基本图案，使用直线贯穿表面。这些线的默认方向是固定的，所以可以很好的被填充和支撑托起。线的方向在每层间交替。
* 提供良好的表面质量。
* 在线条打印方向上非常坚固。
* 有力的和壁黏在一起，形成相对坚固的部分。

<!--screenshot {
"image_path": "top_bottom_pattern_concentric.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "concentric"},
"colours": 64
}-->
同心圆
----
![同心圆](../images/top_bottom_pattern_concentric.png)

同心圆图案持续的朝模型内部绘制轮廓。
* 各个方向强度一致。
* 防止产生空泡和间隙。更容易的产生水密物体。
* 线条很好地桥接带来质量更好的悬垂。
* 如果部件是圆形的，在轮廓汇集的中心会产生一个恼人的点。
* 表面质量不太理想。

<!--screenshot {
"image_path": "top_bottom_pattern_zigzag.png",
"models": [{"script": "ring_5mm.scad"}],
"camera_position": [0, 0, 100],
"settings": {"top_bottom_pattern": "zigzag"},
"colours": 64
}-->
锯齿形
----
![锯齿状](../images/top_bottom_pattern_zigzag.png)

锯齿状图案与直线图案非常相似，不同之处在于直线将在壁内结束，锯齿则向下一条皮肤线继续打印。
* 提供良好的表面质量。
* 在线条打印方向上非常坚固。
* 使挤出速率更稳定，提高难以挤出材料的表面一致性。
* 不像线条图案那样粘在壁上。[皮肤重叠](skin_overlap.md) 的效果降低，会造成零件变弱，悬垂质量降低。
