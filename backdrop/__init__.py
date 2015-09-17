import os
import json

class Backdrop(dict):
    def __init__(self, project_name, directories=[]):
        directories.reverse()

        # first look into user's home directory
        directories.append(os.path.expanduser('~'))

        # then look into current directory
        directories.append(os.path.dirname(os.path.realpath(__file__)))

        directories.reverse()

        data = {}
        for directory in directories:
            file_name = "%s.json" % project_name
            file_path = os.path.join(directory, '.backdrop', file_name)
            if os.path.isfile(file_path):
                file = open(file_path)
                data.update(json.load(file))
                file.close()

        super(Backdrop, self).__init__(data)
