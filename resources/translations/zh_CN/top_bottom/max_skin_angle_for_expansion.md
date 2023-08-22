最大扩展皮肤角度
====
由于皮肤存在于整个模型中，因此没有必要扩展所有的这些区域。相反，只有皮肤表面与地平线之间的角度小于此设置的区域才会扩展。这样，具有突出元素的平坦表面将得到强化，而不会不必要地增加模型其余部分的打印时间。

<!--screenshot {
"image_path": "max_skin_angle_for_expansion_90.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"expand_skins_expand_distance": 3,
"max_skin_angle_for_expansion": 89
},
"colours": 64
}-->
<!--screenshot {
"image_path": "max_skin_angle_for_expansion_45.png",
"models": [{"script": "stamp.scad"}],
"camera_position": [0, 200, 30],
"settings": {
"wall_line_count": 0,
"infill_wall_line_count": 1,
"expand_skins_expand_distance": 3,
"max_skin_angle_for_expansion": 45
},
"colours": 64
}-->
![设置为90度，所有皮肤将按照皮肤扩展距离的设置进行扩展](../images/max_skin_angle_for_expansion_90.png)
![设置为45度，只有水平的区域得到扩展 ](../images/max_skin_angle_for_expansion_45.png)

扩展皮肤对于加强顶部或底部与侧面墙壁之间的连接非常有用。然而，这也会大大增加打印时间和材料使用量。增强皮肤和墙壁的连接在有些部分上作用不大，该设置允许您过滤掉这些部分的材料。

对于此设置，0°为水平方向。如果设置为0°，不会扩展皮肤。90°为垂直方向，可使所有皮肤区域得到扩展。
