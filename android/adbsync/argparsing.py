from typing import List
from dataclasses import dataclass
import argparse
import pathlib

@dataclass
class Args():
    logging_no_color: bool
    logging_verbosity_verbose: int
    logging_verbosity_quiet: int

    LOCAL: str
    ANDROID: str

    dry_run: bool
    copy_links: bool
    exclude: List[str]
    exclude_from: List[pathlib.Path]
    delete: bool
    delete_excluded: bool
    pull: bool
    force: bool
    show_progress: bool

    adb_bin: str
    adb_flags: List[str]
    adb_options: List[List[str]]

def get_args(docstring: str, version: str) -> Args:
    parser = argparse.ArgumentParser(description = docstring)
    parser.add_argument("--version",
        action = "version",
        version = version)

    parser_logging = parser.add_argument_group(title = "logging")
    parser_logging.add_argument("--no-color",
        help = "Disable colored logging (Linux only)",
        action = "store_true",
        dest = "logging_no_color")
    parser_logging_verbosity = parser_logging.add_mutually_exclusive_group(required = False)
    parser_logging_verbosity.add_argument("-v", "--verbose",
        help = "Increase logging verbosity: -v for debug",
        action = "count",
        dest = "logging_verbosity_verbose",
        default = 0)
    parser_logging_verbosity.add_argument("-q", "--quiet",
        help = "Decrease logging verbosity: -q for warning, -qq for error, -qqq for critical, -qqqq for no logging messages",
        action = "count",
        dest = "logging_verbosity_quiet",
        default = 0)

    parser.add_argument("LOCAL",
        help = "Local path")
    parser.add_argument("ANDROID",
        help = "Android path")

    parser.add_argument("-n", "--dry-run",
        help = "Perform a dry run; do not actually copy and delete etc",
        action = "store_true",
        dest = "dry_run")
    parser.add_argument("-L", "--copy-links",
        help = "Follow symlinks and copy their referent file / directory",
        action = "store_true",
        dest = "copy_links")
    parser.add_argument("--exclude",
        help = "fnmatch pattern to ignore relative to source (reusable)",
        action = "append",
        dest = "exclude",
        default = [])
    parser.add_argument("--exclude-from",
        help = "Filename of file containing fnmatch patterns to ignore relative to source (reusable)",
        metavar = "EXCLUDE_FROM",
        type = pathlib.Path,
        action = "append",
        dest = "exclude_from",
        default = [])
    parser.add_argument("--del",
        help = "Delete files at the destination that are not in the source",
        action = "store_true",
        dest = "delete")
    parser.add_argument("--delete-excluded",
        help = "Delete files at the destination that are excluded",
        action = "store_true",
        dest = "delete_excluded")
    parser.add_argument("--pull",
        help = "Pull ANDROID from Android to LOCAL on the computer instead of the default pushing from computer to Android",
        action = "store_true",
        dest = "pull")
    parser.add_argument("--force",
        help = "Allows files to overwrite folders and folders to overwrite files. This is false by default to prevent large scale accidents",
        action = "store_true",
        dest = "force")
    parser.add_argument("--show-progress",
        help = "Show progress from 'adb push' and 'adb pull' commands",
        action = "store_true",
        dest = "show_progress")

    parser_adb = parser.add_argument_group(title = "ADB arguments",
        description = "By default ADB works for me without touching any of these, but if you have any specific "
        "demands then go ahead. See 'adb --help' for a full list of adb flags and options")
    parser_adb.add_argument("--adb-bin",
        help = "Use the given adb binary. Defaults to 'adb' ie whatever is on path",
        dest = "adb_bin",
        default = "adb")
    parser_adb.add_argument("--adb-flag",
        help = "Add a flag to call adb with, eg '--adb-flag d' for adb -d, that is return an error if more than one device is connected",
        metavar = "ADB_FLAG",
        action = "append",
        dest = "adb_flags",
        default = [])
    parser_adb.add_argument("--adb-option",
        help = "Add an option to call adb with, eg '--adb-option P 5037' for adb -P 5037, that is use port 5037 for the adb server",
        metavar = ("OPTION", "VALUE"),
        nargs = 2,
        action = "append",
        dest = "adb_options",
        default = [])

    args = parser.parse_args()

    args = Args(
        args.logging_no_color,
        args.logging_verbosity_verbose,
        args.logging_verbosity_quiet,

        args.LOCAL,
        args.ANDROID,

        args.dry_run,
        args.copy_links,
        args.exclude,
        args.exclude_from,
        args.delete,
        args.delete_excluded,
        args.pull,
        args.force,
        args.show_progress,

        args.adb_bin,
        args.adb_flags,
        args.adb_options
    )

    return args
