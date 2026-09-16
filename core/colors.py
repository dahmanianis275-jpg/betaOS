"""
ANSI color helpers for a beautiful terminal experience.
"""

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    ITALIC  = "\033[3m"
    UNDER   = "\033[4m"

    BLACK   = "\033[30m"
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"

    BG_BLACK   = "\033[40m"
    BG_RED     = "\033[41m"
    BG_GREEN   = "\033[42m"
    BG_YELLOW  = "\033[43m"
    BG_BLUE    = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN    = "\033[46m"
    BG_WHITE   = "\033[47m"

    # Bright
    BRIGHT_BLACK   = "\033[90m"
    BRIGHT_RED     = "\033[91m"
    BRIGHT_GREEN   = "\033[92m"
    BRIGHT_YELLOW  = "\033[93m"
    BRIGHT_BLUE    = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN    = "\033[96m"
    BRIGHT_WHITE   = "\033[97m"


def color(text: str, *codes: str) -> str:
    return "".join(codes) + str(text) + C.RESET


def bold(text: str) -> str:
    return color(text, C.BOLD)


def green(text: str) -> str:
    return color(text, C.GREEN)


def cyan(text: str) -> str:
    return color(text, C.CYAN)


def yellow(text: str) -> str:
    return color(text, C.YELLOW)


def red(text: str) -> str:
    return color(text, C.RED)


def blue(text: str) -> str:
    return color(text, C.BLUE)


def magenta(text: str) -> str:
    return color(text, C.MAGENTA)


def dim(text: str) -> str:
    return color(text, C.DIM)
