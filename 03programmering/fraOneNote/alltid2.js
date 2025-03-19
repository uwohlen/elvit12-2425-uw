/* Går gjennom en array og teller opp hvor mange elementer vi har av en verdi 

Inn:
arrayInn - array i 1 dimensjon 
verdi - verdien du søker etter i arrayen

Ut:
return - antall av verdien du søker etter (tall)

*/
function antallElementer(arrayInn,verdi) {
    let antall = 0;

    for (let i=0; i< arrayInn.length; i++) {
        if (arrayInn[i] === verdi) {
            antall ++;
        }
    }
    return antall;
}