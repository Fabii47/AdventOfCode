import sys
import os

def main():
    day = sys.argv[1]
    os.system(path_to("code", day + ".py"))
    
def path_to(folder : str, file : str) -> str:
    current_path = os.path.abspath(__file__)        # File Path
    current_path = os.path.dirname(current_path)    # Folder Path
    return os.path.join(current_path, folder, file)

if __name__ == "__main__":
    main()