from geopy.geocoders import Nominatim, GoogleV3
from geopy.exc import GeocoderTimedOut

def obtener_coordenadas(direccion, ciudad, pais="Argentina"):
    """
    Devuelve latitud y longitud con la máxima precisión disponible.
    """
    # Combinamos los datos para una búsqueda precisa
    query = f"{direccion}, {ciudad}, {pais}"
    
    # User_agent es obligatorio para Nominatim (puedes poner cualquier nombre)
    geolocator = Nominatim(user_agent="geo_app_rosario")
    
    # Si decides usar Google Maps (recomendado para precisión < 1m):
    # geolocator = GoogleV3(api_key='TU_API_KEY_AQUI')

    try:
        # 'addressdetails=True' ayuda a verificar que el número de puerta sea exacto
        location = geolocator.geocode(query, addressdetails=True, timeout=10)
        
        if location:
            return {
                "direccion_encontrada": location.address,
                "latitud": location.latitude,
                "longitud": location.longitude,
                "raw": location.raw # Contiene metadatos de precisión
            }
        else:
            return "No se encontraron resultados para esa dirección."

    except GeocoderTimedOut:
        return "Error: El servicio de geocodificación tardó demasiado."

# Ejemplo de uso:
direccion_test = "San Luis 2450"
ciudad_test = "Rosario"

resultado = obtener_coordenadas(direccion_test, ciudad_test)

if isinstance(resultado, dict):
    print(f"Dirección: {resultado['direccion_encontrada']}")
    print(f"Latitud: {resultado['latitud']}")
    print(f"Longitud: {resultado['longitud']}")
else:
    print(resultado)