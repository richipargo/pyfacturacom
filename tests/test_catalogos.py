import logging
import unittest
from datetime import datetime, timedelta
from os import path
import vcr
import facturacom
from facturacom.catalogos import Catalogos

LOG = logging.getLogger(__name__)

class TestCatalogos(unittest.TestCase):
    def setUp(self):
        facturacom.DEBUG = True
        facturacom.FACTURACOM_API_KEY = 'JDJ5JDEwJGlZTWhETVZpb01EMmk2REtZWC9EQi53UmhmYlN3TWVPT1N2M3J1U2hEREpibjMuZi80Qk5D'
        facturacom.FACTURACOM_SECRET_KEY = 'JDJ5JDEwJE5pMlRLZjF0NVh4QkdnTDFJQ3paZ2VPdmIuNm45SGc2YkFoalQ2Tm1sMkdEY295TDF1eWJH'

    def test_list_units(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_units.yaml'):
            catalogs = Catalogos.list_units()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'
