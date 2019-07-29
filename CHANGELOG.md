2.0.0 - For Mark(down)
====
In this release all setting articles were completely rewritten, and most images re-made in higher resolution.

New Features
----
* Articles are now stored in Markdown format, allowing greater flexibility in their layout and structure.
* All articles are rewritten. They now contain much more information on their behaviour and how you'd use them. On average the articles have about 2.5 times as much information.
* Almost all images have been re-made in a higher resolution, with better compression techniques to limit installation size.
* All diagrams have been converted to SVG for better picture quality and easier maintainability.
* Support for version 4.2.
* Articles can now link to each other.
* Articles can now link to the internet.
* Each image can now have its own subtext.
* Articles can now be added about other things than settings.
* An about category is added with information about the plug-in itself.

Bug fixes
----
* The plug-in will not load all articles any more during the loading screen, which would slow down Cura's boot sequence.
* Many corrections have been made to various articles.

1.3.0 - Hillity Usability
====
This release adds many tiny quality-of-life features and improves the quality of images while further reducing download size.

New Features
----
* Improved performance of switching selected settings.
* The dialogue can now be resized. Implements [#2](https://github.com/Ghostkeeper/SettingsGuide/issues/2). The dialogue can also be maximised and minimised.
* The dialogue is no longer modal, allowing you to use Cura while the dialogue is open.
* The image thumbnails grid has been reworked. It uses more of the page width if available and should be more reliable.
* The zoomed image is now always 2/3rds of the window size regardless of window size and screen resolution. Fixes [#5](https://github.com/Ghostkeeper/SettingsGuide/issues/5).
* All image thumbnails and zoomed images now have a white background, in order to improve usability in dark themes. Implements [#4](https://github.com/Ghostkeeper/SettingsGuide/issues/4).
* Quality of image downscaling is improved, producing softer borders and fewer Moiré patterns.
* All layer view screenshots have their colour depth slightly reduced. The difference is imperceptible, but the file size of the download is reduced significantly.
* Improved installation instructions in the Readme.
* Removed slight transparency of zoomed images.
* Removed slight transparency of the logo.

Bug Fixes
----
* The categories are now properly hidden if necessary while searching for settings.
* Fixed a typo in the entry in the Extensions menu of Cura.
* The dialogue now scales properly on high DPI screens such as Apple's Retina displays.
* The theme of the Settings Guide should match the active theme of Cura itself more closely, if it changes any sizes or colours.

Setting Descriptions
----
* Prefer Retract: Added description.
* Connect Top/Bottom Polygons: Added description and preview image.
* Minimum Wall Flow: Added description and preview image.
* Layer Height: Rewritten description and hints.
* Enable Acceleration Control: Corrected graph depicting relation of jerk, acceleration and speed. Improved description and added hints.
* Print Acceleration: Corrected graph depicting relation of jerk, acceleration and speed. Improved description and added hints.
* Initial Layer Bottom Pattern: Added hints and improved description.

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