Reporting bugs
----
Please report bugs in the [issues page of this repository](https://github.com/Ghostkeeper/SettingsGuide/issues). Do not report bugs in the Cura repository; they will be closed there.

When reporting a bug, it helps to provide the following information:
* The version of SettingsGuide you're using.
* Cura's log file (see [Cura's readme](https://github.com/Ultimaker/Cura#logging-issues) for instructions on where to find that).

Requesting features
----
Feature requests are also welcome in the [issues page](https://github.com/Ghostkeeper/SettingsGuide/issues).

I intend to write descriptions for every setting in Cura, but this is a lot of work. If you'd like to request priority for certain settings, feel free to ask.

Submitting pull requests
----
Pull requests to the main code (QML, Python) are subject to the following requirements:
* It does not slow down behaviour significantly.
* The code style is similar to the rest of the code in this repository.
* Your code will be licensed under AGPL 3.0 like the rest of the code in this repository.

Pull requests to add descriptions for settings or improve current descriptions are also welcome. Please see the existing setting descriptions for examples.

When taking screenshots of the g-code, these are some instructions to ensure a consistent look throughout the plug-in.
* Before making a screenshot, remove the build plate shader so that the grid doesn't show up in your screenshot.
* Use the light theme of Cura when taking the screenshot.
* Don't use the compatibility mode of layer view.

In an effort to keep the download size of the plug-in manageable, care needs to be taken with .png images.
1. If the image is more than 1024 pixels wide or tall, please resize it to 1024 pixels.
2. Download [OptiPNG](http://optipng.sourceforge.net/).
3. Optimize your image by entering this in a terminal: `optipng -o7 -strip all my_image.png`

Animated images are even more prone to having large file sizes. The following steps should guide you to produce space-efficient animations:
1. Resize your image to 640x480 pixels at the most.
2. Use at most 256 colours (no multi-part GIFs).
3. If you have an animation that requires smooth motion, use at most 10fps. If you have an animation that just shows several stages or layers, limit your image to one frame per stage or layer.
4. Don't create animations of more than 5 seconds.
5. Download [FlexiGIF](https://create.stephan-brumme.com/flexigif-lossless-gif-lzw-optimization/).
6. Optimize your image by entering this in a terminal: `flexigif my_image.gif my_image_opt.gif`.
7. Delete the old image and rename the new `my_image_opt.gif` to have the original file name.

It is up to the discretion of the package maintainer to decide whether images are too big or not. A major factor in this decision is whether the image is any bigger than strictly necessary.