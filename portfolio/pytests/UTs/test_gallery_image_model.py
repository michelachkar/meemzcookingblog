from django.test import TestCase
from django.core.exceptions import ValidationError
from portfolio.models.gallery_image import GalleryImage

class GalleryImageModelTest(TestCase):

    def test_create_gallery_image(self):
        # Test creating a valid GalleryImage instance
        gallery_image = GalleryImage.objects.create(
            alt="Sample Image",
            image="path/to/image.jpg",  # In a real test, this would point to an actual file or be mocked
        )
        # Assert that the gallery image's alt text is correctly set
        self.assertEqual(gallery_image.alt, "Sample Image")
        # Assert that the image field is set properly (indicating it was uploaded)
        self.assertTrue(gallery_image.image)

    def test_alt_text_optional(self):
        # Test that the alt text can be left empty (optional field)
        gallery_image = GalleryImage.objects.create(image="path/to/image.jpg")
        # Assert that the alt field is None when not provided
        self.assertIsNone(gallery_image.alt)

        # Test that setting the alt text to an empty string is valid
        gallery_image.alt = ""
        gallery_image.full_clean()  # No error should be raised when alt is empty

    def test_image_upload(self):
        # Test uploading an image (S3 storage)
        # Note: In real tests, this would require mocking the image upload or using a temporary file
        gallery_image = GalleryImage.objects.create(
            alt="Test Image",
            image="path/to/image.jpg",  # This simulates an image path
        )
        # Assert that the image field is set (i.e., image is successfully uploaded)
        self.assertTrue(gallery_image.image)

    def test_uploaded_at_auto_now_add(self):
        # Test that the 'uploaded_at' field is automatically set when a GalleryImage is created
        gallery_image = GalleryImage.objects.create(
            alt="Sample Image",
            image="path/to/image.jpg"
        )
        # Assert that the uploaded_at field is not None and correctly populated
        self.assertIsNotNone(gallery_image.uploaded_at)

    def test_max_length_constraints_for_alt(self):
        # Test that the alt text respects the maximum length constraint of 150 characters
        gallery_image = GalleryImage(
            alt="T" * 151,  # Exceed max length of 150 for alt text
            image="path/to/image.jpg",
        )
        # Assert that a ValidationError is raised when the alt text exceeds the max length
        with self.assertRaises(ValidationError):
            gallery_image.full_clean()

    def test_string_representation(self):
        # Test the __str__ method of the GalleryImage model
        # The string representation should return "Image for {alt text}"
        gallery_image = GalleryImage(alt="Sample Image", image="path/to/image.jpg")
        self.assertEqual(str(gallery_image), "Image for Sample Image")

    def test_empty_alt_text(self):
        # Test that an empty alt text does not raise any validation errors
        gallery_image = GalleryImage(alt="", image="path/to/image.jpg")
        gallery_image.full_clean()  # No error should be raised for empty alt text

    def test_image_required(self):
        # Test that the image field is required (cannot be null or empty)
        gallery_image = GalleryImage(alt="Sample Image", image=None)
        # Assert that a ValidationError is raised when no image is provided
        with self.assertRaises(ValidationError):
            gallery_image.full_clean()

    def test_empty_image(self):
        # Test that providing an empty string for the image path raises a validation error
        gallery_image = GalleryImage(alt="Sample Image", image="")
        # Assert that a ValidationError is raised when an empty string is provided as an image
        with self.assertRaises(ValidationError):
            gallery_image.full_clean()

    def test_deleting_gallery_image(self):
        # Test the behavior when a GalleryImage is deleted
        gallery_image = GalleryImage.objects.create(
            alt="Test Image", 
            image="path/to/image.jpg"
        )
        gallery_image_id = gallery_image.id
        # Delete the gallery image instance
        gallery_image.delete()
        # Assert that the gallery image is deleted by checking that it no longer exists
        with self.assertRaises(GalleryImage.DoesNotExist):
            GalleryImage.objects.get(id=gallery_image_id)

