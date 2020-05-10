Machine Type
====
This is a descriptive setting, describing which model of printer you are printing with.

Currently this setting is used only to output the correct metadata in the g-code header for the Griffin g-code flavour. Using this information, the printer can know which printer model the g-code was optimised for. If the printer is connected to a group of printers of various types, it may decide to let the correct type of printer print this g-code. If the preferred printer is not available, it may give the user a warning that the g-code was not designed for this printer.

**Since this is a machine setting, this setting is not normally visible in the settings list.**