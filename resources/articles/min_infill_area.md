This setting causes very small pieces to be filled with the skin pattern rather than with the infill pattern, making them completely solid.

![Set to 0, the thin feet of this model get filled with infill](min_infill_area_disabled.png)
![Set to 150, the feet get filled with skin](min_infill_area_150.png)

Sometimes, very small hollow areas cannot properly get filled with infill, since the infill lines would be so short that the material doesn't get time to flow properly. This setting causes them to be filled with skin instead, making them stronger as well and preventing a border between the skin and the infill.

Setting this setting to 0 effectively disables this feature.