import re
import requests
from urllib.parse import urlparse, parse_qs

def find_cid_from_source(url):
    """
    Encuentra el CID en el código fuente de una página de Google Maps y lo formatea en un enlace.
    """
    try:
        print("Descargando código fuente...")
        
        # Obtener código fuente
        response = requests.get(url)
        response.raise_for_status()
        source_code = response.text

        # Buscar el valor de ludocid
        match = re.search(r'ludocid\\u003d(\d+)', source_code)
        if match:
            cid = match.group(1)
            return f"https://maps.google.com/maps?cid={cid}"
        else:
            print("No se encontró el CID en el código fuente.")
    except Exception as e:
        print(f"Error al procesar el código fuente: {e}")
    return None


def find_cid_from_sab_url(url):
    """
    Encuentra el CID desde la URL de un SAB en Google Maps y lo formatea en un enlace.
    """
    try:
        # Extraer los parámetros de la URL
        parsed_url = urlparse(url)

        # Buscar identificadores hexadecimales (0x...)
        match = re.findall(r'0x[a-fA-F0-9]+', parsed_url.path)
        if len(match) >= 2:
            hex_cid = match[1][2:]  # Eliminar "0x"
            # Convertir de hexadecimal a decimal
            cid = int(hex_cid, 16)
            return f"https://maps.google.com/maps?cid={cid}"
        else:
            print("No se encontraron identificadores hexadecimales en la URL.")
    except Exception as e:
        print(f"Error al procesar la URL: {e}")
    return None


# Ejemplo de uso
if __name__ == "__main__":
    print("Método 1: CID desde código fuente de Google Maps")
    url = input("Ingrese la URL del perfil en Google Maps: ").strip()
    cid_link = find_cid_from_source(url)
    if cid_link:
        print(f"El enlace del CID es: {cid_link}")
    else:
        print("Prueba otro método o verifica la URL.")

    print("\nMétodo 2: CID desde URL de SAB")
    sab_url = input("Ingrese la URL del SAB en Google Maps: ").strip()
    cid_link = find_cid_from_sab_url(sab_url)
    if cid_link:
        print(f"El enlace del CID es: {cid_link}")
    else:
        print("No se pudo encontrar el CID desde la URL.")
