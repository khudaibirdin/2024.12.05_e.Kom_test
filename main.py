from fastapi import FastAPI
from app.web.form_detector.handler import router as form_detector_router


app = FastAPI()

app.include_router(form_detector_router)
