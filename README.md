# Google Maps CID Extractor

Este script permite extraer el **CID** (Customer ID) de un perfil empresarial de Google Maps (Google Business Profile) usando dos métodos diferentes. El CID se devuelve en formato de enlace que puedes usar directamente en Google Maps.

## Características

- Extrae el CID del código fuente de una página de Google Maps.
- Extrae el CID desde una URL de un negocio con área de servicio (SAB) en Google Maps.
- Genera un enlace directo en el formato: `https://maps.google.com/maps?cid=XXXXXX`.

## Requisitos

### Dependencias

- **Python 3.7+**
- **Bibliotecas necesarias**:
  - `requests`

### Instalación

1. Clona este repositorio o copia el script.
2. Instala las dependencias usando `pip`:

   ```bash
   pip install requests
