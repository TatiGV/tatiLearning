'''

/* 
 Crea un reloj que te indique las horas: un for que cuenta horas con un for en su interior que cuenta minutos. 
 Un console.log te puede mostrar que para cada vuelta del primer loop, el de dentro da 60. 
 ¿Sabrías crear una alarma que te imprima "¡Despierta!" a las 7:15?
*/

const horas = 24;
const minutos = 60;

for(let i = 0; i < horas; i++){
    for(let j = 0; j < minutos; j++){
        console.log(i,':',j);
        if (i === 7 ){
            if(j === 15){
                console.log(i,':', j, 'Despierta!');
            }
        }
            
    }
        
}

}

'''
