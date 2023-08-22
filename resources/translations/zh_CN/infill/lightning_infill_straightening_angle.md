闪电形填充矫直角
====
此设置确定闪电状填充图案内部悬垂的陡峭程度。

闪电填充产生名义上的闪电般的锯齿线，它需要支持打印的顶部，但由于线条上的尖角，这些需要很长的时间来打印。所以下面，将试图理顺那些锯齿状的线条，以减少打印时间。这种矫直导致悬垂。该设置确定允许的悬垂量。

<!--screenshot {
"image_path": "lightning_infill_straightening_angle_40.png",
"models": [
{
"script": "cylinder.scad",
"transformation": ["scaleZ(0.5)"]
}
],
"camera_position": [36, 44, 19],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 40,
"lightning_infill_prune_angle": 10,
"lightning_infill_straightening_angle": 40
},
"colours": 32
}-->
<!--screenshot {
"image_path": "lightning_infill_straightening_angle_10.png",
"models": [
{
"script": "cylinder.scad",
"transformation": ["scaleZ(0.5)"]
}
],
"camera_position": [36, 44, 19],
"settings": {
"infill_pattern": "lightning",
"wall_line_count": 0,
"top_layers": 0,
"lightning_infill_support_angle": 40,
"lightning_infill_prune_angle": 10,
“lightning_inflill_straightening_angle”：10
},
"colours": 32
}-->
![40°时, 填充线很快聚集成直线](../images/lightning_infill_straightening_angle_40.png)
![10°时, 填充内不再有陡峭的悬垂](../images/lightning_infill_straightening_angle_10.png)

快速矫直（增加的悬垂）在一定程度上减少了打印时间，但也降低了打印的可靠性，特别是对于细的走线宽度。如果悬垂太陡，则会导致分层。分层将出现在打印的内部，通常不会是一个问题，但它可能会导致填充的一部分完全失败，顶部的一部分得不到支撑。顶部会出现可见的粗糙或枕形效应，最坏的情况下甚至是一团乱麻。
