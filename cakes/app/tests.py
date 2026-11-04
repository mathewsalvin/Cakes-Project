from django.test import TestCase

from .serializers import CakeSerializer, CategorySerializer, ShapeSerializer, WeightSerializer


class SerializerConfigurationTests(TestCase):
    def test_model_serializers_validate_input(self):
        serializers = (CakeSerializer, CategorySerializer, ShapeSerializer, WeightSerializer)

        for serializer_class in serializers:
            with self.subTest(serializer=serializer_class.__name__):
                self.assertFalse(serializer_class(data={}).is_valid())
