2.9.0 - Spider's Reference
====
This update supports Cura 5.0. The interface is updated to mimic the new look, and articles are updated with Cura's new functionality. Also added a Czech translation.

New Features
----
* The interface when using Cura 5.0 now reflects the new look of the settings list.
* Added a Czech translation.

Bug Fixes
----
* The Settings Guide now loads in Cura 5.0.
* Fixed a parsing error when using conditional to conditionally show images.
* No longer use deprecated items in Cura 5.0 (except the category icons).
* Fixed crash if Cura's own QML fails to load.

Articles
----
* Added a lot of new articles for the new settings in Cura 5.0.
* Updated existing articles to reflect the new behaviour in Cura 5.0.
* Added missing replacement keys in the start g-code article.
* Updated almost all layer view renders with renders of Cura 5.0 (also when viewed from older Cura versions).
* Updated French translations.
* Updated German translations.

2.8.1
====
Articles
----
* The German translations have been completed.
* Added some information on the position of the build plate to the adhesion article.
* Updated name of Maximum Feedrate article.

2.8.0 - Thank you Sekisback
====
New Features
----
* New German translations are available for 148 articles.

Bug Fixes
----
* Fixed some articles not displaying proper formatting in the setting tooltips.

Articles
----
* Added articles for Lightning Infill settings.
* Expanded shrinkage troubleshooting article.
* Added layer splitting article.
* Added explanation of new combing mode in Cura 4.12
* Added new g-code replacement keys in Cura 4.12.
* Updated French translations.
* Fixed a bunch of broken links between articles.

2.7.1
====
Bug Fixes
----
* Fixed a rare crash if trying to load custom articles for which no English translation exists.

Articles
----
* Added articles for the new Monotonic Order settings.
* Expanded the Alternate Extra Wall article.
* Updated French translations.

2.7.0 - An Update for Ants
====
A small maintenance update to fix a few bugs and address some pain points.

New Features
----
* A new menu entry under the Extensions menu navigates directly to the preferences.

Bug Fixes
----
* The articles are now correctly displayed in the tooltips after switching printer types.
* If Cura's main window doesn't get created for some reason, the Settings Guide won't cause it to also crash any more.

Articles
----
* The diagrams for Slicing Tolerance are made more clear to understand.
* Updated French translations.

2.6.0 - Robot Overlords
====
In this update, all images have been re-made using an automated method that allows updating the images more easily in the future. Many articles have been expanded with additional details.

New Features
----
* Most screenshots are now automatically generated, making it easier to keep them up to date in the future.
* The guide is now loaded in the setting tooltips by default, allowing users to find it more easily.

