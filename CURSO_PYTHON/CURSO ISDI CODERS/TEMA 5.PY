'''
BUCLES

¿Qué son los bucles?

Los bucles son herramientas poderosas que nos permiten ejecutar instrucciones repetitivas de manera ordenada.

Existen dos tipos de estructuras de iteración:

 - Las que dependen de una condición independiente del número de ciclos, normalmente
   mediante while y do ... while
 - Las que se ejecutan un número determinado de veces, normalmente mediante 
 diversas variaciones de for.
 
 En este momento nos centraremos en el bucle for clásico.

 Es utilizado cuando conocemos la cantidad exacta de iteraciones que deseamos realizar.
 Estructura: for (inicialización; condición; actualización) { ... }.
 

Estructura del bucle for:

Inicialización:

- La primera parte del bucle for se ejecuta solo una vez, al principio.
Aquí, puedes inicializar una variable que actuará como contador o configurar
cualquier otra variable necesaria para el bucle.

Condición:

- La condición es evaluada antes de cada iteración del bucle. Si la condición es verdadera, 
el código dentro del bucle se ejecuta; de lo contrario, el bucle se detiene.

Actualización:

- La última parte del bucle for se ejecuta después de cada iteración. Se utiliza típicamente 
para actualizar la variable de control (por ejemplo, incrementar o decrementar el contador).

Ejemplos:

 // Para poder generar una serie de números
 for (let i = 0; i < 5; i++) {
    // Código a ejecutar en cada iteración. En este caso sacamos por pantalla el valor de i
    console.log(i);
 }

 // Iterar sobre un array
 const colours = ['black', 'white', 'red'];

 for (let i = 0; i < colours.length; i++) {
    console.log(colours[i]);
 }

 // Recorrer una cadena de texto
 const word = 'JavaScript';

 for (let i = 0; i < word.length; i++) {
    console.log(word[i]);
 }






'''