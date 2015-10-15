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

import logging

from i18n import _

import paramiko


class NfsAuto():

    def __init__(self):
        self.hosts = {}


class Server():

    def __init__(self, host, username, password, **kwargs):
        self.host = host
        self.username = username
        self.password = password
        self.ssh_args = kwargs

    def ssh_connect(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.username,
                        password=self.password, **self.ssh_args)
            return ssh
        except Exception as e:
            logging.error(e)

    def identify_host(self, ssh):
        try:
            stdin, stdout, stderr = ssh.exec_command("cat /etc/issue")
            return stdout.readlines()[0].split(" ")[0]
        except Exception as e:
            msg = (_("Unable to identify the distribution of host %s")
                   % self.host)
            logging.error(msg)
            logging.error(e)
