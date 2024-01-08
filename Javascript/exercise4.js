// Mostrar el contenido de result en diferentes lineas, el cual será el nombre de las escuelas con sus clases.
// Ej. 
// Balaguer-A
// Balaguer-B
// Balaguer-C
// Balmes-A
// Balmes-B
// Balmes-C
// San Josep-A
// San Josep-B
// San Josep-C
// Después, de esa misma variable result, eliminaremos las clases del último colegio, quedando el mismo contenido que había, pero sin nada de "San Josep"
// Balaguer-A
// Balaguer-B
// Balaguer-C
// Balmes-A
// Balmes-B
// Balmes-C

let schools = ["Balaguer", "Balmes", "San Josep"];
let classes = ["A", "B", "C"];
let result = [];


for (let h = 0; h < schools.length; h++) {
    let school = schools[h];
    for(let i = 0; i < classes.length; i++){

        let letter = classes[i];
        result.push(school+'-'+letter);

        for(let j = result.length; j > 6 ; j--){

            result.pop();
                        
            }        

    }

}
for(let k = 0; k < result.length; k++){

    console.log(result[k]);
}

// NOTA: Cuando utilizas comas lo que hacen son crear items mientras que si lo sumas te lo concatena (te hace una misma string), ejemplo:
// result.push(school+'-'+letter); esto lo que hará será un mismo item, 'school-letter'.
// result.push(school,'-',letter); esto lo que hará es que cada elemento de dentro lo pondra como un item por separado school, '-', letter.