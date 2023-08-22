支撑悬垂角度
====
悬垂角度会影响向下放置多少材料以支撑打印。角度指获得支撑的最小角度。

**减少此设置的值可生成更多支撑。**

<!--screenshot {
"image_path": "support_angle_low.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
"support_enable": true,
"support_join_distance": 0.1,
"support_angle": 40
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_high.png",
"models": [{"script": "duct.scad"}],
"camera_position": [136, 10, 10],
"camera_lookat": [0, 10, 10],
"settings": {
"support_enable": true,
"support_join_distance": 0.1,
"support_angle": 75
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_angle_prepare_mode.png",
"models": [{"script": "duct.scad"}],
"camera_position": [113, 77, 0],
"layer": -1
}-->
![低悬垂角度产生更多支撑](../images/support_angle_low.png)
![高悬垂角度产生更少支撑](../images/support_angle_high.png)
![被支撑区域以红色表示](../images/support_angle_prepare_mode.png)

减小此设置可使打印机支撑更多的打印部分，甚至是较陡且在打印过程中不会下垂太多的表面。如果支撑支持的部分不需要被支撑，则会不必要地增加打印时间和材料使用量，并且还会在支撑接触到打印件的地方产生伤痕。

但是，有时需要减小支撑角度，以防止材料过度下垂。它通常会提高最终零件的尺寸精度，并使悬垂看起来更好。

无论何时使用支撑，最好在"预览"阶段预览其外观。在那里，你可以看到哪里真正生成支撑。调整此设置是您可以使用的工具之一，用于筛选将在何处生成支撑。
