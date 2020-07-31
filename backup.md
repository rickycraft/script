# Android backup on Linux

Backup your phone with custom options. Options *-o* or *-e* must be specified.

| Flag        | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| **-h**      | Print help messages.                                                |
| **-d**      | Delete file not present on dest.                                    |
| **-f FILE** | Only sync folder in FILE. One each line.                            |
| **-o OUT**  | Dest directory set to OUT. Exclusive with -e.                       |
| **-e**      | Dest directory from environment (ADB_SYNC_DEST). Exclusive with -o. |
| **-c**      | Clean clutter files.                                                |
| **-t**      | Update titanium.                                                    |
| **-D**      | Enable debug                                                        |

## Features to implement

- check for device connected
- check for adb sync
- read from argument
- destination folder
	- read from arg
	- read from env
	- check validity
	- check for *"/sdcard"*
- read from file folders
- hardcode clutter files
- subprocess command
- run command w/ debug or not
- generate help