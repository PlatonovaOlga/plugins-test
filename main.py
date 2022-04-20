#! usr/bin/python
import argparse
import importlib
import pkgutil

import plugins


def get_kwargs(plugins=None):
    help_txt = 'Plugin system for media processing.\n\nAvailable plugins:\n' + '\n'.join(plugins)

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=help_txt, 
        usage='main.py [-h] [plugin_name] [options]')

    parser.add_argument('-p', '--plugin')
    parser.add_argument('-o', '--options')
    
    return parser.parse_args()


def load_plugins():
    def iter_namespace(ns_pkg):
        return pkgutil.iter_modules(
            ns_pkg.__path__, 
            ns_pkg.__name__ + ".")

    my_plugins = {
        name.split('.')[-1]: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(plugins)
    }

    return my_plugins


def main(my_plugins, kwargs):
    pl = kwargs.plugin

    if pl not in my_plugins:
        print('Available plugins:')
        print('\n'.join(my_plugins))
        return

    my_plugins.get(pl).\
        main(kwargs.options)


if __name__ == '__main__':
    my_plugins = load_plugins()
    kwargs = get_kwargs(my_plugins)
    main(my_plugins, kwargs)
