//Asignando tipo a una variable
let z = 2;
let g: number = 3;
let objf: any;
//Para colocar distintos tipados
let objetivo : number | null | undefined
//Con arrays se pone como en java
let numeros : number[] = [2, 4, 6, 8, 3, 6 ,7]
//Igual infiere e tipo de arreglo
let web = ["HTML", "Css", "Js"]
//Si queremos colocar distintos tipos se pone en parentesis
let lista : (string | number)[] = []
let matriz : string[][]
//Tipado personalizado para un objeto
type Programador = {
  nombre : string,
  tecnologias : string[] | null,
  edad? : number 
}
//Ejemplo de gato
//Creamos el type 
type CellValue = "X" | "O" | ""
//Creamos un type de tupla (Que es un array con un tamaño inmutable)
type gameBoard = [
  [CellValue, CellValue, CellValue],
  [CellValue, CellValue, CellValue],
  [CellValue, CellValue, CellValue]
]
//Ahora si creamos nuestro board
let board : gameBoard = [
  ["","",""],
  ["","",""],
  ["","",""]
]
//Ejemplo tupla de react
type useReactExample = [string, (a:string)=>void]
let hook : useReactExample = ["Hola", (a:string)=>{}]
//RGB
type RGB = [number, number, number]
let coloreando : RGB = [23, 3, 2]
//Le podemos asignar este valor a un objeto con los tipos de datos que colocamos
let programador : Programador = {
  nombre : "angel",
  tecnologias : null,
  edad : 23
}
//Igual como tiene algunos valores opcionales puede no tenerlos 
let programador2 : Programador = {
  nombre : "luis",
  tecnologias : ["HTML", "CSS"]
}
//2.- Usando template para seguir la regla de como se escribe
type hexadecimalColor = `#${string}`
let color : hexadecimalColor = "456556"
let color2 : hexadecimalColor = "#456556"
//Valores preestablecidos
type EscalaDeFuerza = "Debil" | "Fuerte" | "Galactico"
let thor : EscalaDeFuerza = "Torrencial"
let spiderman : EscalaDeFuerza = "Galactico"
type valor = string | 2
let dato : valor = 3
let dato1 : valor = 2
let dato2 : valor = "Hola"
//Intersection types
//Type HeroInput
type HeroInput = {
  name: string,
  fuerza : EscalaDeFuerza
}
//Type HeroDatos
type HeroDatos = {
  id: number,
  age?: number
}
//Uniendo para crear un heroe
type Hero = HeroDatos & HeroInput
function creandoHeroe(input : HeroInput) : Hero {
  const {name, fuerza} = input
  return {
    id: 64,
    name,
    fuerza,
    age: 2000
  }
}
type Propiedades = {
  isActive : boolean,
  address : {
    planet : string,
    city : string
  }
}
function cambiandoPlaneta(input : Propiedades) : Propiedades {
  let newAddress : Propiedades["address"] = {
    planet: "Tierra",
    city: "Casa"
  }
  input.address = newAddress
  return input;
} 
const address = {
  planeta : "Marte",
  ciudad : "Desconocida"
}
type Address = typeof address
let heroeAdress : Address= {
  planeta: "Tierra",
  ciudad: "Ya se sabe"
}
//Tambien se puede hacer del return que tienen algunas funciones, obtener los tipos de datos
function crearDireccion(){
  return {
    ciudad: "Mango",
    pueblo: "Manchado"
  }
}
type Direccion = ReturnType<typeof crearDireccion>
let direccion : Direccion = {
  ciudad:"",
  pueblo:""
} 
//Funciones****************************************************************************
//Asignando tipo a un parametro de una función
function fsaludar(nombre: String) {
  console.log(`Hola ${nombre}`);
}
//Función que recibe un objeto
function safludarPersona({ nombres, edad }: { nombre: String; edad: number }) {
  console.log(`Hola ${nombre} tienes ${edad} años hermano`);
}
//Función que recibe un objeto pero esto te obliga a destructurar el objeto
function salfudarPersonaForma(persona: { nombre: String; edad: number }) {
  const { nombre, edad } = persona;
  console.log(`Hola ${nombre} tienes ${edad} años paps`);
}

