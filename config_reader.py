import json
from operations import OPERATIONS

DEFAULT_CONDITION = 'equal'
DEFAULT_REFERENCE = 'HTML'
DEFAULT_TIMING = 10


class ConfigReader(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.config = json.load(f)

    def get_configurations(self):
        urls, conds, refs, timings = [], [], [], []
        for key, options in self.config.iteritems():
            urls.append(key)
            conds.append(OPERATIONS[options.get('condition', DEFAULT_CONDITION)])
            refs.append(options.get('reference', DEFAULT_REFERENCE))
            timings.append(options.get('timing', DEFAULT_TIMING))
        return urls, conds, refs, timings
