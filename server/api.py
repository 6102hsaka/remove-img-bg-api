from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove

app = FastAPI(
    title="RemoveImgBg",
    description="Using this API, user can easily remove background of any image",
    version="0.0.1",
    contact={
        "name": "Akash Sharma",
        "url": "https://akash-sharma-portfolio.web.app/",
        "email": "akashsharma15105@gmail.com",
    }
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg")
def remove_bg(file: UploadFile = File(...)):
  input_image = file.file.read()
  output_image = remove(input_image)
  return Response(content=output_image, media_type="image/png")