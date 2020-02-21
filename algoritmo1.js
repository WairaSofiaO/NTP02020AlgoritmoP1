// 3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una estatura registrada.

// 4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero.

// 5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran entre 0 y 100. Además muestre la multiplicación de todos estos.

// 6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13,…).




// 1. Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. 
// Si algún alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18 años.
// EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.

// let n = 0;
// let edad = 0;
// let contPers =0;
// let acumEdad = 0;
// let continuar = 1;

// // continuar = prompt("Escriba 0 para terminar o 1 para seguir: ");
// while (continuar != 0) {
//     edad = parseInt(prompt("Ingrese la edad: "));    
//     contPers++;
//     acumEdad += edad;

//     if (edad > 18) {
//         contPers = contPers - 1; 
//         acumEdad = acumEdad - edad;
//         continuar = prompt("Escriba 0 para terminar o 1 para seguir: ");
//     }else{
//         continuar = 1;
//     }
// }
// console.log("Promedio de edad: " + acumEdad/contPers);


////////////////////////////////////////////////////////////


// 2. Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un ciclo for.
// let acum = 0;
// let n = 0;

// for (let i = 0; i < 10; i++) {
//     n = parseInt(prompt("Ingrese el número " + (i+1)+ ": "));
//     acum = acum + n ;
//     console.log("La suma del 1 al 10 es: "+ acum);
    
// }


/////////////////////////////////////////////////////////


// 3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una estatura registrada.
let est = 0;
let continuar = 1;
let acumEst = 0;
let contPers =0;

while (continuar != 0) {
        est = parseInt(prompt("Ingrese la estatura en metros: "));    
        contPers++;
        acumEst += est;

        continuar = prompt("Escriba 0 para terminar o 1 para seguir: ");
    }
    console.log("Promedio de estatura: " + acumEst/contPers);