连桥表面流量
====
此设定可调整为打印桥接底面挤出的材料量。

<!--screenshot {
"image_path": "bridge_skin_density_100.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
"bridge_settings_enabled": true,
"bridge_skin_density": 100,
"bridge_skin_material_flow": 100,
"bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
<!--screenshot {
"image_path": "bridge_skin_material_flow_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
"bridge_settings_enabled": true,
"bridge_skin_density": 100,
"bridge_skin_material_flow": 50,
"bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![在100%流量时，线条会以其一般走线宽度绘制](../images/bridge_skin_density_100.png)
![流量为50%时，线条会变细](../images/bridge_skin_material_flow_50.png)

减少材料的量将有效地减少桥接间隙底侧的走线宽度。随着走线宽度的减小，线的表面质量比更大，这允许它们更快地冷却，这将防止它们同样多地下垂。

但是，将流速降低太多会导致流量速率发生很大变化，尤其是在与[较慢打印速度](bridge_skin_speed.md)结合使用时。实际上，材料将不能非常快地改变其流量速率，这导致线条在流速减慢时比预期的稍厚，并且在流速加快时比预期的稍薄。
