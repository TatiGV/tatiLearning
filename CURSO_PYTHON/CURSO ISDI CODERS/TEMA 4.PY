'''
CONDICIONALES

Las estructuras condicionales en JavaScript permiten ejecutar diferentes bloques de código
dependiendo de si una condición es verdadera o falsa.

Hay diferentes tipos de condicionales en JavaScript como:

if - else: la estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera. 
Se puede complementar con else para indicar la condición contraria.

switch: permite evaluar una expresión para varios casos diferentes.

ternarios: proporciona una forma concisa de escribir condicionales en una sola línea.

Para el nivel en el que nos encontramos ahora, nos centraremos principalmente en la estructura if-else.

 
Como se ha comentado más arriba, if es una estructura de control que permite ejecutar 
un conjunto específico de instrucciones, si una condición dada es evaluada como verdadera. 
En términos más técnicos, la condición es una expresión booleana que resulta en true o false.

 let temperature = 35;

 if (temperature > 30) {
   // código que se ejecutará si temperature es mayor que 30
   console.log('¡Hace calor!');
}
Podemos completar el if con otro bloque alternativo, que se ejecutará si no se cumple la condición.

 // Ampliamos el ejemplo anterior: 

 let temperature = 35;

 if (temperature > 30) {
    // código que se ejecutará si temperatura es mayor que 30
    console.log('¡Hace calor!');
 } else {
    // código que se ejecutará si temperatura es menor que 30
    console.log('No hace calor');
 }
Otro ejemplo del uso de if-else para distinguir entre pares e impares puede ser el uso del operador 
de módulo o resto (%), que devuelve el resto de una división:

 En los pares el resto es 0: n%2 = 0
 En los impares es 1: n%2 = 1
 const num = 2

 if (num % 2 === 0) {
    console.log(El número ${num} es par);
 } else {
    console.log(El número ${num} es impar);
 }
 

¿Por qué utilizamos el operador ‘===’?

Antes de explicar qué significa el operador ‘===’ tenemos que entender que en JS 
tenemos unos operadores de comparación para evaluar la relación entre valores.

Comparadores de igualdad:

 - Igual (==). Devuelve true si los operandos son iguales.
 - No es igual (!=). Devuelve true si los operandos no son iguales.
 - Estrictamente igual (===). Devuelve true si los operandos son iguales y del mismo tipo.
 - Desigualdad estricta (!==). Devuelve true si los operandos son del mismo tipo pero no iguales, 
 o son de diferente tipo.
 

Mayor o menor:

 - Mayor que (>)
 - Mayor o igual que (>=)
 - Menor que (<)
 - Menor o igual (<=)






'''