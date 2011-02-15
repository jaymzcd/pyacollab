import urllib
from xml.dom.minidom import parse
from activecollab.settings import API_KEY, AC_URL
from activecollab.constants import *
from activecollab.exceptions import ACCommandException

class ACRequest(object):
    """ Makes a request to your Active Collab site and executes
        commands with a given API key. The returned XML is
        then parsed and returned in usable form """

    def __init__(self, command, **kwargs):
        if (command not in AC_COMMANDS):
            raise ACCommandException('Not a valid command')

        self.command = command
        self.api_key = kwargs.get('api_key', API_KEY)
        self.ac_url = kwargs.get('ac_url', AC_URL)
        self.params = urllib.urlencode(kwargs.get('params', dict()))

    @property
    def base_url(self):
        """ Build our base API request URL"""
        return 'http://%s/api.php?token=%s&path_info=' % \
            (self.ac_url, self.api_key)

    @property
    def command_url(self):
        """ This url is the base of all executed commands """
        url = self.base_url + self.command
        if self.params:
            return '%s&%s' % (url, self.params)
        else:
            return url

    def execute(self):
        """ Make a request for the XML and parse the response """
        try:
            raw_xml = urllib.urlopen(self.command_url)
        except:
            raise ACCommandException('Could not execute command')

        xml = parse(raw_xml)
        items = xml.getElementsByTagName(AC_SUBCOMMAND[self.command])

        for item in items:
            output = ''
            for node in item.childNodes:
                if node.localName in AC_BASE_FIELDS:
                    output += node.childNodes[0].nodeValue + AC_FIELD_SEP

            if output:
                print output.rstrip(AC_FIELD_SEP)

