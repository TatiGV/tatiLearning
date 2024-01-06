// Hacer un programa que por cada letra de la variable abecedario muestre el nombre del componente de los Beatles
// cuyo nombre empiece por esa letra. Si no hay ninguno, mostrará 'Nadie empieza por X ' donde x es la letra que se esta comparando


let beatles = ["Ringo Star", "John Lenon", "Paul McArtney", "George Harryson"];
let abecedario = "abcdefghijklmnopqrstuvwxyz";
let existe = "";

for(let i = 0; i < abecedario.length; i++){  
    let letra = abecedario[i];
    existe = "";

    for (let j = 0; j < beatles.length; j++) {
            let nombre = beatles[j].toLowerCase();

            if (letra == nombre[0]) {
                existe = nombre;
            }
    }

    if (existe != "") {
        console.log(existe, 'empieza por la letra', letra);
    } else  {
        console.log('Nadie empieza por', letra);
    }
}

 

