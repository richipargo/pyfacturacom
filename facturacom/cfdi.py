import logging
from facturacom.api_wrapper import ApiWrapper

LOG = logging.getLogger(__name__)

class Cfdi(object):
    """
    Manage cfdi from endpoints
    """
    def __init__(self):
        pass

    @staticmethod
    def list_all():
        """
        Get all cfdi's
        """
        return ApiWrapper.api_call('/v3/cfdi33/list', dict())

    @staticmethod
    def create(data):
        """
        Creates cfdi from api
        """
        return ApiWrapper.api_call('/v3/cfdi33/create', data, 'POST')
