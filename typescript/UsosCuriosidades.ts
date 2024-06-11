//Narrowing
function obtener(objeto: number | string) {
    if(typeof objeto == "string"){
        return objeto.length //Aqui sabe que es string porque ya valido que no es number
    }
    return objeto.toString().length //Aqui como no paso la validacion entonces ya sabe que es number
}
//Ejemplo mas a fondo
interface Mario {
    company : "Nintendo",
    nombre : string,
    saltar: () => void
}

interface Sonic {
    company : "Sega",
    nombre : string,
    correr : () => void
}

type Personaje = Mario | Sonic

//Como lo hicimos anteriormente
function jugar(pj:Personaje) : void {
    console.log(pj.nombre) //Aqui si se puede acceder sin problema
    if(pj.company == "Nintendo"){
        pj.saltar() //Aqui ya sabe de cual personaje hablo
    } else {
        pj.correr() //Aqui ya sabe que es el otro personaje
    }
}

//con el type guard
function checkIsSonic(personaje : Personaje) : personaje is Sonic {
    return (personaje as Sonic).correr !== undefined
}

function jugando(personaje:Personaje) {
    if(checkIsSonic(personaje)){
        personaje.correr()
    } else {
        personaje.saltar()
    }
}
