import logging
from facturacom.api_wrapper import ApiWrapper

LOG = logging.getLogger(__name__)

class Catalogos(object):
    """
    Manage catalogs from endpoints
    """
    def __init__(self):
        pass

    @staticmethod
    def list_units():
        """
        Get all units of measurment
        """
        return ApiWrapper.api_call('/v3/catalogo/ClaveUnidad', dict())
