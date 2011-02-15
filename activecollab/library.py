import urllib
from xml.dom.minidom import parse
from activecollab.settings import API_KEY, AC_URL
from activecollab.constants import AC_COMMANDS, AC_SUBCOMMAND
from activecollab.exceptions import ACCommandException

class ACRequest(object):

    def __init__(self, command, **kwargs):
        if (command not in AC_COMMANDS):
            raise ACCommandException('Not a valid command')

        self.command = command
        self.api_key = kwargs.get('api_key', API_KEY)
        self.ac_url = kwargs.get('ac_url', AC_URL)
        self.params = urllib.urlencode(kwargs.get('params', dict()))

    @property
    def base_url(self):
        return 'http://%s/api.php?token=%s&path_info=' % \
            (self.ac_url, self.api_key)

    @property
    def command_url(self):
        url = self.base_url + self.command
        if self.params:
            return '%s&%s' % (url, self.params)
        else:
            return url

    def execute(self):
        try:
            raw_xml = urllib.urlopen(self.command_url)
        except:
            raise ACCommandException('Could not execute command')

        xml = parse(raw_xml)
        items = xml.getElementsByTagName(AC_SUBCOMMAND[self.command])

        for item in items:
            for node in item.childNodes:
                if node.localName == 'name':
                    print node.childNodes[0].nodeValue

