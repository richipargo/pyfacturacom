import logging
import unittest
import vcr
import facturacom
from facturacom.cfdi import Cfdi

LOG = logging.getLogger(__name__)

class TestClients(unittest.TestCase):
    def setUp(self):
        facturacom.DEBUG = True
        facturacom.FACTURACOM_API_KEY = 'JDJ5JDEwJGlZTWhETVZpb01EMmk2REtZWC9EQi53UmhmYlN3TWVPT1N2M3J1U2hEREpibjMuZi80Qk5D'
        facturacom.FACTURACOM_SECRET_KEY = 'JDJ5JDEwJE5pMlRLZjF0NVh4QkdnTDFJQ3paZ2VPdmIuNm45SGc2YkFoalQ2Tm1sMkdEY295TDF1eWJH'

    def test_list_all(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_all.yaml'):
            cfdis = Cfdi.list_all()
            assert cfdis['status'] == 'success'

    def test_create(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/create.yaml'):
            clients = Cfdi.create({
                'nombre': 'Ricardo',
                'apellidos': 'Tapia Mancera',
                'email': 'rtapia92@gmail.com',
                'telefono': '4433223322',
                'razons': 'Ricardo Tapia Mancera',
                'rfc': 'TAMR92032229A',
                'calle': 'Av. Castorena',
                'numero_exterior': '30',
                'numero_interior': '32',
                'codpos': '05000',
                'colonia': 'Cuajimalpa',
                'estado': 'Ciudad de Mexico',
                'ciudad': 'Ciudad de Mexico',
                'delegacion': 'Cuajimalpa'
            })
            LOG.debug(clients)
            assert clients['status'] == 'success'
