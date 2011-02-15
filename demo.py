from activecollab.library import ACRequest
from sys import argv

try:
    item_id = argv[1]
except IndexError:
    item_id = None

try:
    subcommand = argv[2]
except IndexError:
    subcommand = None

try:
    sub_id = argv[3]
except IndexError:
    sub_id = None


req = ACRequest('projects', item_id=item_id, subcommand=subcommand, sub_id=sub_id)
print req.command_url
req.execute()

