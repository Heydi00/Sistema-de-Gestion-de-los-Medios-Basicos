from django.contrib.auth.models import User
from django.test import TestCase
from .models import *


# # Create your tests here.


class EntidadTestCase(TestCase):

    def setUp(self):
        Entidad.objects.create(nombreEntidad="Universidad de las Ciencias Informáticas", telefonoEntidad="78584871",
                               correoEntidad="uci@edu.cu")
        Entidad.objects.create(nombreEntidad="Universidad de la Habana", telefonoEntidad="74584872",
                               correoEntidad="uh@edu.cu")

    def test_entidad_create(self):
        # Las entidades son creadas correctamente
        ent1 = Entidad.objects.get(nombreEntidad="Universidad de las Ciencias Informáticas")
        ent2 = Entidad.objects.get(nombreEntidad="Universidad de la Habana")
        self.assertEqual(ent1.nombreEntidad, 'Universidad de las Ciencias Informáticas')
        self.assertEqual(ent2.telefonoEntidad, '74584872')
        self.assertEqual(ent2.correoEntidad, 'uh@edu.cu')
