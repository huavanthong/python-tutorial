import subprocess

# Đọc file requirements.txt
with open('requirements.txt', 'r') as file:
    packages = file.readlines()

# Gỡ bỏ từng package
for package in packages:
    package = package.strip()
    if package:
        subprocess.call(['pip', 'uninstall', '-y', package])
