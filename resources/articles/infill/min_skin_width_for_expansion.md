Minimum Skin Width for Expansion
====
Since skin is present throughout the model, it is unnecessary to expand all of those areas. Rather, only the skin angles that are already wider than this setting will get expanded. In that way, flat surfaces with protruding elements will be strengthened, without needlessly increasing printing time for the rest of the model.

![Set to 0mm, all skin is expanded with the Skin Expand Distance setting](../images/max_skin_angle_for_expansion_90.png)
![Set to 0,8mm, only the flat areas are expanded](../images/max_skin_angle_for_expansion_45.png)

Expanding the skin is useful for strengthening the connection between the top or bottom of the print and the walls on the sides. However it can also greatly increase the printing time and material usage. This setting allows you to filter out the material from the sides of the print where it is less useful for strengthening the connection between walls and skin.

You can also configure this setting with the [Maximum Skin Angle for Expansion](max_skin_angle_for_expansion.md) setting. If that setting is changed, this setting will automatically change along. This setting is the one that is actually used for slicing.