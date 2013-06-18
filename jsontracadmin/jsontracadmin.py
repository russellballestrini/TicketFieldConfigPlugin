from trac.core import *
from trac.admin import IAdminCommandProvider
from trac.util.text import printout

# needed to dumps
import json

# import each of the panels we would like to support
from trac.ticket.admin import PriorityAdminPanel
from trac.ticket.admin import SeverityAdminPanel
from trac.ticket.admin import TicketTypeAdminPanel
from trac.ticket.admin import ResolutionAdminPanel

# Need the following to create list of [(component,owner),...]
from trac.ticket.model import Component as TicketComponent
from trac.util.translation import _

class JsonAdminCommandProvider(Component):
    implements(IAdminCommandProvider)
    
    # IAdminCommandProvider methods

    def get_admin_commands(self):
        #yield ('command regex', '<arg>',
        #       'trac-admin help text',
        #       self.tab_complete_callback, self.command_callback)
        yield ('priority json list', None,
               'Show possible ticket priorities in json',
               None, self._list_priority_in_json)
        yield ('severity json list', None,
               'Show possible ticket severities in json',
               None, self._list_severity_in_json)
        yield ('resolution json list', None,
               'Show possible ticket resolutions in json',
               None, self._list_resolution_in_json)
        yield ('ticket_type json list', None,
               'Show possible ticket types in json',
               None, self._list_ticket_type_in_json)
        yield ('component json list', None,
               'Show available components in json',
               None, self._list_component_in_json)

    # the following methods list various enums in json

    def _list_priority_in_json(self):
        panel = PriorityAdminPanel(self.env)
        printout(json.dumps(panel.get_enum_list()))
     
    def _list_severity_in_json(self):
        panel = SeverityAdminPanel(self.env)
        printout(json.dumps(panel.get_enum_list()))
     
    def _list_resolution_in_json(self):
        panel = ResolutionAdminPanel(self.env)
        printout(json.dumps(panel.get_enum_list()))
     
    def _list_ticket_type_in_json(self):
        panel = TicketTypeAdminPanel(self.env)
        printout(json.dumps(panel.get_enum_list()))
     
    def _list_component_in_json(self):
        # stolen from trac.ticket.admin.py format: [(component,owner)]
        components = [(c.name, c.owner) for c in TicketComponent.select(self.env)], [_('Name'), _('Owner')]
        printout(components)
   