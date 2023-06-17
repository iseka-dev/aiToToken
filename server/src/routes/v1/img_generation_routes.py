from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse


from src.core.logger import log
from src.services.v1.images_service import ImageGeneratorService


img_generation_routes = APIRouter(
    prefix="/v1/generate-img",
    tags=["generate_image"]
)


@img_generation_routes.post("/", response_class=HTMLResponse)
async def generate_image_openai(request: Request):
    try:
        return await ImageGeneratorService().generate_image(request)
    except Exception as e:
        log.error(f"generate_openai_image-E01: {e}")
        error = f"Error at img generation: {e}"
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"Error": error},
    )
