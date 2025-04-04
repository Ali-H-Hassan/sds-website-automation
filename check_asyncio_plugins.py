import sys
import pkg_resources

# Check all installed packages for asyncio-related names
asyncio_packages = [
    pkg.key for pkg in pkg_resources.working_set
    if "asyncio" in pkg.key.lower() or "async" in pkg.key.lower()
]

print("Installed asyncio-related packages:")
for pkg in asyncio_packages:
    print(f"- {pkg}")

# Check for pytest plugins
pytest_plugins = [
    pkg.key for pkg in pkg_resources.working_set
    if pkg.key.startswith("pytest-")
]

print("\nInstalled pytest plugins:")
for plugin in pytest_plugins:
    print(f"- {plugin}")