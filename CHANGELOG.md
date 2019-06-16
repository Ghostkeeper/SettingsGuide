1.2.1
====

Bug Fixes
----
* Display the correct setting when starting the settings guide from the context menu of a setting.
* Minor performance increases when changing selected setting.
* Updated the readme.

1.2.0 - The Transfer
====
This update, Ghostkeeper has taken over development and made it compatible with Cura 4.0.

New Features
----
* Now works with Cura's own dark theme. Some images still show a white-ish border around the image though.
* Improved performance of settings list. It should now load an order of magnitude faster.
* CMake support allows developers to install their work to their local Cura installation more easily.
* Optimised images for smaller file size.

Bug Fixes
----
* Now works in Cura 4.0. No longer works in Cura 3.6 though, so please refer to the [original author's plug-in](https://github.com/alekseisasin/SettingsGuide) for that.
* Images are no longer reduced in quality in order to reduce file size of the plug-in download.

1.1.0 - Ironing Out
====
This release fixes some bugs in order to make the plug-in more appropriate for public release. It is the first release to make its way to the built-in plug-in browser in Cura.

New Features
----
* Added a dark theme.
* Colours and sizes no longer adjust with the main theme file from Cura.

Bug Fixes
----
* The selected setting now correctly updates when changing the selection after opening the dialogue via right-clicking a setting.

1.0.0 - Guiding the Way
====
This release is the original version by AlekseiSasin. It starts as a research project at Ultimaker B.V.

Features
----
* An entry gets added to the Extensions menu that opens a dialogue.
* The dialogue shows the list of all settings in Cura on the right. Clicking on one of these settings displays a more extensive explanation of the setting. Some settings show pictures which can be magnified.
* Right-clicking on a setting in the main Cura window allows you to open the Settings Guide for that setting.
* Added more extensive descriptions for 244 settings, thanks to ElleCross!
* Added 143 images to explain some of the settings better.
* A landing page shows the first time that the Settings Guide is opened.
* A hidden page is added that shows the authors of the plug-in.
* Added support for PNG and GIF images.