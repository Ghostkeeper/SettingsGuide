# Copyright (c) 2018 Ultimaker B.V.

#
# This file optimizers the plugin and inspect files in the resource folder
#

from typing import Dict
from PIL import Image

import shutil
from shutil import copyfile
import os.path
import glob
import json
class PluginInspection:

    def __init__(self):
        self._path_resources = "resources"
        self._path_images = "images"
        self._path_setting_i18n = "i18n"
        self._path_setting_json = "en_US"

                          #name  : path
        self.lanugages = {"en_US": "en_US"}
        self.all_settings_keys = []
        self.all_images_in_plugin = []

        self.fdmprinter_json_path = "/home/asasin/Documents/Cura_GitHub/Cura/resources/definitions/fdmprinter.def.json"


        # Max zoom image * scale factor (this value is taken average)
        # Max zoom_image is taken from GeneralTemplate.qml
        scale_factor = 1.25
        self.image_width_max = 700 * scale_factor
        self.image_height_max = 400 * scale_factor


    def startInspection(self) -> None:

        # Find all available settings in Cura
        self._defineAllCuraSettings()
        plugin_path = self._getPluginPath()

        # Inspect Images in plugin
        images_path = os.path.join(plugin_path, os.path.join(self._path_resources, self._path_images))
        self.checkImages(images_path)

        # Inspect Settings descriptions in the plugin
        setting_json_files_path = os.path.join(plugin_path, os.path.join(self._path_resources, self._path_setting_i18n, self._path_setting_json))
        self.checkSettingDescriptions(setting_json_files_path)
        
        # Optimize images size
        self.optimizeImagesSize(images_path, plugin_path)

    def optimizeImagesSize(self, images_path: str, plugin_path: str) -> None:
        print("Optimize images")

        opt_dir_images_path = os.path.join(plugin_path, os.path.join(self._path_resources, "images_opt"))

        # If the folder exist then delete it
        if os.path.exists(opt_dir_images_path):
            shutil.rmtree(opt_dir_images_path)

        os.mkdir(opt_dir_images_path)

        valid_extensions = ["jpg", "png"]

        all_image_files = glob.glob(os.path.join(images_path, '*'))

        original_total_size = 0
        optimized_total_size = 0
        for image_file in sorted(all_image_files):
            base_name = os.path.basename(image_file)
            extension = base_name.split('.')[-1]

            original_total_size += os.path.getsize(image_file)

            new_file_path = os.path.join(opt_dir_images_path, base_name)
            if extension in valid_extensions:
                img = Image.open(image_file)

                ratio = max(img.width / self.image_width_max, img.height / self.image_height_max)

                if ratio > 0:
                    new_width = int(img.width / ratio)
                    new_height = int(img.height / ratio)

                    img = img.resize((new_width, new_height), Image.ANTIALIAS)
                    img.save(new_file_path)
                else:
                    copyfile(image_file, new_file_path)

            else:
                copyfile(image_file, new_file_path)

            optimized_total_size += os.path.getsize(new_file_path)


        print("Finished images optimizing. Origina size {org_size}Kb and New Size {new_size}Kb"
              .format(org_size = original_total_size, new_size = optimized_total_size))



    def checkSettingDescriptions(self, json_files_path: str) -> None:
        print("Inspect Settings")

        not_valid_json_files = []
        not_valid_json_files_data = []

        for json_file in  glob.glob(os.path.join(json_files_path, '*.json')):

            base_name = os.path.basename(json_file)
            file_name_id = os.path.splitext(base_name)[0]

            if file_name_id not in self.all_settings_keys:
                not_valid_json_files.append(base_name)

            with open(json_file, 'r') as f:
                file_data = json.load(f)

                if "general" in file_data:
                    id = file_data["general"]["id"]
                    name = file_data["general"]["name"]
                    images = {}

                    if "images" in file_data["general"]:
                        images = file_data["general"]["images"].values()

                # check data in json
                if id != file_name_id or len(name) == 0:
                    not_valid_json_files_data.append(base_name)
                    continue # already has wrong data, no reason to continue this file inspections

                matches_images = [x for x in list(images) if x in self.all_images_in_plugin]

                if len(matches_images) != len(images):
                    not_valid_json_files_data.append(base_name)

        for file in not_valid_json_files_data:
            print("Unknown setting id: {json_file}".format(json_file=file))

        for file in not_valid_json_files_data:
            print("Wrong data in json file: {json_file}".format(json_file=file))


    def checkImages(self, images_path: str) -> None:
        print("Inspect Images")

        not_valid_images = []

        # Load images paths
        images_files = os.listdir(images_path)

        for file in images_files:
            file_name_parts = file.split("_")
            file_id = file_name_parts[:-1]
            image_id = "_".join(file_id)

            if image_id not in self.all_settings_keys:
                not_valid_images.append(image_id)

            self.all_images_in_plugin.append(file)

        for image in not_valid_images:
            print("Wrong Image: {img_id}".format(img_id = image))


    def _defineAllCuraSettings(self) -> None:
        print("Start searching settings in Cura ")

        with open(self.fdmprinter_json_path) as f:
            json_data = json.load(f)
            self._flattenAllSettings(json_data)

        print("Total setting keys: " + str(len(self.all_settings_keys)))

    def _flattenAllSettings(self, json_file: Dict[str, str]) -> None:
        for key, data in json_file["settings"].items():  # top level settings are categories
            self._flattenSettings(data["children"])  # actual settings are children of top level category-settings

    def _flattenSettings(self, settings: Dict[str, str]) -> None:
        for key, setting in settings.items():

            if "type" in setting and setting["type"] != "category":
                self.all_settings_keys.append(key)

            if "children" in setting:
                self._flattenSettings(setting["children"])

    def _getPluginPath(self) -> str:
        plugin_file_path = os.path.dirname(os.path.abspath(__file__))
        path_records = os.path.split(plugin_file_path)
        global_path = path_records[:-1]
        path = os.path.join(*global_path)
        return path

# if __name__ is "__main__":
#     print("Start plugin inspection")

try:
    plugin_inspector = PluginInspection()
    plugin_inspector.startInspection()
except Exception as e:
    print("Error, while inspecting the plugin occurred unexpected error: %s" % (str(e)))


