from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from .utils import get_dicom_data, save_image

router = APIRouter()


@router.get("/dicom/patient")
async def get_dicom_patient():
    """
    Route to retrieve the patient name from a DICOM file.
    """
    data = get_dicom_data()
    return {"name": data["patient_name"]}


@router.get("/dicom/image")
async def get_dicom_image():
    """
    Route to retrieve the DICOM image.
    """
    data = get_dicom_data()
    image_bytes = save_image(data["pixel_data"])
    return StreamingResponse(image_bytes, media_type="image/png")
