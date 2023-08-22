圆柱装填塔
====
如果启用此设置，装填塔的形状将为圆柱形。如果它被禁用，装填塔将是方形的。

<!--screenshot {
"image_path": "prime_tower_circular_enabled.png",
"models": [
{
"script": "cube.scad",
"object_settings": {
"extruder_nr": 0
}
},
{
"script": "cube.scad",
"object_settings": {
"extruder_nr": 1
},
"transformation": ["translateX(40)"]
}
],
"camera_position": [470, -384, 150],
"camera_lookat": [470, -470, 5],
"settings": {
"prime_tower_enable": true,
"prime_tower_min_volume": 3
},
"colours": 16
}-->
![方形装填塔](../images/prime_tower_circular_disabled.png)
![圆柱装填塔](../images/prime_tower_circular_enabled.png)

无论哪种情况，装填塔依然是中空的。圆柱装填塔完全小于方形装填塔（因为角被切掉了）。装填塔的[最小体积](prime_tower_min_volume.md)仍然保持正确。

如果材料有翘曲的趋势，则方形装填塔的四个角可能会从构造板上松动。相比圆形装填塔，这使得它更容易倾倒。打印方形装填塔时也会有更大的加速度。这些加速度使流量速率不一致，这并不符合你装填材料的预期。

圆柱装填塔几乎在各方面都更好。这就是新版Cura删除了该设置的原因。这些版本将始终有一个圆形的装填塔。
