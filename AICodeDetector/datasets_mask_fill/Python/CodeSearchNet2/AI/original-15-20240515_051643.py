
    parser = argparse.ArgumentParser(description='MS Bot')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s'+ __version__)
    parser.add_argument('-c', '--config', default='config.json',
                        help='Path to configuration file')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Enable debug mode')
    parser.add_argument('-l', '--log', action='store_true',
                  