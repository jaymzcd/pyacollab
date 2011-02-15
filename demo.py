from activecollab.library import ACRequest

req = ACRequest('people')
print req.command_url
req.execute()

