// Hacer un ejercicio que calcule los resultados de las tablas de multiplicar del 1 al 5 y muestre por pantalla el mensaje:
// "Los resultados son: 1, 2, 3..."
// Después modificaremos el array de "total" para mostrar el mismo mensaje solo con los primeros 20 números
// 5 tablas de multiplicar cada una hasta el 10....1x1, 2x1, 3x1, 4x1, 5x1

let total = [];

for(let i = 1; i <= 5; i++){
    for(let j = 0; j <= 10; j++){
        let multiplicacion = i * j

        total.push(multiplicacion);

    }
    
}

console.log('Los resultados son: ', total);

//total.splice(20);

//console.log('Los primeros 20 numeros son: ',total);

for( let i = total.length; i > 20; i--){

    total.pop();

}

console.log('Los 20 primeros resultados son: ', total);

