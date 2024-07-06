from django.core.exceptions import ValidationError
from django.test import TestCase

from main_app.models import Customer


class CustomerModelValidationTest(TestCase):
    def test_zero_all_fields_invalid(self):
        """
        Zero test all fields should raise ValidationError.
        """
        customer = Customer(
            name="Svetlin Nakov1",
            age=17,
            email="nakov@example",
            phone_number="+35912345678",
            website_url="htsatps://nakov.com/"
        )
        with self.assertRaises(ValidationError) as error:
            customer.full_clean()

        exception = error.exception
        self.assertEqual(exception.message_dict['name'][0], 'Name can only contain letters and spaces')
        self.assertEqual(exception.message_dict['age'][0], 'Age must be greater than or equal to 18')
        self.assertEqual(exception.message_dict['email'][0], 'Enter a valid email address')
        self.assertEqual(
            exception.message_dict['phone_number'][0],
            "Phone number must start with '+359' followed by 9 digits"
        )
        self.assertEqual(exception.message_dict['website_url'][0], 'Enter a valid URL')