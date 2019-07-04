import os

try:
    from orbis.core.plugin_setup import PluginSetupBaseClass
    PluginSetupBaseClass().run(os.path.dirname(os.path.realpath(__file__)))
except Exception as exception:
    print("Orbis not found. Please install Orbis first.")
    print(f"({exception})")
