from app.api.utils import get_dicom_data, save_image


def test_get_dicom_data():
    # Load DICOM data
    data = get_dicom_data()
    # Test that the patient name is not empty
    assert data["patient_name"] != ""
    # Test that the pixel data is not empty
    assert data["pixel_data"].size != 0


def test_save_image():
    # Create some sample pixel data
    pixel_data = [[1, 2], [3, 4]]
    # Save the image
    buffer = save_image(pixel_data)
    # Test that the buffer is not empty
    assert buffer.getvalue() != b""
