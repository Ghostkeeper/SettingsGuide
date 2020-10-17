This Cura plug-in aims to be free software (as in freedom). You are free to modify it under the terms of the [license](LICENSE.md), which is chosen purposefully to stimulate people to contribute. Contributors who have their changes merged into Ghostkeeper's repository will be added to the [contributors article](resources/articles/about/contributors.md). This document describes how you can contribute and things you need to keep in mind then.

Reporting bugs
----
Please report bugs in the [issues page of this repository](https://github.com/Ghostkeeper/SettingsGuide/issues). Do not report bugs in the Cura repository; they will be closed there.

When reporting a bug, it helps to provide the following information:
* The version of SettingsGuide you're using.
* Cura's log file (see [Cura's readme](https://github.com/Ultimaker/Cura#logging-issues) for instructions on where to find that).
* What you did when you encountered the bug, or what someone else could do to see it happen.

Reporting mistakes or omissions in the articles
----
If you think there is something wrong with an article, or you think something is missing, you may not always have the technical skill or time to correct it yourself. Please [create an issue](https://github.com/Ghostkeeper/SettingsGuide/issues/new/choose) and explain:
* which article the mistake or omission is in,
* what you'd like to change.

The developer or other contributors can make the changes for you. Keep in mind that some effects are subjective, and settings may have different effects with different printers or materials. Your own experiences are not the only truth, so if there are intricate changes to the effects of a setting there will be discussions to work out the details of what can be written down. 

Requesting features
----
Feature requests are also welcome in the [issues page](https://github.com/Ghostkeeper/SettingsGuide/issues).

I intend to write descriptions for every setting in Cura, but this is a lot of work. If you'd like to request priority for certain settings, feel free to ask.

Providing code improvements
----
Pull requests to the main code (QML, Python) are subject to the following requirements:
* It does not slow down behaviour significantly.
* The code style is similar to the rest of the code in this repository.
* Your code will be licensed under AGPL 3.0 like the rest of the code in this repository.

Writing articles
----
Pull requests to add descriptions for settings or improve current descriptions are also welcome. In general, articles about settings should hold the following format:
1. First an explanation of what the setting does directly.
2. Some pictures with examples, if applicable.
3. Some more technical details of what the setting does.
4. The effects of the setting on your print.
5. Warnings of common mistakes made with this setting or other things that the user should watch out for, if applicable.

This is not set in stone. For some articles (in particular drop-down settings) it makes sense to have a different format.

When taking screenshots of the g-code in layer view, these are some instructions to ensure a consistent look throughout the plug-in.
* Before making a screenshot, remove the build plate shader so that the grid doesn't show up in your screenshot.
* Use the light theme of Cura when taking the screenshot.
* Use the perspective camera mode, not orthographic.
* Don't use the compatibility mode of layer view.
* Don't collage your screenshots. Use separate images for different effects, each with their own subtitle.
* Don't write any text in PNG images. Use SVG images for that, if necessary with embedded PNG images.
* Use an image editor to remove the background, shadow and build plate from your screenshots, to make it work if users have a dark theme.

To adjust your Cura installation for easier screenshot making, the theme can be adjusted. In the file `resources/themes/cura-light/theme.json`, replace the three sections starting with `disabled_axis` with the following:
```
        "disabled_axis": [127, 127, 127, 0],
        "x_axis": [255, 0, 0, 0],
        "y_axis": [0, 0, 255, 0],
        "z_axis": [0, 255, 0, 0],
        "all_axis": [255, 255, 255, 0],

        "viewport_background": [255, 255, 255, 255],
        "volume_outline": [50, 130, 255, 0],
        "buildplate": [255, 255, 255, 0],
        "buildplate_grid": [255, 255, 255, 0],
        "buildplate_grid_minor": [255, 255, 255, 0],

        "convex_hull": [255, 255, 255, 0],
        "disallowed_area": [0, 0, 0, 0],
        "error_area": [255, 0, 0, 127],
```
To restore your Cura installation on Windows, you can run the installer again. On other platforms, you can just download the application again.

Unfortunately, this plug-in is running into the limits of what Ultimaker's Marketplace can handle. Contributions are checked for metadata, and this plug-in is also signed for use in the Enterprise edition of Cura. To prevent a DOS attack, Ultimaker's servers have a limit to the memory and time usage when submitting the plug-in which effectively cap the file size to about 30MB. To stay below this limit, the plug-in employs a lot of tricks to reduce the file size of its resources.

Please take care with PNG images. Using the above theme settings will already make screenshots smaller. Other adjustments you can make are:
1. Reduce your image to 256 colours. You can use dithering if you think it looks better, but quite often it doesn't look better.
2. Download [OptiPNG](http://optipng.sourceforge.net/).
3. Optimize your image by entering this in a terminal: `optipng -o7 -strip all my_image.png`

Animated images are even more prone to having large file sizes. The following steps should guide you to produce space-efficient animations:
1. Use a smaller resolution, by zooming out in Cura rather than by scaling the pictures down after taking the screenshots.
2. See if you can reduce the colour depth to 64 or 32 colours without introducing a significant amount of dithering or losing visual detail.
3. If you have an animation that requires smooth motion, use at most 5fps. If you have an animation that just shows several stages or layers, limit your image to one frame per stage or layer.
4. Don't create animations of more than 5 seconds.
5. Download [FlexiGIF](https://create.stephan-brumme.com/flexigif-lossless-gif-lzw-optimization/).
6. Optimize your image by entering this in a terminal: `flexigif my_image.gif my_image_opt.gif`.
7. Delete the old image and rename the new `my_image_opt.gif` to have the original file name.

Note that Cura's interface framework doesn't properly support animated SVG images. GIF is a better option.

Diagrams should be submitted in SVG format. Also for these there are a number of requirements:
* The source code of the SVG file will be treated as normal source code during the review, so please make sure that it is readable.
* The SVG files are rendered with QtSVG, which supports a very [limited subset](https://doc.qt.io/qt-5/svgrendering.html) of the SVG specification. Only the static features of SVG Tiny 1.2.
* Clipping is not supported.
* Gradients are not supported.
* Animations are not supported.
* Patterns are not supported.

Optimising these images takes a lot of knowledge. Don't be afraid to ask the package maintainer for help.

It is up to the discretion of the package maintainer to decide whether images are too big or not. A major factor in this decision is whether the image is any bigger than strictly necessary.

Translating
----
Translating this guide is no small task and not something that the maintainer can do, so all help is welcome.

To translate articles, put translations in the `resources/languages` folder, in a subfolder named with the language code of the language you're translating into. Inside this folder, please keep the folder structure of the English folder (which sorts the articles by their category). This helps to keep articles easy to find online and while developing.

There are a few things to pay attention to though:
* Automatic (machine) translations are not allowed.
* The guide is intended to be shown within Cura as well as online on Github. This means that your translations will need to link correctly to images using relative paths.
* When linking to other articles, use relative links to the translated article of the same name, if such an article exists. If the linked article is not (yet) translated, link to the English article.
* You will generally not need to translate images, but all images containing text should be SVG images, which are text-based and should be easy to translate. Do not copy any images you're not translating.
* Do not translate the preferences file. While the helper text won't cause any harm, translating the labels of the preferences will cause them to stop working.

Don't be afraid to ask for help with translations. I have experience handling Cura's translations and did a lot of translating in my spare time.