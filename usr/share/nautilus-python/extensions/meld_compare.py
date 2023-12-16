import os
from gi.repository import Nautilus, GObject

class MeldExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        GObject.GObject.__init__(self)  # Initialize the GObject type system
        self.left_file = None
        self.left_dir = None

    def menu_activate_cb(self, menu, file1, file2):
        os.system(f"meld \"{file1}\" \"{file2}\" &")

    def set_left_cb(self, menu, file, is_directory):
        if is_directory:
            self.left_dir = file
        else:
            self.left_file = file

    def get_file_items(self, files):
        print(GObject._version)
        items = []

        if len(files) == 1:
            file = files[0]
            is_directory = file.is_directory()
            left = self.left_dir if is_directory else self.left_file

            if left:
                item = Nautilus.MenuItem(
                    name=f"MeldExtension::Compare_{'Dir' if is_directory else 'File'}",
                    label=f"Compare to '{left.get_name()}'",
                    tip=f"Compare selected {'directory' if is_directory else 'file'} with the left {'directory' if is_directory else 'file'} using Meld"
                )
                item.connect("activate", self.menu_activate_cb, left.get_location().get_path(), file.get_location().get_path())
                items.append(item)

            item = Nautilus.MenuItem(
                name=f"MeldExtension::Set_Left_{'Dir' if is_directory else 'File'}",
                label=f"Set as Left {'Directory' if is_directory else 'File'} to Compare",
                tip=f"Set selected {'directory' if is_directory else 'file'} as the left {'directory' if is_directory else 'file'} for comparison using Meld"
            )
            item.connect("activate", self.set_left_cb, file, is_directory)
            items.append(item)

        elif len(files) == 2:
            file1, file2 = files

            # If both are of the same type
            if file1.is_directory() == file2.is_directory():
                item = Nautilus.MenuItem(
                    name="MeldExtension::Compare_Two",
                    label=f"Compare Selected {'Directories' if file1.is_directory() else 'Files'}",
                    tip=f"Compare the two selected {'directories' if file1.is_directory() else 'files'} using Meld"
                )
                item.connect("activate", self.menu_activate_cb, file1.get_location().get_path(), file2.get_location().get_path())
                items.append(item)

        return items

