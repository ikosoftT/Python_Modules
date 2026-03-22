import sys
import site
import os

def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_env_name(path: str) -> str:
    return os.path.basename(path)
def main() -> None:
    py_path = sys.executable
    env_path = None
    if is_venv():
        env_path = sys.prefix
        env_name = get_env_name(env_path)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {py_path}")
        print(f"Virtual Enviroment: {env_name}")
        print(f"Enviroment Path: {env_path}")

        print("SUCESS: You're in an isolated environment!")
        print("Safe To install Packeges without affecting the global system.")

        try:
            paths = site.getsitepackages()
            if paths:
                print("Package installation path:")
                print(paths[0])
        except Exception:
            print("Could not retrieve site packeges path.")
    else:
        print("MATRIX STATUS: You 're still plugged in")
        print(f"Currnet Python: {py_path}")
        print(f"Virtual Enviroment: {env_path} detected") 

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install;")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env") 
        print("source matrix_env/bin/activate # On Unix") 
        print("matrix_env\\bin\\Scripts\\activate.bat # On Windows") 

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print('Error:', e)
