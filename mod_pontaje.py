APP_NAME = "Generator Pontaje"
CATEGORY = "Resurse Umane"
DIRECTOR_SALVARE = "pontaje/output"


if __name__ == "__main__":
    import os
    import sys

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(BASE_DIR)  # schimbă directorul de lucru
    sys.path.append(BASE_DIR)


    from pontaje.ui import run_ui
    run_ui()
