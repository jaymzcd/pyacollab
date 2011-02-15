# These are the 'top level' commands available
AC_COMMANDS = ('projects', 'people', 'discussions', 'calendar')

# The following is a list of sub elements of the main
# command XML which is returned
AC_SUBCOMMAND = {
    'projects': 'project',
    'people': 'company',
    'discussions': 'topic',
}

# These fields are common throughout XML responses so we
# grab these for all items as a good start
AC_BASE_FIELDS = ('id', 'name')

# Used in printing output
AC_FIELD_SEP = ': '