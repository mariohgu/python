# Los principios SOlid para el desarrollo:

# matenibilidad: el software debe ser facil de mantener y modificar
# mantenibilidad: el software debe ser facil de mantener y modificar.
#    - Separar responsabilidades en clases y métodos pequeños y bien nombrados
#    - Documentar el código con comentarios y documentación de API
#    - No repetir código
#    - No tener código muerto (código que no se usa)
#    - Testear el código para asegurar que sigue funcionando correctamente

# reusabilidad, el software debe ser facil de reutilizar
#    - Crear abstracciones que se puedan reutilizar en diferentes contextos
#    - No depender de clases o métodos concretos, sino de abstracciones.
#    - Crear interfaces y clases abstractas que puedan ser implementadas de diferentes maneras.

# legibilidad, debe ser facil de entender para ti y otro desarrollador.
#    - Usar nombres descriptivos para variables, métodos, clases y funciones
#    - No usar variables mágicas ni números mágicos en el código
#    - No usar comentarios que dupliquen la información que ya está en el código
#    - No usar código que no sea necesario para entender el comportamiento del programa
#    - No usar estructuras de control complicadas o anidadas sin necesidad
#    - Separar secciones de código con líneas en blanco
#    - No usar tabs en el código, sino espacios

# extensible, el software debe ser capaz de extenderse pero sin afectar su funcionamiento.
#    - El software debe ser capaz de extenderse sin necesidad de modificar su comportamiento original.
#      Esto se logra a través de la creación de abstracciones y la inversión de dependencias.


# S: Single Responsability Principle: Una clase debe tener una sola responsabilidad
# O: Open/Closed Principle: La clase debe estar abierta a extensiones, pero cerrada a modificaciones
# L: Liskov Substitution Principle: Los hijos deben ser sustitutos perfectos de sus padres
# I: Interface Segregation Principle: No se debe forzar a las clases a implementar metodos que no usan
# D: Dependency Inversion Principle: Las clases deben depender de abstracciones, no de implementaciones concretas.

# responsabilidad unica, una clase debe tener una sola responsabilidad. No hay sobrecarga, es decir que tenga muchas funciones. Es importante que saber que esa clase puede hacer su tarea sin depender de otra clase.
# ejemplo: una clase para manejar la base de datos de un programa de gestión de tareas,
# solo debe tener una responsabilidad: manejar la base de datos.
# no debe tener funciones para mostrar la interfaz gráfica, ni funciones para
# enviar notificaciones, ni funciones para guardar los datos en un archivo, etc.
