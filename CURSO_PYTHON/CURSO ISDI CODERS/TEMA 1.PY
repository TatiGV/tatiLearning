

'''
- Comentarios: en JS hay dos formas de hacerlo, como puedes ver a continuación:

// Comentario de una línea, termina al final de esta

/*
  Comentario de múltiples líneas
  No termina hasta que aparecen los siguientes símbolos
*/

- Sentencia: es una instrucción que realiza una acción o realiza una tarea específica. 
Se ejecutan secuencialmente, una tras otra. 
Cada sentencia termina con un punto y coma (;), aunque, en algunos casos, puede ser opcional.

En este ejemplo creamos nuestro primer programa (con una única sentencia) donde imprimimos por consola un mensaje:

console.log('Hola mundo');

- Qué es un console.log?
    Es una función en JavaScript que se utiliza para imprimir mensajes o valores en la consola del navegador
o entorno en el que se esté ejecutando el código.

    En este ejemplo de sentencia, declaramos una variable llamada name, donde le asignamos el valor 'Ernestina' y,
posteriormente, imprimimos por consola su valor.

cont name = 'Ernestina';
console.log(name);

- Variable: las variables son etiquetas (labels) que hacen referencia a un valor o que dan nombre a las localizaciones 
donde se almacenan (named storage) los valores.

    Piensa en ella como una caja etiquetada donde puedes guardar un valor y luego referenciar ese valor utilizando el nombre de la variable.

    Para poder usar una variable, tenemos que:

    * Declararla (sería como crear la etiqueta que mencionábamos anteriormente).
    * Asignarle un valor (inicializarla).

- ¿Cómo declarar una variable?

    La declaración de variables en JS se realiza mediante las palabras reservadas let y const.

* La palabra reservada let declara una variable cuyo valor puede ser reasignado tantas veces como sea necesario. 
Por tanto, la declaración puede incluir una asignación inicial o dejarlo para más adelante.

 // declaramos la variable age y le asignamos un valor 
 let age = 20; 

 // modificamos el valor de la variable age 
 age = 30;
 

* La palabra reservada const declara una variable cuyo valor NO puede ser reasignado nunca, 
por lo que siempre debe incluir la asignación del valor de la variable.

const userName = 'John';
userName = 'Peter'; // Esto generará un error

    Esto no significa que las variables de tipo const no puedan cambiar de valor. Cuando se trata de objetos, 
podemos modificar partes específicas dentro del objeto, como agregar, eliminar o cambiar propiedades. 
Esto se llama mutabilidad y es una excepción a la regla de inmutabilidad de const.

    Para completar estos primeros pasos acabaremos hablando de la concatenación. 
Puedes unir dos o más cadenas para formar una cadena más larga utilizando el operador de concatenación (+) o el método concat( ).

let name = 'John';
let surname = 'Wick';

 // Usando el operador +
let fullName = name + ' ' + surname;
console.log(fullName);  // output: John Wick

 // Usando el método concat()
let greetings = 'Hello, ';
let fullMessage = greetings.concat(fullName);
console.log(fullMessage);  // output: ¡Hello, John Wick!


'''