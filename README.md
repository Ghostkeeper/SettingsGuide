# CuraSettingsGuidePlugin

- GIF Guidelines
- Prepare Ultimaker Cura: White background, remove build plate.
- Prefered capture application: Giphy Capture
- Configure 640 * 480px record area
- Save as: Pixel size: 640px, frame rate 10fps
- Upload to exgif.com Gif, for optimization:
- IF timelapse applicable: Decrease length to ± 5seconds.
- Perform Lossy compression, 75-125.
- Perform transparency optimization, fuzz 3-10%.
- Save GIF


# Validate settings and prepare plugin for making Cura Plugin Package
1. Run python script 'optimizer.py' in DoNotIncludeToPackage, before it define file 'fdmprinter.def.json' location
2. The script will create a new folder resources/images_opt . This folder has all resized and optimized settings images
3. Delete 'resources/images' folder
4. Rename resources/images_opt to resources/images
5. Now you can create Cura Plugin package