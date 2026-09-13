"""Application-specific skills and instructions for the system prompt."""

def get_blender_skills() -> str:
    return """
   IMPORTANT - BLENDER MENU NAVIGATION: When interacting with menus (especially in apps like Blender), use the mouse to hover over or click the MAIN menu options to open them. However, for navigating SUB-MENUS, DO NOT use the mouse to hover or click on the sub-menu items, as moving the mouse often causes them to close. Instead, you MUST leave the mouse cursor where it is, and use the keyboard arrow keys (`up`, `down`, `left`, `right`) to navigate through the sub-menu options. ALWAYS take a `screenshot` to verify the correct sub-menu item is highlighted BEFORE pressing `enter` to select it.

   IMPORTANT - BLENDER HOTKEYS: In Blender, instead of clicking icons to move, scale, or rotate objects, ALWAYS use the keyboard hotkeys sequentially using `press_keys`. For example, to scale an object on the X axis by a factor of 2, pass the keys as a single comma-separated string to `press_keys` like this: `s, x, 2, enter` (do NOT type them as text or separate function calls). `g` is for move/grab, `s` is for scale, `r` is for rotate. Use the axes `x`, `y`, `z` to constrain movement. This is much more precise than using the mouse.
"""

def get_all_skills() -> str:
    """Return all application-specific skills combined."""
    return get_blender_skills()

