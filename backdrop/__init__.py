import os
import json

class Backdrop(dict):
    def __init__(self, project_name):
        home_dir = os.path.expanduser('~')
        file_name = "%s.json" % project_name
        file_path = os.path.join(home_dir, '.backdrop', file_name)
        file = open(file_path)
        data = json.load(file)
        super(Backdrop, self).__init__(data)
