'''
TIPOS DE DATOS

Existen 8 tipos de datos. Siete de ellos se consideran primitivos 
y uno también conocido como tipo de dato estructurado o de referencia.

1. String: representa una secuencia de caracteres. Puedes utilizar comillas simples ( ' ) 
o dobles ( " ) para delimitar las cadenas.

 let greetings = 'Hello, world';
 const name = 'John';

2. Number: representa números enteros o de punto flotante(con decimales). 
El operador de signo negativo permite definir números negativos.

 const pi = 3,1416
 const myAge = 34

3. Boolean: es un tipo de dato que representa dos únicos valores: true o false

 let isSunny = true
 let isRainy = false

 4. Undefined: es un valor y un tipo de dato que se utiliza para representar 
 la ausencia de un valor asignado a una variable o a una propiedad de objeto.
 Cuando declaras una variable pero no le asignas un valor, o cuando intentas acceder 
 a una propiedad que no existe en un objeto, el resultado es undefined.

 const userName;
 console.log(userName); // output: undefined

5. Null: es un valor especial que se utiliza para representar la ausencia intencional 
de cualquier valor, o un objeto que no existe o que no tiene ningún valor asignado. 
A diferencia de undefined, que generalmente indica la falta de asignación, null se 
utiliza para expresar explícitamente que no hay valor o que algo está vacío.

 const foo = null
 console.log(null) // output: null

6. BigInt: el tipo de dato BigInt se introdujo en ECMAScript 2020 (también conocido como ECMAScript 11)
para manejar enteros más grandes que los que se pueden representar de manera precisa
 con el tipo de dato Number. Un BigInt se crea añadiendo la letra n al final de un número literal 
 o utilizando el constructor BigInt( ).

 let bigNumber = 1234567890123456789012345678901234567890n;
 console.log(bigNumber);  // Output: 1234567890123456789012345678901234567890n

 let anotherBigNumber = BigInt('9876543210987654321098765432109876543210');
 console.log(anotherBigNumber);  // Output: 9876543210987654321098765432109876543210n

 7. Symbol: es un tipo de dato primitivo introducido en ECMAScript 2015 (ES6). 
 Los símbolos son valores únicos e inmutables que se pueden utilizar como identificadores 
 para propiedades de objetos. Proporcionan una forma de crear claves de propiedad privadas 
 o no ambiguas, evitando colisiones de nombres no deseadas en objetos.

 // creamos un símbolo
 let mySymbol = ()

 // utilizamos un símbolo como clave de propiedad 
 let object = {
	[mySymbol]: 'Hello, Symbol';
 }
En este ejemplo, mySymbol es un símbolo que se utiliza como clave de propiedad en el objeto object. 
Los símbolos están garantizados para ser únicos, lo que los hace útiles para crear identificadores 
de propiedad que no entrarán en conflicto con otras claves.

(Igualmente, no se utilizan demasiado, no te preocupes si ahora no los entiendes).

8. Object: es un tipo especial referenciado que incluye principalmente los Object, 
Array, RegExp, Date, Error y Function.

 // Mostramos dos ejemplos sobre Object y Array. Los demás los verás más adelante

 /* Object: colección no ordenada de pares clave-valor, donde las claves son cadenas de texto o símbolos, 
  y los valores pueden ser de cualquier tipo de dato, incluidos otros objetos */
  
 const user = {
	name: 'John',
	age: 23
 }

 // Array: estructura de datos que se utiliza para almacenar una colección ordenada de elementos
 const brandCars = ['Audi', 'Mercedes', 'Seat']





'''