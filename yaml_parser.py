import yaml, traceback


class YamlParser():
    def __init__(self):
        nfs_server = None
        nfs_clients = None
        args = None

    def parse_yaml(self, path):
        try:
            with open(path, 'r') as stream:
                return yaml.load(stream)
        except IOError:
            print "Please provide correct file path."
            print "*"*50
            traceback.print_exc()
            
    def set_properties(self):
        parsed_yaml = self.parse_yaml('nfs_options.yaml')['NFS_configuration']
        self.nfs_server = parsed_yaml['nfs-server']
        self.nfs_clients = parsed_yaml['nfs-clients']
        self.args = parsed_yaml['args']
