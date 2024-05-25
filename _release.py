import platform
import re
import shutil
import subprocess

def run_command(command: str):
    print("\n>>> " + command)
    if platform.system() == "Windows":
        command = [e.replace("__"," ") for e in command.split(" ")]
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        exit(1)


def update_version():
    with open("setup.py", "r") as fp:
        file = fp.read()

    ver = re.findall(r"version=['\"](\d+\.\d+\.\d+)['\"]", file)[0]
    name = re.findall(r"name=['\"](.*)['\"]", file)[0]

    new_ver = ver.split(".")
    new_ver[2] = str(int(new_ver[2]) + 1)
    new_ver = ".".join(new_ver)

    file = file.replace(
        f"version='{ver}'", f"version='{new_ver}'"
    ).replace(
        f'version="{ver}"', f'version="{new_ver}"'
    )
    with open("setup.py", "w") as fp:
        fp.write(file)

    return name, new_ver


if __name__ == "__main__":
    python_command = "python" if platform.system() == "Windows" else "python3"

    name, version = update_version()
    run_command(f"{python_command} setup.py sdist")
    run_command("twine upload dist/*")
    run_command(f"pip uninstall {name} -y")
    run_command(f"pip install {name}")

    shutil.rmtree("dist")
    shutil.rmtree(f"{name}.egg-info")

    run_command("git add .")
    run_command(f"git commit -m Version__released__:__{version}")
    run_command("git push")
