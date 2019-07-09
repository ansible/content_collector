from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        module_name = self._task.args.get('module')
        # new_module_args = self._task.args.copy()
        # new_module_args.pop('ansible_network_os')
        new_module_args = {}
        result.update(self._execute_module(module_name=module_name,
                                           module_args=new_module_args,
                                           task_vars=task_vars,
                                           tmp=tmp))
        return result
