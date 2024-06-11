//Asignando tipo a una variable
var z = 2;
var g = 3;
var objf;
//Con arrays se pone como en java
var numeros = [2, 4, 6, 8, 3, 6, 7];
//Funciones****************************************************************************
//Asignando tipo a un parametro de una función
function fsaludar(nombre) {
    console.log("Hola ".concat(nombre));
}
//Función que recibe un objeto
function safludarPersona(_a) {
    var nombre = _a.nombre, edad = _a.edad;
    console.log("Hola ".concat(nombre, " tienes ").concat(edad, " a\u00F1os hermano"));
}
//Función que recibe un objeto pero esto te obliga a destructurar el objeto
function salfudarPersonaForma(persona) {
    var nombre = persona.nombre, edad = persona.edad;
    console.log("Hola ".concat(nombre, " tienes ").concat(edad, " a\u00F1os paps"));
}
//Al retornar hay nferencia de tipo de dato
function salufdarRetorno(nombre) {
    return "Hola ".concat(nombre, " padrusc");
}
//Como sabe que dato retorna no se puede asignar a esta variable por ser distintos tipos de datos
//let saludo : number = saludarRetorno("hola")
var saludof = salufdarRetorno("hola");
//Igual se puede especificar que tipo de dato retorna al crear la función
function salfudarRetornoAvisado(nombre) {
    return "Hola ".concat(nombre);
}
//Igual al pasar funciones como parametro debemos tipar las funciones diciendo que tipo de datos recibira la función y que tipo de dato va a retornas colocandolo de esta manera :
//"(funcion : (nombre : string) => string) =>"
//En caso de no devolver nada pondria void : "(funcion : (nombre : string) => void) =>"
var diHolaf = function (funcion) {
    funcion("Miguel");
};
var funcionCafllback = function (nombre) {
    console.log(nombre);
    return nombre;
};
diHolaf(funcionCafllback);
//Funciones con parametros opcionales
function saludafme(nombre) {
    if (nombre === void 0) { nombre = "Carnal"; }
    console.log("Hola ".concat(nombre));
}
//Funciones con parametros opcionales
function saludamfeOpcional(nombre, edad) {
    if (nombre === void 0) { nombre = "Carnal"; }
    if (edad == null) {
        console.log("Hola ".concat(nombre));
    }
    else {
        console.log("Hola ".concat(nombre, " tienes ").concat(edad));
    }
}
//Clases ***********************************************+
//Aqui en clases se parece mucho a Java
var persona = /** @class */ (function () {
    function persona(nombre) {
        this.nombre = nombre;
    }
    persona.prototype.saludar = function () {
        console.log("Hola yo soy ".concat(this.nombre));
    };
    return persona;
}());
