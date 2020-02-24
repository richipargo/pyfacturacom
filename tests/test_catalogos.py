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

    def test_list_aduanas(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_aduanas.yaml'):
            catalogs = Catalogos.list_aduanas()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_units(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_units.yaml'):
            catalogs = Catalogos.list_units()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_payment_methods(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_payment_methods.yaml'):
            catalogs = Catalogos.list_payment_methods()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_taxes(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_taxes.yaml'):
            catalogs = Catalogos.list_taxes()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_currencies(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_currencies.yaml'):
            catalogs = Catalogos.list_currencies()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_countries(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_countries.yaml'):
            catalogs = Catalogos.list_countries()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_tax_configurations(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_tax_configurations.yaml'):
            catalogs = Catalogos.list_tax_configurations()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_relation_types(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_relation_types.yaml'):
            catalogs = Catalogos.list_relation_types()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'

    def test_list_cfdi_uses(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_cfdi_uses.yaml'):
            catalogs = Catalogos.list_cfdi_uses()
            LOG.debug(catalogs)
            assert catalogs['response'] == 'success'
