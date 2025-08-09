from core import executor, parser, builtins
import sys, colorama


running = True

while running:
    try:
        u_input = input(f"{colorama.Fore.YELLOW}shit-shell{colorama.Fore.RESET} >> ")
        if not u_input:
            continue

        tokens = parser.tokenize_input(u_input)
        command = tokens[0]

        if command in builtins.builtins_dict.keys():
            builtins.builtins_dict[command](tokens)

        else:
            executor.execute_command(tokens)

    except KeyboardInterrupt:
        print('\n')
        continue
    except EOFError:
        sys.exit(0)
