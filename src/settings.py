

def read_settings() -> dict:
    """
    Read settings from file.
    :return: dict
    """
    settings = {}
    file_path = 'src/settings.properties'
    with open(file_path) as file:
        lines = file.readlines()

        # UI TYPE 
        line = lines[0].strip()
        key, value = line.split('=')
        settings[key.strip()] = value.strip().lower()

        # BOARD SIZE
        line = lines[1].strip()
        key, value = line.split('=')
        settings[key.strip()] = [int(_) for _ in value.strip().split(',')]

    return settings