from pathlib import Path
from colorama import init, Fore, Style 
import sys



def print_tree(path, indent=''):
        for item in path.iterdir():
             if item.is_dir():
                print(Fore.BLUE + indent + item.name + "/")
                print_tree(item, indent + "    ")
             else:
              print(Fore.GREEN + indent + item.name)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <directory_path>")
        return 
    root_path = Path(sys.argv[1])
    if not root_path.exists():
        print(f'Directory {root_path} not found!')
        return
    if not root_path.is_dir():
        print(f'{root_path} is not a directory!')
        return
    
    init(autoreset=True)

    print(Fore.BLUE + root_path.name + '/')
    print_tree(root_path)



if __name__ == '__main__':
     main()


          