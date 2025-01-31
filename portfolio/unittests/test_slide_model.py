from django.test import TestCase
from portfolio.models.slide import Slide
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from django.core.exceptions import ValidationError

class SlideModelTest(TestCase):

    # Test that a Slide object can be created and saved successfully
    def test_slide_creation(self):
        # Prepare a sample image for testing (we use a dummy image for testing)
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",  # Mock file content
            content_type="image/jpeg"
        )
        
        # Create a new Slide instance
        slide = Slide.objects.create(
            title="Test Title",
            subtitle="Test Subtitle",
            paragraph="Test Paragraph",
            cta_1_text="Learn More",
            cta_1_link="http://example.com",
            cta_2_text="Sign Up",
            cta_2_link="http://example.com/signup",
            image=image,
            alt="Test Image Alt Text"
        )
        
        # Check if the slide was saved correctly
        self.assertEqual(slide.title, "Test Title")
        self.assertEqual(slide.subtitle, "Test Subtitle")
        self.assertEqual(slide.paragraph, "Test Paragraph")
        self.assertEqual(slide.cta_1_text, "Learn More")
        self.assertEqual(slide.cta_1_link, "http://example.com")
        self.assertEqual(slide.cta_2_text, "Sign Up")
        self.assertEqual(slide.cta_2_link, "http://example.com/signup")
        self.assertEqual(slide.alt, "Test Image Alt Text")
        self.assertTrue(slide.image.name.startswith('slider/test_image'))  # Check if image was uploaded properly
        self.assertIsInstance(slide.uploaded_at, datetime)  # Ensure 'uploaded_at' is a datetime object

    # Test that Slide fields with null/blank values are handled correctly
    def test_slide_with_null_fields(self):
        # Create a Slide with some empty fields (no null image here)
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",  # Mock file content
            content_type="image/jpeg"
        )

        # Create a Slide with some empty fields
        slide = Slide.objects.create(
            title="Test Title",
            subtitle="Test Subtitle",
            paragraph="Test Paragraph",
            cta_1_text=None,
            cta_1_link=None,
            cta_2_text=None,
            cta_2_link=None,
            image=image,  # Ensure image is provided
            alt=None
        )
        
        # Check if empty fields are correctly set to None
        self.assertIsNone(slide.cta_1_text)
        self.assertIsNone(slide.cta_1_link)
        self.assertIsNone(slide.cta_2_text)
        self.assertIsNone(slide.cta_2_link)
        self.assertIsNone(slide.alt)

    # Test the __str__ method of the Slide model
    def test_slide_str_method(self):
        # Create a slide
        slide = Slide.objects.create(
            title="Test Slide",
            subtitle="Subtitle for Test",
            paragraph="This is a paragraph for the test.",
            image=None
        )
        
        # Check if the string representation is correct
        self.assertEqual(str(slide), "Slider for Test Slide")
    
    # Test the image field upload functionality (ensuring it is stored in the correct location)
    def test_image_upload(self):
        # Create a Slide instance with an image
        image = SimpleUploadedFile(
            "test_upload.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        slide = Slide.objects.create(
            title="Test Slide with Image",
            subtitle="Subtitle",
            paragraph="Paragraph text",
            image=image,
            alt="Test image alt"
        )
        
        # Verify that the image is saved under the 'slider' directory in S3 storage
        self.assertTrue(slide.image.name.startswith('slider/test_upload'))

    # Test that the 'uploaded_at' field is automatically set
    def test_uploaded_at_field(self):
        # Create a slide without specifying 'uploaded_at'
        slide = Slide.objects.create(
            title="Auto Date Test",
            subtitle="Auto Subtitle",
            paragraph="Some Paragraph",
            image=None,
            alt="Alt Text"
        )
        
        # Check that 'uploaded_at' is not None and is a datetime
        self.assertIsInstance(slide.uploaded_at, datetime)
        self.assertIsNotNone(slide.uploaded_at)


    # Test the max_length validation for CharFields
    def test_max_length_validation(self):
        # Test max_length on `title`
        title = "A" * 151  # Exceeding max_length of 150
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        with self.assertRaises(ValidationError):
            slide = Slide(
                title=title,
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()  # Validate before saving

        # Test max_length on `subtitle`
        subtitle = "B" * 151
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle=subtitle,
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `paragraph`
        paragraph = "C" * 151
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph=paragraph,
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `cta_1_text`
        cta_1_text = "D" * 51  # Exceeding max_length of 50
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text=cta_1_text,
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `cta_1_link`
        cta_1_link = "http://" + "E" * 251  # Exceeding max_length of 255
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link=cta_1_link,
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `cta_2_text`
        cta_2_text = "F" * 51  # Exceeding max_length of 50
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text=cta_2_text,
                cta_2_link="http://example.com",
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `cta_2_link`
        cta_2_link = "http://" + "G" * 251  # Exceeding max_length of 255
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link=cta_2_link,
                image=image,
                alt="Alt Text"
            )
            slide.full_clean()

        # Test max_length on `alt`
        alt = "H" * 151  # Exceeding max_length of 150
        with self.assertRaises(ValidationError):
            slide = Slide(
                title="Valid Title",
                subtitle="Valid Subtitle",
                paragraph="Valid Paragraph",
                cta_1_text="Valid Text",
                cta_1_link="http://example.com",
                cta_2_text="Valid Text",
                cta_2_link="http://example.com",
                image=image,
                alt=alt
            )
            slide.full_clean()

    # Test blank and nullable fields
    def test_blank_and_nullable_fields(self):
        # Test Slide creation with null and blank fields (image is required, but other fields may be blank or null)
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",  # Mock file content
            content_type="image/jpeg"
        )
        slide = Slide.objects.create(
            title="Valid Title",
            subtitle="Valid Subtitle",
            paragraph="Valid Paragraph",
            cta_1_text=None,  # Nullable field
            cta_1_link="",  # Blank field
            cta_2_text=None,  # Nullable field
            cta_2_link="",  # Blank field
            image=image,  # Image is required
            alt=None  # Nullable field
        )
        
        # Check that nullable fields are correctly set to None
        self.assertIsNone(slide.cta_1_text)  # Nullable field
        self.assertEqual(slide.cta_1_link, "")  # Blank field (empty string)
        self.assertIsNone(slide.cta_2_text)  # Nullable field
        self.assertEqual(slide.cta_2_link, "")  # Blank field (empty string)
        self.assertIsNone(slide.alt)  # Nullable field

        # Test that the `cta_1_text` field can be blank (""), but not null
        slide_blank_cta = Slide.objects.create(
            title="Another Title",
            subtitle="Another Subtitle",
            paragraph="Another Paragraph",
            cta_1_text="",  # Blank field
            cta_1_link="http://example.com",
            cta_2_text="Sign Up",
            cta_2_link="http://example.com/signup",
            image=image,
            alt="Alt Text"
        )
        self.assertEqual(slide_blank_cta.cta_1_text, "")  # It can be blank but not null

        # Check if `cta_2_text` is set to None (nullable)
        slide_nullable_cta = Slide.objects.create(
            title="Yet Another Title",
            subtitle="Yet Another Subtitle",
            paragraph="Yet Another Paragraph",
            cta_1_text="Click Here",
            cta_1_link="http://example.com",
            cta_2_text=None,  # Nullable field
            cta_2_link="http://example.com/signup",
            image=image,
            alt="Alt Text"
        )
        self.assertIsNone(slide_nullable_cta.cta_2_text)  # Should be None

        # Test saving a slide with a blank alt field (should be allowed because blank=True)
        slide_blank_alt = Slide.objects.create(
            title="Title with Blank Alt",
            subtitle="Subtitle with Blank Alt",
            paragraph="Paragraph with Blank Alt",
            cta_1_text="Learn More",
            cta_1_link="http://example.com",
            cta_2_text="Sign Up",
            cta_2_link="http://example.com/signup",
            image=image,
            alt=""  # Blank field (empty string)
        )
        self.assertEqual(slide_blank_alt.alt, "")  # It can be blank

        # Test if a `null` field is actually saved as `None`
        slide_nullable = Slide.objects.create(
            title="Nullable Test Title",
            subtitle="Nullable Test Subtitle",
            paragraph="Nullable Test Paragraph",
            cta_1_text="Some Text",
            cta_1_link="http://example.com",
            cta_2_text="Nullable",
            cta_2_link="http://example.com/signup",
            image=image,
            alt=None  # Nullable field set to None
        )
        self.assertIsNone(slide_nullable.alt)  # The 'alt' field is allowed to be null
