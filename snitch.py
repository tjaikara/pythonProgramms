

import re
import sys
import time


odie = '/dotomi/odie -> /opt/dotomi/odie-201802.0.777-20180219.172726-7'
maestro = '/dotomi/maestro -> /opt/dotomi/maestro-201802.9.14826-20180220.213346-3'

bessy = '/dotomi/bessy -> /opt/dotomi/bessy-201802.13.15129-20180222.222805-7'

# capture the application information
APP_PATTERN = re.compile(r"(:?/opt)?(:?/dotomi/)?"
                         r"(?P<component>.+?)(?=-\d)-"
                         r"(?P<version>.+?\.)\.{0,1}"
                         r"(?P<master>MASTER?)?\.?"
                         r"(?P<increment>\d+)\.?"
                         r"(?P<snapshot>\d{3,6})?"
                         r"(?P<minor>\d{1})?-?"
                         r"(?P<mapr>MAPR)?")

"""
UTILITIES
"""
def format_variable(value, prefix, suffix):
    """compose the variable as needed"""
    if value is None:
        return ''
    else:
        return prefix + value + suffix


def compose_component_version(arr):
    """take an array of version flags and return a single string"""
    version = ''
    for item in arr:
        version += item
    return version



"""
MAIN FUNCTIONS
"""


def transform_component_version(symlink):
    """given a path, return the key value pair of component and version"""
    m = re.search(APP_PATTERN, symlink)
    component = format_variable(m.group('component'), '', '')
    version = format_variable(m.group('version'), '', '')
    master = format_variable(m.group('master'), '', '.')
    inc = format_variable(m.group('increment'), '', '')
    snapshot = format_variable(m.group('snapshot'), '.', '-SNAPSHOT')
    minor = format_variable(m.group('minor'), '.', '')
    mapr = format_variable(m.group('mapr'), '-', '')
    versionArgs = [version, master, inc, snapshot, minor, mapr]
    return component, compose_component_version(versionArgs)

def run():


    key, value = transform_component_version(maestro)
    print(key)
    print(value)

    key, value = transform_component_version(odie)
    print(key)
    print(value)

    key, value = transform_component_version(bessy)
    print(key)
    print(value)

def main():
    """main method"""
    while True:
        try:
            run()
            time.sleep(120)
        except KeyboardInterrupt:
            print ('You cancelled the operation.')
            sys.exit(0)

if __name__ == "__main__":
    main()