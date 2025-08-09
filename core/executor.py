import subprocess, colorama

def execute_command(args):
    if not args:
        return

    try:
        subprocess.run(args, check=True)
    except FileNotFoundError:
        print(f"[{colorama.Fore.LIGHTCYAN_EX}sea-shell{colorama.Fore.RESET}]: Command not found: {args[0]}")
        return
    except subprocess.CalledProcessError as e:
        print(f"[{colorama.Fore.LIGHTCYAN_EX}sea-shell{colorama.Fore.RESET}]: Command failed with exit code: {e.returncode}")
    except Exception as e:
        print(f"[{colorama.Fore.LIGHTCYAN_EX}sea-shell{colorama.Fore.RESET}]: An error occurred: {e}")
