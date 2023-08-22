连桥稀疏填充物最大密度
====
如果您使用非常低的填充密度进行打印，则顶部皮肤会下垂，导致[枕形效应](../troubleshooting/pillowing.md) ，并且打印的顶部表面通常不规则。可选地，桥接技术也可以应用于顶部皮肤。此设置配置将开始应用桥接技术的填充速率。

<!--screenshot {
"image_path": "bridge_sparse_infill_max_density.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"layer": 108,
"settings": {
"bridge_settings_enabled": true,
"bridge_sparse_infill_max_density": 100
},
"camera_position": [58, 27, 104],
"colours": 64
}-->
![皮肤在填充上桥接](../images/bridge_sparse_infill_max_density.png)

此设置被配置为阈值，以允许配置文件包含单个值。当用户不断调整填充密度时，皮肤的桥接将自动启用或禁用。

顶部皮肤的桥接通常以非常低的填充率产生更平滑的顶部表面。但是，如果使用此方法，请务必确保有足够的[顶层](../top_bottom/top_layers.md)来正确闭合曲面，而无需在最高层上应用桥接技术。桥接技术（尤其是在[走线宽度](bridge_skin_material_flow_3.md)减小的情况下）不会完全闭合曲面。如果顶部皮肤没有足够的层次，打印件最终将存在孔洞并影响强度。
