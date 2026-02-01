import sys
from pathlib import Path
# ---- imports
from logic.backup import backup_zip
from logic.ins_hyprism import install_hyprism
from logic.ins_shortcut import ins_shortcut
# ----

def main():
    if len(sys.argv) > 1:
        install_dir = Path(sys.argv[1]).expanduser().resolve()
    else:
        install_dir = Path.home() / "Applications" / "HyPrism"

    app_file = install_dir / "HyPrism.AppImage"
    is_update = app_file.exists()

    if is_update:
        print(f"Update detected in {install_dir}")
        backup_zip(install_dir)

    try:
        app_path = install_hyprism(install_dir)

        if not is_update:
            ans = input("Do you want to create a desktop shortcut? [y/N]: ").lower()
            if ans in ('y', 'yes'):
                ins_shortcut(app_path, install_dir)
            else:
                print("Ok, skipping shortcuts.")
        else:
            # Always update shortcuts on update
            ins_shortcut(app_path, install_dir)

        print("Done!")

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()