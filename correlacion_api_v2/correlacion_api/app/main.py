from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import correlacion

app = FastAPI()

# Añadir soporte para CORS y permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir las rutas del módulo correlacion
app.include_router(correlacion.router)

@app.get("/")
async def root():
    return {"message": "API de correlación funcionando correctamente"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
