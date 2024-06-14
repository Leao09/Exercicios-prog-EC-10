from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io
from logs.logger import setup_logger
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
logger = setup_logger('processamento-imagens')


@app.post("/images/upload", tags=["images"])
async def upload_image(image: UploadFile = File(...)):
    try:
        contents = await image.read()
        input_image = Image.open(io.BytesIO(contents)).convert("RGBA")
        output_image = remove(input_image)
        byte_arr = io.BytesIO()
        output_image.save(byte_arr, format="PNG")
        byte_arr = byte_arr.getvalue()
        logger.info('imagem enviada e processada')
        return StreamingResponse(io.BytesIO(byte_arr), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)