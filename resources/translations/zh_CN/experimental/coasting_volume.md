滑行体积
====
此设置确定送料机在轮廓结束之前停止送料的距离。然而，滑行的长度在材料体积中配置。它与喷嘴室内的容积关系更为密切。

<!--screenshot {
"image_path": "coasting_enable.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
"coasting_enable": true,
"coasting_volume": 0.06,
"z_seam_position": "backright"
},
"colours": 32
}-->
<!--screenshot {
"image_path": "coasting_volume_0_03.png",
"models": [{"script": "phone_holder.scad"}],
"camera_position": [0, -215, 117],
"minimum_layer": 1,
"structures": ["travels", "helpers", "shell", "infill", "starts"],
"settings": {
"coasting_enable": true,
"coasting_volume": 0.03,
"z_seam_position": "backright"
},
"colours": 32
}-->
![滑行0.06毫米³的材料](../images/coasting_enable.png)
![滑行0.03mm ³的材料](../images/coasting_volume_0_03.png)

增加滑行体积会导致喷嘴在完成轮廓之前停止进一步挤出。其结果是，接近结束时它将有更多的挤出不足。滑行的功能是在接合轮廓时补偿斑点，因此增加滑行体积可以补偿更大的斑点。

但是，过度增加滑行体积将导致轮廓末端出现严重的挤出不足。它甚至会导致轮廓后打印的任何东西都出现一些挤出不足，因为那时喷嘴上的压力仍然较低。
