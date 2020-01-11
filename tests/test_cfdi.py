import logging
import unittest
from datetime import datetime, timedelta
from os import path
import vcr
import facturacom
from facturacom.cfdi import Cfdi

LOG = logging.getLogger(__name__)

class TestCfdi(unittest.TestCase):
    def setUp(self):
        facturacom.DEBUG = True
        facturacom.FACTURACOM_API_KEY = 'JDJ5JDEwJGlZTWhETVZpb01EMmk2REtZWC9EQi53UmhmYlN3TWVPT1N2M3J1U2hEREpibjMuZi80Qk5D'
        facturacom.FACTURACOM_SECRET_KEY = 'JDJ5JDEwJE5pMlRLZjF0NVh4QkdnTDFJQ3paZ2VPdmIuNm45SGc2YkFoalQ2Tm1sMkdEY295TDF1eWJH'

    def test_list_all(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/list_all.yaml'):
            cfdis = Cfdi.list_all()
            LOG.debug(cfdis)
            assert cfdis['status'] == 'success'

    def test_create(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/create.yaml'):
            dat = datetime.now().replace(microsecond=0) - timedelta(hours=8)
            date_string = dat.isoformat()
            LOG.debug(dat)
            cfdi = Cfdi.create({
                "Receptor": {
                    "UID": "5a9c6ccb26e36",
                    "ResidenciaFiscal": "023203d",
                },
                "TipoDocumento":"factura",
                "Conceptos": [{
                    "ClaveProdServ": "25181608",
                    "NoIdentificacion": "SKU-12122",
                    "Cantidad": 10,
                    "ClaveUnidad": "E48",
                    "Unidad": "Unidad de servicio",
                    "ValorUnitario": 1500,
                    "Descripcion": 'Diseno de interfaces para sitio web',
                    "Descuento": 0,
                    "Impuestos": {
                        "Traslados": [{
                            "Base" : 15000,
                            "Impuesto": "002",
                            "TipoFactor": "Tasa",
                            "TasaOCuota": 0.16,
                            "Importe": 2400
                        }],
                        "Retenidos": [{
                            "Base" : 15000,
                            "Impuesto": "001",
                            "TipoFactor": "Tasa",
                            "TasaOCuota": 0.10,
                            "Importe": 1500
                        }],
                        "Locales": [{
                            "Impuesto": "ISH",
                            "TasaOCuota": 0.03
                        }]
                    },
                }],
                "UsoCFDI": "G02",
                "Serie":"1215",
                "FormaPago":"03",
                "MetodoPago": "PUE",
                "CondicionesDePago": "Pago en 10 dias",
                "Moneda": "MXN",
                "TipoCambio": 19.89,
                "NumOrder": "MY-Order-10",
                "FechaFromAPI": date_string,
                "Comentarios": "Comentarios para agregar a la factura PDF",
                "EnviarCorreo": False
            })
            LOG.debug(cfdi)
            assert cfdi['response'] == 'success'

    def test_cancel(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/cancel.yaml'):
            cfdi = Cfdi.cancel('5e19f24d6bb3c')
            LOG.debug(cfdi)
            assert cfdi['response'] == 'success'

    def test_xml(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/xml.yaml'):
            cfdi = Cfdi.xml('5e19f24d6bb3c')
            LOG.debug(cfdi.name)
            assert path.isfile(cfdi.name)

    def test_pdf(self):
        with vcr.use_cassette('fixtures/vcr_cassettes/cfdi/pdf.yaml'):
            cfdi = Cfdi.pdf('5e19f24d6bb3c')
            LOG.debug(cfdi.name)
            assert path.isfile(cfdi.name)