//Al retornar hay nferencia de tipo de dato
function salufdarRetorno(nombre: String) {
  return `Hola ${nombre} padrusc`;
}
//Como sabe que dato retorna no se puede asignar a esta variable por ser distintos tipos de datos
//let saludo : number = saludarRetorno("hola")
let saludof: string = salufdarRetorno("hola");
//Igual se puede especificar que tipo de dato retorna al crear la función
function salfudarRetornoAvisado(nombre: String): string {
  return `Hola ${nombre}`;
}
//Igual al pasar funciones como parametro debemos tipar las funciones diciendo que tipo de datos recibira la función y que tipo de dato va a retornas colocandolo de esta manera :
//"(funcion : (nombre : string) => string) =>"
//En caso de no devolver nada pondria void : "(funcion : (nombre : string) => void) =>"
const diHolaf = (funcion : (nombre : string) => string) => {
    funcion("Miguel")
}
let funcionCafllback = (nombre : string)=>{
    console.log(nombre)
    return nombre
}
diHolaf(funcionCafllback)
//Funciones con parametros opcionales
function saludafme(nombre:string = "Carnal") {
  console.log(`Hola ${nombre}`)
}
//Funciones con parametros opcionales
function saludamfeOpcional(nombre:string = "Carnal", edad? : number) {
  if(edad == null){
    console.log(`Hola ${nombre}`)
    } else {
    console.log(`Hola ${nombre} tienes ${edad}`)
  }
}
//Clases ***********************************************+
//Aqui en clases se parece mucho a Java
class persona{
  nombre : string

  constructor(nombre:string){
    this.nombre = nombre
  }

  saludar(){
    console.log(`Hola yo soy ${this.nombre}`)
  }
}
//Interfaces ********************************+++++++
interface personas{
  nombre : string
  edad : number
}
let dev : personas = {
  nombre : "Hola",
  edad : 4
}
//Con propiedades opcionales
interface producto{
  nombre : string
  precio : number
  descripcion? : string
}
let coca : producto = {
  nombre : "Coca",
  precio : 5.7,
}
//Para funciones
interface comparador{
  (a: number, b : number) : boolean;
}
const comparando: comparador = (a:number, b:number) =>  {
  return a == b;
}
//Para clases
interface personaclas{
  nombre : string
  edad : number

  saluda(a:string):void;
}
class Humano implements personaclas{
  nombre:string
  edad:number
  constructor(nombre:string, edad:number){
    this.nombre = nombre
    this.edad = edad
  }

  saluda(nombre:string){
    console.log(`Hola ${nombre}, soy ${this.nombre}`)
  }
}
class Palomitas{

}
class Pelicula<T>{

	private promocion? : T
  nombre?:string = "No se aceptan devoluciones"
  protagonistas: string[] | null = null
  actores?: string[]

  constructor(nombre: string, protagonistas:string[], actores:string[]){
    this.nombre = nombre
    this.protagonistas = protagonistas
    this.actores = actores
  }

  private proyectarEnCine(){
    console.log(`${this.nombre} esta siendo proyectada`)
  }
  
  public ejecutarPromocion(){
	  console.log("Ejecutando la promocion " + this.promocion)
  }
}

let pelicula = new Pelicula<Palomitas>("Barbie", ["Barbie"], ["Margot Robie"])
//Enums
//En javascript lo hariamos de esta manera
const ERROR_TYPES = {
  NOT_FOUND: "Not found",
  UNAUHTORIZED: "Unauthorized",
  FORBIDDEN: "Forbidden"
}
function showError(tipoError){
  if (tipoError == ERROR_TYPES.NOT_FOUND) {
    console.log("No se encontro")
  }
  else if (tipoError == ERROR_TYPES.UNAUHTORIZED) {
    console.log("Sin autorizacion")
  }
  else if (tipoError == ERROR_TYPES.FORBIDDEN) {
    console.log("No tienes permisos")
  }
}
//En typescript lo hariamos de esta manera
const enum ERROR_TYPE {
  NOT_FOUND,
  UNAUHTORIZED,
  FORBIDDEN = "forbidden"
}
function mostrarMensaje(tipoError : ERROR_TYPE){
  if (tipoError == ERROR_TYPE.NOT_FOUND) {
    console.log("No se encontro")
  }
  else if (tipoError == ERROR_TYPE.UNAUHTORIZED) {
    console.log("Sin autorizacion")
  }
  else if (tipoError == ERROR_TYPE.FORBIDDEN) {
    console.log("No tienes permisos")
  }
}
const canvas = document.querySelector("canvas")
if (canvas instanceof HTMLCanvasElement) {
  const ctx = canvas.getContext("2d")
}