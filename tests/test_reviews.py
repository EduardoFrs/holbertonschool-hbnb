import unittest
from dataclasses import dataclass
from ..Model.user import User
from pydantic import BaseModel, ValidationError


@dataclass
class Review(BaseModel):
    user: User = None
    place: dict = None
    rating: float = None
    content: str = None


class TestReview(unittest.TestCase):

    def test_valid_review(self):
        user = User(name="John Doe")  # Assuming User definition
        review = Review(user=user, place={"name": "Restaurant X"}, rating=4.5, content="Great food!")
        self.assertIsInstance(review, Review)  # Check instance type
        self.assertEqual(review.user, user)
        self.assertEqual(review.place, {"name": "Restaurant X"})
        self.assertEqual(review.rating, 4.5)
        self.assertEqual(review.content, "Great food!")

    def test_missing_user(self):
        with self.assertRaises(ValidationError) as cm:
            Review(place={"name": "Cafe Y"}, rating=3.8, content="Nice coffee")
        self.assertEqual(str(cm.exception), '"user" is required')

    def test_invalid_rating(self):
        with self.assertRaises(ValidationError) as cm:
            Review(user=User(name="Jane Doe"), place={"name": "Park Z"}, rating=-1.0, content="Beautiful")
        self.assertIn('"rating" must be between 0 and 5', str(cm.exception))

    def test_empty_content(self):
        user = User(name="Alice")
        review = Review(user=user, place={"name": "Museum A"}, rating=4.2, content="")
        self.assertIsInstance(review, Review)  # Content can be empty
        self.assertEqual(review.content, "")

if __name__ == "__main__":
    unittest.main()
