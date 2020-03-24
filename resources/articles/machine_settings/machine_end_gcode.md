End G-code
====
With this setting, a bit of g-code can be written that will be executed at the very end of every print. Using this g-code, the printer can turn its components off and clean up after printing.

Some examples of things that are commonly executed in the end g-code are:

* Retracting the material.
* Cooling down the nozzle(s).
* Cooling down the build plate.
* Turning the fans off.

For a reasonably comprehensive list of the available g-codes you can write here, refer to the [RepRap Wiki](https://reprap.org/wiki/G-code).

References to settings
----
When editing the end g-code, you can refer to the values of other settings. This uses a certain syntax. Settings are referred to by their *key*. This key is an internal name in Cura. It's not visible in the user interface. For a full list of all keys, refer to [this document](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) in Cura's source code.

The syntax to get the value of a global setting is as follows:

`{setting_key}`

In other words, write the setting's key in curly brackets. This will get the global value of a setting. Many settings though can be different for each extruder. Those should be referenced as follows:

`{setting_key, #}`

Here in place of the `#` symbol you should write the number of the extruder from which to get the setting. Extruders start counting at 0. Global settings can also be obtained by specifying an extruder, but they will be the same for all extruders. When you try to obtain an extruder-specific temperature without specifying the extruder number, you will get the global default for your printer, before any material profile or anything has been applied (since materials are extruder-specific).

You can use these references for instance to cool-down to a stand-by temperature, or restore the printer's default acceleration and jerk. Here are some examples:

`M104 T0 S{material_standby_temperature, 0} ;stand-by for the next print`

`M104 T1 S{material_standby_temperature, 1}`

`M204 P{machine_acceleration} T{machine_acceleration}`

Be careful with the speeds. G-code normally accepts feed rate in millimetres per *minute*, while the settings are listed in millimetres per *second*. There is no way to select the correct feed rate at the moment. Making calculations in these references is impossible.

Other information
----
Through the same syntax as references to settings, some auxiliary information is also available:

* `{time}` refers to the current local time of the day it was sliced.
* `{date}` refers to the date it was sliced.
* `{day}` refers to the day of the week on which it was sliced.
* `{initial_extruder_nr}` refers to the extruder that the print will start with.