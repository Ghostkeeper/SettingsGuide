起始层走线宽度
====
该设置按一定的比例增大或减小起始层的线宽。

<!--screenshot {
"image_path": "initial_layer_line_width_factor.png",
"models": [{"script": "hex_foot.scad"}],
"camera_position": [0, 92, 122],
"settings": {
"adhesion_type": "brim",
"initial_layer_line_width_factor": 200
},
"colours": 32
}-->
![起始层的线宽是其余部分的两倍](../images/initial_layer_line_width_factor.png)

本设置的目标是改善构造板的粘附能力。为了打印更宽的线条，喷嘴必须挤出更多材料，也必须让他们向外流的更宽。这使得喷嘴将材料用更大的力推向构造板，增加了线材和构造板之间的粘附。
* 线条不仅在宽度上变化，他们之间的距离也会相应改变。所以不会出现挤出过度或挤出不足。
* 该设置影响所有走线宽度：皮肤层、壁、平台附着、支撑、装填塔等。他们将使用相同的比例变宽或收窄。
