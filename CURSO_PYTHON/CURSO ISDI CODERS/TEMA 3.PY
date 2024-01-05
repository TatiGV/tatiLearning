'''
ARRAYS

Un Array es una estructura de datos que permite almacenar múltiples valores bajo un solo nombre. 
Estos valores, también llamados elementos, pueden ser de cualquier tipo de dato 
(números, cadenas, objetos, etc.) y se almacenan en posiciones numeradas llamadas índices.
La numeración de los índices generalmente comienza desde cero.

 // Crear un array de números
 const numbers = [1, 2, 3, 4, 5];

 // Crear un array de cadenas
 const fruits = ['apple', 'orange', 'banana'];

 // Crear un array de elementos mixtos
 const mix = [1, 'four', true, { name: 'John' }];
Podemos acceder a los elementos de un array utilizando sus índices:

 console.log(numbers[0]);  // output: 1
 console.log(fruits[1]);    // output: orange
También puedes modificar, añadir o eliminar elementos de un array dinámicamente
utilizando los métodos push y pop.

Y, ¿qué son los métodos?

Son funciones que pertenecen a un objeto y nos permiten modificar o manipular sus elementos. 
Cada tipo de objeto en JavaScript tiene su propio conjunto de métodos asociados.

PROPIEDAD LENGTH

Es una propiedad incorporada en JavaScript que se utiliza para obtener o 
establecer la cantidad de elementos en un array o la longitud de un String.

 // mostramos por pantalla la longitud del array
 console.log(fruits.length);          

 // Modificar un elemento
 fruits[1] = 'pear';  
 // Mostramos por pantalla que elemento hay ahora en la posición 1  
 console.log(fruits[1])   
          
 // Añadir un elemento al final 
 fruits.push('kiwi');    
 // mostramos de nuevo la longitud del array         
 console.log(fruits.length);          

 fruits.pop();    // Eliminar el último elemento
 console.log(fruits.length);   / mostramos de nuevo la longitud del array
 

El array es una herramienta poderosa y versátil en programación, y se utiliza comúnmente 
para almacenar y manipular colecciones de datos.






'''