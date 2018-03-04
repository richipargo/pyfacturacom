import logging
from facturacom.api_wrapper import ApiWrapper

LOG = logging.getLogger(__name__)

class Clients(object):
    """
    Manage clients from endpoints
    """
    def __init__(self):
        pass

    @staticmethod
    def list_all():
        """
        Get all Clients
        """
        LOG.debug('Start List all clients')
        return ApiWrapper.api_call('/clients', dict())
