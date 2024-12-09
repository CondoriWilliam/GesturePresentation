# Control de Presentaciones con Gestos de Mano

Este proyecto, basado en el contenido de [Computer Vision Zone](https://www.computervision.zone/courses/hand-gesture-presentation/) (publicado el 5 de mayo de 2022), utiliza **OpenCV** y **cvzone** para implementar un controlador de presentaciones que responde a gestos de mano. Permite navegar entre diapositivas, realizar anotaciones y ejecutar acciones sin necesidad de usar teclado o mouse.

## Características
- **Seguimiento de manos**: Detecta gestos utilizando `cvzone.HandTrackingModule`.
- **Navegación entre diapositivas**: Cambia entre diapositivas con gestos simples.
- **Anotaciones**: Dibuja directamente en las diapositivas con tu dedo índice.
- **Borrado de anotaciones**: Borra anotaciones realizadas anteriormente.
- **Superposición de cámara en vivo**: Muestra el video de la cámara web en las diapositivas.
- **Cierre de presentación**: Termina la presentación con un gesto de "cinco dedos".

## Gestos Reconocidos
| **Gesto**                    | **Acción**                              |
|------------------------------|-----------------------------------------|
| ✋ **Todos los dedos**        | Cierra la presentación.                 |
| ☝ **Dedo índice**            | Dibuja anotaciones en las diapositivas. |
| ✌ **Índice + Medio**         | Imprime un punto rojo en la diapositiva.|
| 👈 **Solo pulgar**            | Retrocede a la diapositiva anterior.    |
| 👉 **Solo meñique**           | Avanza a la siguiente diapositiva.      |
| 🤚 **Índice + Medio + Anular** | Borra la última anotación.             |

## Requisitos
- **Python**: Versión 3.11
- **Librerías necesarias**:
  - `opencv-python`
  - `cvzone`
  - `numpy`
