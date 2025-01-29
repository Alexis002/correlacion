# Usar una imagen base oficial de Python
FROM python:3.12

# Instalar tzdata para configurar la zona horaria
RUN apt-get update && apt-get install -y --no-install-recommends tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer la zona horaria de Bogotá, Colombia
ENV TZ=America/Bogota
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias al contenedor
COPY requirements.txt .

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Comando para ejecutar el script principal
CMD ["python", "app/main.py"]
