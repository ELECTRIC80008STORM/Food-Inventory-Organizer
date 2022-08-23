# Nombre-por-Decidir
Este será un organizador de inventario enfocado para personas foráneas que permitirá añadir y categorizar los distintos alimentos que tengas. Ayudando a permitirles una mejor organización acerca de los alimentos que posean, con recordatorios para cuando estén cercanos a expirar y para cuando estén cerca de acabarse.

## La utilidad de este organizador estará dada por:
* La capacidad de organizar los distintos alimentos que se introduzcan a la base de datos local.  

* El poder categorizar los distintos alimentos con categorías predeterminadas o creadas por el usuario.  

* La capacidad de etiquetar los alimentos en base a qué tan cercanos están de acabarse. (La información de duración aproximada tendrá que ser dada por el usuario para que la aplicación pueda recordarle previo a que se le acabe).  

* Los recordatorios sobre la cercana expiración del alimento son dados cuando el usuario pone la fecha de caducidad del alimento.

### Cambios Posibles
Permitir al usuario meter el precio de cada producto para que el inventario también funcioné como una lista de compras, juntándose con los recordatorios de qué tan próximo está por acabarse.

---

## Pseudocódigo en el que se basaran las bases del proyecto:
función pantalla_de_inicio () {
Permitirá al usuario ver una pantalla de carga con una pequeña animación en lo que el programa carga.
}

función pantalla_principal () {
Mostrará un título con el nombre de la app. Abajo aparecerá al ingresar por primera vez un signo de más gris en medio. Y un texto abajo mostrando “Haz clic para añadir el primer elemento de tu lista”
}

lista_de_alimentos {Contendrá todos los productos que el usuario ingrese}

lista_de_caducidad {Estará ligada a la lista de alimentos y permitirá guardar la caducidad de los productos}

lista_de_categorías {Permitirá escoger de una serie de categorías predeterminadas o asignarle una nueva categoría a los alimentos que añades a tu lista, estará ligada a la lista de alimentos.}

lista_de_etíquetas {Permitirá a los usuarios añadir un estimado de cuando creen que se acaben sus productos. Tambien guardara el nuevo estimado.}

función caducidad () {Dependiendo de la fecha de caducidad ingresada por el usuario llamará a la función notificación que permite notificarle 5 días antes de que caduque, 2, y el dia en que caduque}

función etiquetas () {Dependiendo del estimado puesto por el usuario de cuando se acabara su producto llamara a la función notificación y le avisara al usuario 3 días antes y 1 dia antes de que su producto se acabe, y tambien el dia que seleccionó preguntando si el estimado fue correcto, sino le permitirá corregirlo, guardando el nuevo valor y sumandolo al anterior para la próxima vez recordarle el valor total al usuario}

función notificación () {Notificará al usuario cuando se requiera}
