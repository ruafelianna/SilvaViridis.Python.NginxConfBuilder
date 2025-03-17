from enum import Enum

from .Path import Path
from .Size import Size
from .TimeInterval import TimeInterval
from .TimeIntervalGroup import TimeIntervalGroup

class BuildArgsHelper:
    @staticmethod
    def str_empty(
        value : str | None,
    ) -> bool:
        return value is None or len(value) == 0 or value.isspace()

    @staticmethod
    def add_enum_value(
        args : list[str],
        enum_obj : Enum | None,
    ) -> None:
        if enum_obj is not None:
            args.append(str(enum_obj.value))

    @staticmethod
    def add_str_value(
        args : list[str],
        value : str,
    ) -> None:
        if not BuildArgsHelper.str_empty(value):
            args.append(value)

    @staticmethod
    def add_path(
        args : list[str],
        path : Path,
    ) -> None:
        args.append(path.value)

    @staticmethod
    def add_time(
        args : list[str],
        time : TimeInterval | TimeIntervalGroup,
    ) -> None:
        args.append(str(time))

    @staticmethod
    def add_size(
        args : list[str],
        time : Size,
    ) -> None:
        args.append(str(time))
