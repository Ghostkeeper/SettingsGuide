支撑Brim走线次数
====
此设置可调整支撑区域内支撑边缘(Brim)的轮廓数量。线条越多，边缘(Brim)越宽。

<!--screenshot {
"image_path": "support_brim_2mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
"support_enable": true,
"support_use_towers": false,
"support_brim_enable": true,
"support_brim_width": 2
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
"support_enable": true,
"support_use_towers": false,
"support_brim_enable": true,
"support_brim_width": 4
},
"colours": 64
}-->
![5条边缘线](../images/support_brim_2mm.png)
![10条边缘线](../images/support_brim_4mm.png)

更多的边缘(Brim)数量将增加支撑件与构造板的粘附性，并减少支撑件的翘曲。因此，支撑件将更牢固地站立，这提高了打印的可靠性。
