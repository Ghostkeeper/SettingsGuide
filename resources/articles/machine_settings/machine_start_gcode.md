Start G-code
====
With this setting, a bit of g-code can be written that will be executed at the very start of every print. Using this g-code, the printer can be set up to be ready for printing.

Some examples of things that are commonly executed in the start g-code are:
* Priming the nozzle(s).
* Heating up the build plate.
* Heating up the nozzle(s).
* Making sure the correct extruder is selected.
* Configuring the fans, accelerations or jerk.
* Automatic bed levelling.
* Configuring linear advance.

For a reasonably comprehensive list of the available g-codes you can write here, refer to the [RepRap Wiki](https://reprap.org/wiki/G-code).

References to settings
----
When editing the start g-code, you can refer to the values of other settings. This uses a certain syntax. Settings are referred to by their *key*. This key is an internal name in Cura. It's not visible in the user interface. For a full list of all keys, refer to [this document](https://github.com/Ultimaker/Cura/blob/master/resources/definitions/fdmprinter.def.json) in Cura's source code.

The syntax to get the value of a global setting is as follows:

`{setting_key}`

In other words, write the setting's key in curly brackets. This will get the global value of a setting. Many settings though can be different for each extruder. Those should be referenced as follows:

`{setting_key, #}`

Here in place of the `#` symbol you should write the number of the extruder from which to get the setting. Extruders start counting at 0. Global settings can also be obtained by specifying an extruder, but they will be the same for all extruders. When you try to obtain an extruder-specific temperature without specifying the extruder number, you will get the value for the first extruder that is not disabled.

You can use these references for instance to pre-heat to the correct temperature, or to set the accelerations. Here are some examples:

`M104 S{material_print_temperature_layer_0, 0} ;pre-heat`

`M140 S{material_bed_temperature_layer_0} ;heat bed`

`M204 P{acceleration_print, 0} T{acceleration_travel, 0}`

`M205 X{jerk_print, 0}`

Be careful with the speeds. G-code normally accepts feed rate in millimetres per *minute*, while the settings are listed in millimetres per *second*. There is no way to select the correct feed rate at the moment. Making calculations in these references is impossible.

Other information
----
Through the same syntax as references to settings, some auxiliary information is also available:

* `{time}` refers to the current local time of the day it was sliced.
* `{date}` refers to the date it was sliced.
* `{day}` refers to the day of the week on which it was sliced.
* `{initial_extruder_nr}` refers to the extruder that the print will start with.

Heating before the start g-code
----
Cura will automatically issue heating commands before your start g-code begins. This way your start g-code doesn't need to consider that the nozzle needs to heat up. You can immediately start priming the nozzle. If your start g-code contains a reference to any temperature (for the nozzle or the bed), this will be disabled (for respectively the nozzle or the bed).

*This setting is a machine setting, so it will not appear in the normal list of settings. It can be changed by going to the list of printers in the preferences screen and clicking on "Machine Settings".*