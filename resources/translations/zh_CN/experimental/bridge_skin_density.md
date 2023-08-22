连桥表面密度
====
此设定可控制打印底侧的密度，将在那里桥接间隙。密度为100%时，直线会直接相邻放置。在较低的密度下，线被进一步隔开。

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
"image_path": "bridge_skin_density_50.png",
"models": [{"script": "bridge.scad"}],
"layer": 80,
"settings": {
"bridge_settings_enabled": true,
"bridge_skin_density": 50,
"bridge_skin_material_flow": 100,
"bridge_wall_material_flow": 100
},
"camera_position": [0, 18, 79],
"colours": 64
}-->
![密度为100%时，线条直接相邻放置](../images/bridge_skin_density_100.png)
![密度50%时，线条之间有一些间隔](../images/bridge_skin_density_50.png)

调整此设置时，有两个主要影响：

当将皮肤线彼此直接相邻时，它们将彼此粘在一起。这将使桥接间隙的底部看起来更漂亮，因为曲面将是连续的而不是拉丝的。此外，第二条线在桥接时可以稍微靠在第一条线上，这使得桥的下垂稍微少一点。

然而还有另一个影响：当这些线间隔更远时，它们将能够更快地冷却，然后也不会下垂太多。当然，这只适用于风扇打开时，所以对于高温材料，这种策略是行不通的。

哪种效果更强取决于材料的粘度、固化速度和风扇速度。始终需要进行一些调整。

**如果[连桥表面流量](bridge_skin_material_flow.md)小于100%，则即使密度为100%，线条之间也会有一些间距，因为这样线条会更细。**
