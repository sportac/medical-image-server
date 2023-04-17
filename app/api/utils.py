import io
import os

import matplotlib.pyplot as plt
import pydicom


def get_dicom_data() -> dict:
    """
    Load DICOM data from a file and extract patient name and pixel data.

    Returns:
        Dict: A dictionary containing patient name and pixel data.
    """
    file_path = os.path.join(
        os.path.dirname(__file__), "..", "resources", "N2D_0002.dcm"
    )
    ds = pydicom.dcmread(file_path)
    data = {"patient_name": str(ds.PatientName), "pixel_data": ds.pixel_array}
    return data


def save_image(pixel_data):
    """
    Save a DICOM image to a file using matplotlib.

    Args:
        pixel_data: An array containing pixel data.
    """
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(pixel_data, cmap=plt.cm.gray)
    plt.axis("off")
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    return buffer
