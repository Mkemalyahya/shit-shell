import sys, os, colorama, subprocess

def exit(args):
    confirmation = input(f"{colorama.Fore.RED}Are you sure?{colorama.Fore.RESET} (Y/N): ")
    if not confirmation:
        return
    elif confirmation.lower() == 'y':
        sys.exit(0)
    elif confirmation.lower() == 'n':
        return

def echo(args):
    if not args[1:]:
        return
    print(" ".join(args[1:]))

def cd(args):
    if not args[1:]:
        os.chdir(os.path.expanduser('~'))
        return
    try:
        os.chdir(args[1])
    except FileNotFoundError:
        print(f"[{colorama.Fore.RED}cd{colorama.Fore.RESET}]: No such file or directory: {args[1]}")

def pwd(args):
    print(os.getcwd())

def clear(args):
    if args[1:]:
        print(f"[{colorama.Fore.RED}clear{colorama.Fore.RESET}]: Too many arguments!")
        return

    subprocess.run(["cls" if os.name == "nt" else "clear"], shell=True)

builtins_dict = {
    "exit": exit,
    "echo": echo,
    "cd": cd,
    "pwd": pwd,
    "cls": clear,
    "clear": clear,
}
