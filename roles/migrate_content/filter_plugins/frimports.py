import re

def frimports(file, frimports, builtins):
    with open(file, "r") as source:
        contents = source.readlines()
    for line in contents:
        cap = re.match(r"^(from|import) ansible.module_utils.(?P<file>[^. ]+)\s",
                       line)
        if cap:
            capdict = cap.groupdict()
            if capdict['file'] not in frimports:
                if capdict['file'] not in builtins:
                    frimports[capdict['file']] = None
    return frimports

class FilterModule(object):

    filter_map = {
        'frimports': frimports,
    }

    def filters(self):
        return self.filter_map
