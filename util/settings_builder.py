from python_json_config import ConfigBuilder

SETTINGS_FILE = "config.json"


class Settings:
    """
    A class that represents the bot settings.

    Attributes:
        values: An object containing all settings.
    """

    def __init__(self):
        # create config parser
        self.builder = ConfigBuilder()

        # parse config
        self.values = self.builder.parse_config(SETTINGS_FILE)

        # check if valid color
        self.builder.validate_field_value('style.color',
                                     lambda color: len(color) == 3 and all(isinstance(x, int) for x in color))

    def save(self):
        """Writes the settings to the settings file"""
        with open(SETTINGS_FILE, 'w') as settings_file:
            settings_file.write(self.values.to_json())
