import dmgbuild

# Set the paths and other parameters
volume_name = "FileOrganizer"
application_name = "FileOrganizer.app"
dmg_file = "FileOrganizer.dmg"

background_image = "background.png"  # Optional background image for the dmg
icon_file = "FileOrganizer.icns"  # Custom icon for the app

# Define the properties of the dmg
dmg_spec = {
    "volume_name": volume_name,
    "application_name": application_name,
    "dmg_file": dmg_file,
    "background_image": background_image,
    "icon_file": icon_file,
}

# Now use dmgbuild to create the dmg
dmgbuild.create_dmg(**dmg_spec)
