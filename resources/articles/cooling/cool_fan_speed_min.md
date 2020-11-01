Regular Fan Speed
====
The speed at which the fans on the print head will spin, unless the layer is very small. This is the fan speed that will be used for most of your print, but if the layer is small then the fan speed will be increased towards the [Maximum Fan Speed](cool_fan_speed_max.md) in order to cool the layer faster.

![Which fan speed is used where](../images/cool_fan_speed.svg)

* A greater speed allows better cooling. This reduces oozing and stringing.
* A greater speed will produce better overhangs and reduces the pillowing effect.
* A lower speed will reduce warping with some materials and will make the print stronger.

The fan speed should almost always be maximum when printing materials with a low glass transition temperature range, such as PLA. These materials have virtually no downsides to cooling quickly, since the heat of the nozzle easily keeps the temperature above the glass transition range.