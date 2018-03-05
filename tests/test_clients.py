import logging
import unittest
import vcr
import facturacom
from facturacom.clients import Clients

LOG = logging.getLogger(__name__)

class TestClients(unittest.TestCase):
    def setUp(self):
        facturacom.DEBUG = True
        facturacom.FACTURACOM_API_KEY = 'JDJ5JDEwJGlZTWhETVZpb01EMmk2REtZWC9EQi53UmhmYlN3TWVPT1N2M3J1U2hEREpibjMuZi80Qk5D'
        facturacom.FACTURACOM_SECRET_KEY = 'JDJ5JDEwJE5pMlRLZjF0NVh4QkdnTDFJQ3paZ2VPdmIuNm45SGc2YkFoalQ2Tm1sMkdEY295TDF1eWJH'

    def test_list_all(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/clients/list_all.yaml'):
            clients = Clients.list_all()
            LOG.debug(clients)
            assert clients['status'] == 'success'

    def test_find(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/clients/find.yaml'):
            clients = Clients.find('TAMR92032229A')
            assert clients['status'] == 'success'

    def test_create(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/clients/create.yaml'):
            clients = Clients.create({
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
            assert clients['Data']['Contacto']['Nombre'] == 'Ricardo'
            assert clients['status'] == 'success'

    def test_update(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/clients/update.yaml'):
            clients = Clients.update('5a9c6ccb26e36', {
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
            assert clients['Data']['Contacto']['Nombre'] == 'Ricardo'
            assert clients['status'] == 'success'
