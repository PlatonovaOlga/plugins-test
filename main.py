#! usr/bin/python
import argparse
import importlib
import pkgutil

import plugins


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--param', type=str)
parser.add_argument('-o', '--option', default=None)


def iter_namespace(ns_pkg):
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def load_plugins():
    discovered_plugins = {
        name.split('.')[-1]: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(plugins)
    }
    return discovered_plugins


def main(param, option):
    plugins = load_plugins()

    if not param or param == 'help':
        print('Available plugins:')
        print('\n'.join(plugins.keys()))

    elif param in plugins.keys() and option in ['help', None]:
        doc = plugins.get(param).run.__doc__
        print(doc)

    elif param in plugins.keys():
        plugins.get(param).run(option)

    else:
        print('Failed to recognize command')


if __name__ == '__main__':
    args = parser.parse_args()
    main(args.param, args.option)
