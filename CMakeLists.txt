#Copyright (C) 2019 Ghostkeeper
#This plug-in is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This plug-in is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for details.
#You should have received a copy of the GNU Affero General Public License along with this plug-in. If not, see <https://gnu.org/licenses/>.

project(SettingsGuide)
cmake_minimum_required(VERSION 3.10.2) #Oldest version it's been tested with.

#Project metadata.
set(SETTINGSGUIDE_PLUGIN_NAME "Settings Guide" CACHE STRING "The name of the plug-in in distribution.")
set(SETTINGSGUIDE_VERSION_MAJOR 1 CACHE STRING "The major version number, indicating a backward compatibility break.")
set(SETTINGSGUIDE_VERSION_MINOR 1 CACHE STRING "The minor version number, indicating a forward compatibility break.")
set(SETTINGSGUIDE_VERSION_PATCH 1 CACHE STRING "The patch version number, indicating an incremental improvement without compatibility break.")
set(SETTINGSGUIDE_SUPPORTED_SDKS "5.0.0;6.0.0" CACHE STRING "List of supported Cura SDK versions.")

#Installation.
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/plugin.json.in" plugin.json)
set(installed_files
	__init__.py
	CuraSettingsGuide.py
	LICENSE.md
	MenuItemHandler.py
	README.md
)
set(installed_files_resources_icons
	arrow.png
	createdBy.data
	icon.png
	play_icon.png
)
set(installed_files_resources_qml
	CreatedBy.qml
	SettingsGuide.qml
	SettingsSidebar.qml
)
set(installed_files_resources_qml_SidebarSettings
	SettingCategory.qml
	SettingCheckBox.qml
	SettingComboBox.qml
	SettingExtruder.qml
	SettingItem.qml
	SettingOptionalExtruder.qml
	SettingTextField.qml
	SettingUnknown.qml
)
set(installed_files_resources_qml_SidebarSettingTemplates
	EmptyTemplate.qml
	GeneralTemplate.qml
)
set(installed_paths "")
foreach(f IN LISTS installed_files)
	list(APPEND installed_paths ${CMAKE_CURRENT_SOURCE_DIR}/${f})
endforeach()
list(APPEND installed_paths ${CMAKE_CURRENT_BINARY_DIR}/plugin.json)
set(installed_paths_resources_icons "")
foreach(f IN LISTS installed_files_resources_icons)
	list(APPEND installed_paths_resources_icons ${CMAKE_CURRENT_SOURCE_DIR}/resources/icons/${f})
endforeach()
set(installed_paths_resources_qml "")
foreach(f IN LISTS installed_files_resources_qml)
	list(APPEND installed_paths_resources_qml ${CMAKE_CURRENT_SOURCE_DIR}/resources/qml/${f})
endforeach()
set(installed_paths_resources_qml_SidebarSettings "")
foreach(f IN LISTS installed_files_resources_qml_SidebarSettings)
	list(APPEND installed_paths_resources_qml_SidebarSettings ${CMAKE_CURRENT_SOURCE_DIR}/resources/qml/SidebarSettings/${f})
endforeach()
set(installed_paths_resources_qml_SidebarSettingTemplates "")
foreach(f IN LISTS installed_files_resources_qml_SidebarSettingTemplates)
	list(APPEND installed_paths_resources_qml_SidebarSettingTemplates ${CMAKE_CURRENT_SOURCE_DIR}/resources/qml/SidebarSettingTemplates/${f})
endforeach()
file(GLOB installed_paths_resources_descriptions ${CMAKE_CURRENT_SOURCE_DIR}/resources/descriptions/*)
file(GLOB installed_paths_resources_images ${CMAKE_CURRENT_SOURCE_DIR}/resources/images/*)

#Find out where to install this thing.
if(WIN32)
	set(cura_directory "$ENV{APPDATA}\\cura")
elseif(APPLE)
	set(cura_directory "$ENV{HOME}/Library/Application Support/cura")
else()
	set(cura_directory "$ENV{HOME}/.local/share/cura")
endif()
#Figure out the latest Cura release that's installed.
file(GLOB versions RELATIVE "${cura_directory}" "${cura_directory}/*")
set(latest_version 2.0)
foreach(version ${versions})
	if(IS_DIRECTORY "${cura_directory}/${version}")
		if(${version} VERSION_GREATER ${latest_version})
			set(latest_version ${version})
		endif()
	endif()
endforeach()
if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
	set(CMAKE_INSTALL_PREFIX "${cura_directory}/${latest_version}/plugins" CACHE PATH "Location of the Cura plug-ins folder to install this plug-in to." FORCE)
endif()
install(FILES ${installed_paths} DESTINATION SettingsGuide)
install(FILES ${installed_paths_resources_icons} DESTINATION SettingsGuide/resources/icons)
install(FILES ${installed_paths_resources_qml} DESTINATION SettingsGuide/resources/qml)
install(FILES ${installed_paths_resources_qml_SidebarSettings} DESTINATION SettingsGuide/resources/qml/SidebarSettings)
install(FILES ${installed_paths_resources_qml_SidebarSettingTemplates} DESTINATION SettingsGuide/resources/qml/SidebarSettingTemplates)
install(FILES ${installed_paths_resources_descriptions} DESTINATION SettingsGuide/resources/descriptions)
install(FILES ${installed_paths_resources_images} DESTINATION SettingsGuide/resources/images)

#Packing this into a .curapackage file.
add_custom_target(pack COMMAND "") #Packs for all supported SDK versions.
foreach(sdk_version ${SETTINGSGUIDE_SUPPORTED_SDKS})
	file(COPY ${installed_paths} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide)
	file(COPY ${installed_paths_resources_icons} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/icons)
	file(COPY ${installed_paths_resources_qml} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/qml)
	file(COPY ${installed_paths_resources_qml_SidebarSettings} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/qml/SidebarSettings)
	file(COPY ${installed_paths_resources_qml_SidebarSettingTemplates} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/qml/SidebarSettingTemplates)
	file(COPY ${installed_paths_resources_descriptions} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/descriptions)
	file(COPY ${installed_paths_resources_images} DESTINATION pack${sdk_version}/files/plugins/SettingsGuide/resources/images)
	file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/cmake/[Content_Types].xml" DESTINATION pack${sdk_version})
	file(COPY "${CMAKE_CURRENT_SOURCE_DIR}/cmake/_rels" DESTINATION pack${sdk_version})
	configure_file("${CMAKE_CURRENT_SOURCE_DIR}/cmake/package.json.in" pack${sdk_version}/package.json)
	set(packaged_files
		package.json
		[Content_Types].xml
		_rels
		files
	)
	add_custom_target(pack${sdk_version}
		COMMAND "${CMAKE_COMMAND}" -E tar cfv ../SettingsGuide${sdk_version}.curapackage --format=zip ${packaged_files}
		WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/pack${sdk_version}
	)
	add_dependencies(pack pack${sdk_version})
endforeach()

#Let CPack find it.
include(InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_VERSION_MAJOR ${SETTINGSGUIDE_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${SETTINGSGUIDE_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH ${SETTINGSGUIDE_VERSION_PATCH})
set(CPACK_PACKAGE_NAME ${SETTINGSGUIDE_PLUGIN_NAME})
set(CPACK_PACKAGE_DESCRIPTION_FILE ${CMAKE_CURRENT_SOURCE_DIR}/README.md)
set(CPACK_GENERATOR ZIP)
include(CPack)
