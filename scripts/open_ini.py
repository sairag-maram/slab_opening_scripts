from src.io import load_ini_file

filepath = "path/to/your/config.ini"

config = load_ini_file(filepath)
print("Loaded INI config:")
for section, params in config.items():
    print(f"[{section}]")
    for key, value in params.items():
        print(f"{key} = {value}")
    print()