Bug Fixes
----
* The translation menu of the guide is no longer empty if modified with additional translations (for all of Cura's own languages).
* The Settings Guide no longer creates its own theme, causing mix-ups with the original theme and bugs in Cura's interface if it is outdated.

Articles
----
* Almost all screenshots have been updated to how they look in Cura 4.9.
* Most screenshots have improved resolution. Some are changed to show the result better.
* Added articles for new settings in Cura 4.9.
* Updated dozens of articles with more information and corrections.
* Updated French translations.
* Updated Czech translations.
* Improved linking between different articles.

2.5.0 - In the Background
====
This is a maintenance update to document the new features of Cura 4.8, with just some minor adjustments.

New Features
----
* If the window was already open but gets opened again, it will now be brought to the foreground and get focus.
* Added a preference to keep the window always in focus (modal).

Articles
----
* Update for new features in Cura 4.8.
* Added a glossary of 3D printing terms and how they're used in Cura.
* Updated French translations.
* Updated Czech translations.

2.4.0 - Something to Hide
====
This is a maintenance update to document the new features of Cura 4.7. The articles can now also show different content depending on which version of Cura the user is running.

New Features
----
* Added a syntax to allow articles to display different content in different Cura versions.
* Added a syntax to be able to hide outdated content when viewed on Github.
* Automated tests have been put in place to make it easier for people to contribute articles and translations while ensuring quality.

Bug Fixes
----
* Some very short articles weren't displaying paragraphs properly. They are now.

Articles
----
* Added articles about new settings for Cura 4.7.
* Added a Czech translation.
* Updated French translations.
* Another pass over some old articles has been made to add advantages and disadvantages of some settings that were missing them.
* In old versions of Cura, information only relevant to new versions is no longer shown.
* In new versions of Cura and on Github, information only relevant to old versions is no longer shown.
* Notices at the end of the articles are consistently bold now, not italic.
* The contributors page is redesigned to give all contributors an equal position, not highlighting some with a picture but not others.

2.3.0 - Machine Language
====
This release adds translations of the guide, and new articles about the printer ("machine") settings.

New Features
----
* If translations for an article are available, a button in the top right corner of the article allows switching the language.
* Articles will now show their titles when viewed on Github.
* By default, articles will be shown in the language configured for the rest of Cura (if translations are available).

Bug Fixes
----
* The guide will no longer cause a (harmless) error to appear in the log upon starting Cura.
* Links to articles in the same category work again on Windows.
* The scroll position is no longer retained when switching articles.

Articles
----
* Added articles for the printer/machine settings.
* Added partial French translations.
* Added partial Russian translations.
* Added partial Dutch translations.

2.2.1 - Bug Fixes
====
* Fixed inter-article links.

2.2.0 - The Bad One
====
This release adds articles on common forms of print failure, including pictures of the actual print results.

New Features
----
* Support for Cura 4.5.
* Articles can optionally be shown in the setting tooltip in the main setting list, instead of Cura's own setting description.
* Articles can now contain checkboxes, which are stored as preferences for the plug-in.
* All images are now brute-force RLE optimised, improving loading speed and reducing file size.

Bug Fixes
----
* The menu entry now appears under the Extensions header in MacOS as well.
* Fixed possible bug where image links would break if another closing bracket appears in the same paragraph.
* Fixed building with CMake if you didn't have Mistune cloned from an earlier build.

Articles
----
* Added articles about print problems, their causes and how to fix them with Cura settings.
* Added pictures of print results for settings where layer view doesn't adequately show the result.
* Added articles for the new settings in Cura 4.5.
* A new "article" has been added for Settings Guide preferences.
* The article files are now subdivided by category, so that they can more easily be found with a browser.
* Fixed a dozen broken links in various articles.
* Added pictures for fuzzy skin articles.

2.1.0 - Completionist
====
In this release the aim was to complete the articles for all of Cura's settings. No more missing links.

New Features
----
* Support for Cura 4.4.
* Added keyboard navigation with the arrow keys (once focus is in the article list).
* If an article is missing in a future release of Cura because the plug-in hasn't been updated yet, the setting description is now shown.
* Links to different articles now also work when viewed on Github.
* Images now also work when viewed on Github.
* The selection highlight in the article list is now animating when a different article is shown.
* The article font is a little bigger than before, for readability.

Bug Fixes
----
* SVG images are now rendered at the correct size, improving performance and image quality.
* Links are now coloured according to the theme, making them easier to read in dark themes.
* Italic text is now rendered properly.
* Fixed QML errors in the log when no article is selected.
* Improved performance of the search bar.
* The lazy-loading of articles is no longer triggered when the guide opens for the first time, but when opening an article, further reducing performance impact on start-up.

Articles
----
* Added 247 new articles about settings, doubling the amount of articles. This completes the entire settings list.
* The About page is renamed to Contributors and lists all contributors.

2.0.2 - The Requirement
====
* Categories are now always expanded while a search is active.

2.0.1 - Bug Fixes
====
* Fix packaging script.
* Fix loading the settings list in Cura 4.3 and newer.

2.0.0 - For Mark(down)
====
In this release all setting articles were completely rewritten, and most images re-made in higher resolution.

New Features
----
* Articles are now stored in Markdown format, allowing greater flexibility in their layout and structure.
* Support for Cura version 4.2.
* Articles can now link to each other.
* Articles can now link to the internet.
* Each image can now have its own subtext.
* Articles can now be added about other things than settings.

Bug Fixes
----
* The plug-in will not load all articles any more during the loading screen, which would slow down Cura's boot sequence.

Articles
----
* All articles are rewritten. They now contain much more information on their behaviour and how you'd use them. On average the articles have about 2.5 times as much information.
* Almost all images have been re-made in a higher resolution, with better compression techniques to limit installation size.
* All diagrams have been converted to SVG for better picture quality and easier maintainability.
* An about category is added with information about the plug-in itself.
* Many corrections have been made to various articles.

1.3.0 - Hillity Usability
====
This release adds many tiny quality-of-life features and improves the quality of images while further reducing download size.

New Features
----
* Improved performance of switching selected settings.
* The dialogue can now be resized.
* The dialogue is no longer modal, allowing you to use Cura while the dialogue is open.
* The image thumbnails grid has been reworked. It uses more of the page width if available and should be more reliable.
* The zoomed image is now always 2/3rds of the window size regardless of window size and screen resolution.
* All image thumbnails and zoomed images now have a white background, in order to improve usability in dark themes.
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
