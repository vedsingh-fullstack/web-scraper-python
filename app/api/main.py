from fastapi import FastAPI
from endpoints.api import api_router
from fastapi_pagination import add_pagination


api = FastAPI(title="DNL API")


api.include_router(api_router)
add_pagination(api)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api, host="0.0.0.0", port=8001)