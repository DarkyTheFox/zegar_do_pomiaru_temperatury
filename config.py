import configparser

# if mode = 'write' create config.ini files
# else mode = 'read' read config files
mode = 'write'

config = configparser.ConfigParser()

if mode == 'write':
    config.add_section('debug_command')
    config.set('debug_command', 'display_print', 'True')
    config.set('debug_command', 'print_error', 'True')
    config.set('debug_command', 'shift_print', 'True')
    config.set('debug_command', 'clock_print', 'True')

    config.add_section('user_info')
    config.set('user_info', 'author', 'True')

    try:
        with open(r"/config.ini", 'w') as configfile:
            config.write(configfile)
    except:
        print("Error Write Config Files!!!")

elif mode == 'read':
    try:
        config.read("/config.ini")
    except:
        print("ERROR. Can't read files.")
        pass
    dbparam = config["debug_command"]
    user_info = config["user_info"]


