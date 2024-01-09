// printar el largo de la array beatles
// y después printar el largo de cada nombre.
// ejemplo:
// Ringo Star tiene 10 caracteres
// John Lenon tiene 10 caracteres
//....
// buscar cuales de los componenetes tienen mas de dos "a"
// Ej. :
// Paul McArtney tiene 2 a

let beatles = ["Paul McArtney", "John Lenon", "Ringo Star", "George Harryson"];
let letra = 'a';
let count = 0;


console.log('Los Beatles se componen de',beatles.length,'personas:');

for( let i = 0; i < beatles.length; i++){
    let name = beatles[i];
    let caracteres = beatles[i].length;
    count = 0;
    console.log(name,'tiene',caracteres,'caracteres' );
       
    for(let j = 0; j < caracteres; j++) {
        let beatlesLetter = beatles[i][j];
                       
        if( letra.toLowerCase() === beatlesLetter.toLowerCase()){
            count += 1;
        } 
    }

    if(count > 0){
        console.log(name,'tiene la letra',letra, count, 'veces');
    } else{
        console.log(name,'no tiene esa letra');
    }
    
}

