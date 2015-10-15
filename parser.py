#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import yaml
import traceback


class Parser():
    """
    Parse YAML file.
    """
    def __init__(self):
        self.nfs_server = None
        self.nfs_clients = None
        self.args = None

    def _parse_yaml(self, path):
        """
        Parse yaml file and return a dictionary.
        """
        try:
            with open(path, 'r') as stream:
                return yaml.load(stream)
        except IOError:
            print "Please provide correct file path."
            print "*"*50
            traceback.print_exc()

    def _set_properties(self):
        """
        Set properties based on the values listed in config file.
        """
        parsed_yaml = self._parse_yaml('nfs_options.yaml')['NFS_configuration']
        self.nfs_server = parsed_yaml['nfs-server']
        self.nfs_clients = parsed_yaml['nfs-clients']
        self.args = parsed_yaml['args']
