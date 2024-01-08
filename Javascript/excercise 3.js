// reloj

let minutes = 60;
let hours = 10;
let seconds = 60;

for(let i = 0; i < hours; i++){
    for(j = 0; j < minutes; j++){
        for( let h = 0; h < seconds; h++){

            if(i === 7 && j === 15 && h === 0){
                
                console.log(i,':',j,':',h)            
                console.log('Despierta!!!!');
                
    
            } else{
    
                console.log(i,':',j,':',h);
    
    
            }


        }
        

        
        
    }



}