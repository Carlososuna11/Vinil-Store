# Vinyl Store

Utilizando la base de datos de demostración que tiene SQLite, la cual contiene datos de una aplicación de un sitio de música ficticio se  desea hacer una prueba de concepto para un sitio real. El dueño de la tienda real quiere construir una aplicación para lo cual contrata un equipo de desarrollo del cual usted forma parte. Su función en el equipo es la del desarrollo del backend.

En una primera fase se requiere que el API exponga algunos endpoints con la finalidad de ir haciendo la prueba de concepto. Es así que el API va a ser bastante sencillo y no tendrá funcionalidad de seguridad, en otras palabras no requiere que tenga funciones de chequeo de usuario y password, ni emisión de jwt o verificación usando Oauth2.

## Instrucciones

- Lee cuidadosamente todo el texto del proyecto antes de empezar a trabajar, si tiene alguna duda, consulte al profesor, según las condiciones al final del texto.

- EL proyecto **DEBE** ser desarrollado en Python, usando FastAPI para generar el API solicitado.

- Los endpoints que se requieren son:

    - Proporcione una lista artistas (nombre)
    
    - Proporcione una lista de los álbumes de un artista, seleccionándolo con el Id del artista.
    
    - Proporcione una lista de las canciones de un álbum, seleccionándolo con el Id del álbum.
    
    - Proporcione una lista de canciones de un artista, 
    seleccionándolo con el Id del artista
    
    - Proporcione el detalle completo (todos los campos de la tabla) de una canción, incluyendo el nombre del género musical y el nombre del tipo de media donde está localizado.

- Los nombres de los endpoints DEBEN SER LOS SIGUIENTES:
    
    - `music-store/api/v1/singers/` -> lista total de artistas.
    
    -  `music-store/api/v1/singers/{id}/` -> lista de álbumes de un artista.
    
    -  `music-store/api/v1/albums/{id}/` -> lista de canciones del álbum de un artista.
    
    - `music-store/api/v1/singer/{id}/` -> lista total de canciones de un artista.
    
    - `music-store/api/v1/song/{id}/` -> detalle de una canción por su id.

    **Importe**: no cambie los nombres de los endpoints, porque serán probados con una colección ya predefinida en Postman, ver en CONDICIONES en caso de que no funcione.

- La respuesta debe estar en formato JSON.

- La estructura de carpetas debe ser la misma que se ha usado en los ejemplo de clase.

- El proyecto debe correr en localhost:8000 y mostrar la documentación con el swagger
incorporado de FastAPI.

- No se ponga creativo, limítese a lo que solicita el proyecto

## Condiciones:

- La presentación del proyecto será individual.

- Se debe subir al sitio indicado en la pregunta respectiva del parcial en M7 el archivo con el proyecto empaquetado en un archivo zip o rar. Recuerde no agregar la carpeta contentiva del ambiente virtual, pero si el archivo con las dependencias.

- Se evaluará de la manera siguiente:
    - Ejecuta correctamente y muestra el swagger en localhost:8000/docs: 30%.

    - Se obtienen resultados correctos en cada endpoint que va a exponer al ser revisados con Postman: 30% (6% por cada uno de los endpoints).

    - Organización y estilo del código, revisado en el proyecto: 20%

    - Correcta documentación del código: 20%.

    - **Observación**: Si el proyecto no se ejecuta a la primera vez (primer apartado), sólo se evaluará lo referente a organización y documentación del código).

- **No se aceptarán entregas por correo ni del proyecto o del parcial**

- Los nombres de paquetes, módulos y variables a utilizar deben tener un nombre auto explicativo y en **inglés**. La documentación del código puede estar en español.

- El sistema debe ser auto-explicativo en el sentido que no se necesite un manual para ejecutarlo y la obtención de resultados.