import unittest
from unittest.mock import MagicMock

from pydantic import ValidationError
from ..Model.countries import Country
from ..Model.cities import City
from ..Model.amenities import Amenity
from ..Model.reviews import Review
from typing import List
from ..Model.places import Place


class TestPlace(unittest.TestCase):

    def test_valid_place(self):
        city_mock = MagicMock()
        country_mock = MagicMock()
        amenity1 = Amenity(name="Wi-Fi")
        place = Place(
            id="abc123",
            name="Cozy Cabin",
            description="A charming getaway in the woods.",
            address="123 Forest Lane",
            city=city_mock,
            country=country_mock,
            host_id=123,
            number_of_rooms=2,
            number_of_bathrooms=1,
            price_per_night=100.50,
            max_guests=4,
            amenities=[amenity1],
        )
        self.assertIsInstance(place, Place)
        self.assertEqual(place.id, "abc123")
        # ... (Assert other attributes)

    def test_missing_id(self):
        with self.assertRaises(ValidationError) as cm:
            Place(
                name="Modern Apartment",
                description="Spacious city living.",
                address="456 Main St",
                city=MagicMock(),
                country=MagicMock(),
                host_id=456,
                number_of_rooms=1,
                number_of_bathrooms=1,
                price_per_night=150.00,
                max_guests=2,
                amenities=[],
            )
        self.assertEqual(str(cm.exception), '"id" is required')

    def test_invalid_price(self):
        with self.assertRaises(ValidationError) as cm:
            Place(
                id="def456",
                name="Beach House",
                description="Relax by the ocean.",
                address="789 Beach Rd",
                city=MagicMock(),
                country=MagicMock(),
                host_id=789,
                number_of_rooms=3,
                number_of_bathrooms=2,
                price_per_night=-25.0,  # Negative price
                max_guests=6,
                amenities=[],
            )
        self.assertIn('"price_per_night" must be a value greater than or equal to 0', str(cm.exception))

    def test_optional_fields(self):
        place = Place(
            id="ghi789",
            name="Mountain Retreat",
            address="012 Mountain View",
            city=MagicMock(),
            country=MagicMock(),
            host_id=1011,
            number_of_rooms=4,
            number_of_bathrooms=3,
            price_per_night=200.75,
            max_guests=8,
            amenities=[],
            reviews=[],  # Empty reviews list is allowed
        )
        self.assertIsInstance(place, Place)
        # ... (Assert specific optional attributes)


if __name__ == "__main__":
    unittest.main()
