//Interface dentro de otra interface
interface Producto {
    id: number,
    nombre: string,
    precio : number
}
interface Carrito {
    totalPrice: number,
    productos : Producto[]
}
//Extendiendo interface
//Aqui ya no es necesario coocar lo de la otra interface, solo de la nueva
//Es como unir los type
interface Zapato extends Producto {
    talla : number
}
let tenis : Zapato = {
    talla : 4,
    id: 4,
    nombre : "Nike",
    precio : 59
}
//Entonces ahora podrias poner el carrito como:
interface CarritoCompras {
    totalPrice: number,
    productos : (Producto | Zapato)[]
}
//Tambien puedes por ejemplo poner funciones determinadas
interface CarritoOpciones {
    add(producto : Producto) : void,
    remove : (id : number) => void
}