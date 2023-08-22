熨平流量
====
熨平将在表面放置额外的线条，是一种有技巧的过度挤出。该设置控制这个额外的挤出流量。流量对于填充表面的缝隙至关重要。

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": true
},
"colours": 64
}-->
<!--screenshot {
"image_path": "ironing_flow.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": true,
"ironing_flow": 20
},
"colours": 64
}-->
![流量为10%时](../images/ironing_enabled_enabled.png)
![流量为20%时](../images/ironing_flow.png)

该值应设置的足够高，以保持喷嘴的压力。这种压力是填充表面缝隙所需的。如果表面非常粗糙（枕形效应或打印过快导致），可能需要您增大此值。
