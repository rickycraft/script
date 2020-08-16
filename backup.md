# Android backup on Linux

Backup your phone with custom options. Options _-o_ or _-e_ must be specified.

| Flag        | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| **-h**      | Print help messages.                                                |
| **-d**      | Delete file not present on dest.                                    |
| **-f FILE** | Only sync folder in FILE. One each line.                            |
| **-o OUT**  | Dest directory set to OUT. Exclusive with -e.                       |
| **-e**      | Dest directory from environment (ADB_SYNC_DEST). Exclusive with -o. |
| **-j**      | Clean clutter files.                                                |
| **-t**      | Update titanium.                                                    |
| **-D**      | Enable debug                                                        |
| **-i**      | Specify the device id                                               |
| **-l**      | Backup only by folder                                               |
| **-n**      | Dry run                                                             |

## Features to implement

-   check for device connected
-   check for adb sync
-   read from argument
-   destination folder
    -   read from arg
    -   read from env
    -   check validity
    -   check for _"/sdcard"_
-   read from file folders
-   hardcode clutter files
-   subprocess command
-   run command w/ debug or not
-   generate help
