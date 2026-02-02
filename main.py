import sys
from pathlib import Path
# ---- imports
from logic.backup import backup_zip
from logic.ins_hyprism import install_hyprism
from logic.ins_shortcut import ins_shortcut
from logic.dp import dp
from parser import parser_argv
# ----

def main():
    config = parser_argv(sys.argv[1:])

    install_dir = (
        config["install_dir"]
        if config["install_dir"]
        else Path.home() / "Applications" / "HyPrism"
    )

    if dp(config):
        return

    app_file = install_dir / "HyPrism.AppImage"
    is_update = app_file.exists()

    if is_update:
        print(f"Update detected in {install_dir}")
        if config["no_backup"]:
            print("Skipping backup (--no-backup)")
        else:
            backup_zip(install_dir)

    try:
        app_path = install_hyprism(install_dir)
        # if no_shortcut == True: skip
        if not is_update and not config["no_shortcut"]:
            ans = input("Do you want to create a desktop shortcut? [y/N]: ").strip().lower()
            if ans in ("y", "yes"):
                ins_shortcut(app_path, install_dir)
            else:
                print("Ok, skipping shortcuts.")
        else:
            print("Skipping shortcuts.")

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()