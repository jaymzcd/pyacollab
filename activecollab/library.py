import urllib
from activecollab.settings import API_KEY, AC_URL
from activecollab.constants import AC_COMMANDS
from activecollab.exceptions import ACCommandException

class ACRequest(object):

    def __init__(self, command, **kwargs):
        if (command not in AC_COMMANDS):
            raise ACCommandException('Not a valid command')

        self.command = command
        self.api_key = kwargs.get('api_key', API_KEY)
        self.ac_url = kwargs.get('ac_url', AC_URL)
        self.req_url = self.base_url()
        self.params = urllib.urlencode(kwargs.get('params', dict()))

    def base_url(self):
        return 'http://%s/api.php?token=%s&path_info=' % (self.ac_url, self.api_key)

    def execute(self):
        url = self.req_url + self.command
        if self.params:
            return '%s&%s' % (url, self.params)
        else:
            return url


