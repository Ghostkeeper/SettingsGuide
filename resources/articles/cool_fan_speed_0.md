The speed at which the fans on the print head will spin in the beginning of the print, during the first few layers. The fan speed will then slowly transition into the regular fan speed. At the layer number indicated by the [Regular Fan Speed At Layer](cool_fan_full_layer.md) setting, the fan speed will have transitioned to the [Regular Fan Speed](cool_fan_speed_min.md).

![Which fan speed is used where](images/cool_fan_speed.svg)

The fan speed at the beginning of the print is normally lower than during the rest of the print. This allows the material to cool down slower and sag further onto the build plate. This improves build plate adhesion.