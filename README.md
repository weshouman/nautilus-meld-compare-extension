# Nautilus Meld Extension

## Overview

This Nautilus extension allows us to easily compare files and directories using the Meld comparison tool directly from the Nautilus context menu. The extension adds new menu items that let us set a "left" file or directory for comparison and then compare a "right" file or directory against it.

## Features

- Set a file or directory as the "left" item for comparison.
- Compare another file or directory as the "right" item against the previously set "left" item.
- Directly compare two selected files or directories.

## Installation

### Prerequisites

- Ubuntu (or any GNOME-based Linux distribution)
- Nautilus File Manager
- Python 3.x
- Meld
- Nautilus Python bindings (Install with `apt install python3-nautilus`)
- **For newer Ubuntu releases (e.g., 23.10)**: Modify the signature of `get_file_items` from `get_file_items(self, window, files)` to `get_file_items(self, files)` for compatibility. [Reference](https://github.com/nextcloud/desktop/issues/5041)

### Steps

1. Download the `nautilus-meld-diff-extension.deb` package.
2. Install the package:
    ```bash
    sudo dpkg -i nautilus-meld-diff-extension.deb
    ```
3. You may need to resolve dependencies:
    ```bash
    sudo apt-get -f install
    ```
4. Restart Nautilus to apply the changes:
    ```bash
    nautilus -q && nautilus --no-desktop
    ```
   (Alternatively, you can restart Nautilus manually at your convenience.)

## Usage

### Scenario 1

- Right-click on a file or directory and choose "Set as Left File to Compare" or "Set as Left Directory to Compare."
- Right-click on another file or directory to see an option to compare it to the previously set "left" item.

### Scenario 2

- Right-click on two files or two directories to compare both.


