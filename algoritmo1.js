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


//-------------------------------------/


// 2. Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un ciclo for.
// let acum = 0;
// let n = 0;

// for (let i = 0; i < 10; i++) {
//     n = parseInt(prompt("Ingrese el número " + (i+1)+ ": "));
//     acum = acum + n ;
//     console.log("La suma del 1 al 10 es: "+ acum);

// }


//--------------------------------------------------//


// 3. Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, 
// cuyo número de miembros se desconoce, el ciclo debe efectuarse siempre y 
// cuando se tenga una estatura registrada.

// let est = 1.0;
// let acumEst = 0;
// let contPers =0;

// while (est != 0) {
//         est = parseFloat(prompt("Ingrese la estatura en metros o 0 para terminar: "));
//         if (est==0) {
//             contPers--;
//         }
//         contPers++;
//         acumEst += est;
//     }
//     console.log("Promedio de estatura: " + acumEst/contPers);

//-------------------------------------//

// 4. Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero.
// num = "";
// countMj=0;
// countMn=0;

// while (num != "*") {
//     num = prompt("Ingrese el número o ' * ' para terminar");
//     if (num<=0) {
//         countMn++;
//     }else if(num>0){
//         countMj++;
//     }
// }
// console.log("Cantidad de números menores o iguales a cero: " +countMn +"\n" + "Cantidad de números mayores a cero: " + countMj);

//-------------------------------------//

// 5. Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran entre 0 y 100. 
// Además muestre la multiplicación de todos estos.

// let par = [];
// let impar = [];

// for (let i = 0; i < 100; i++) {
//     if (i % 2 == 0) {
//         par.push(i);
//     }else{
//         impar.push(i);
//     }
// }
// console.log("Los números pares son : " + par);
// console.log("Los números impares son: "+ impar);

//----------------------------------------//

// 6. Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13,…).
// 0 y 1 los dos números anteriores para hallar el segundo. Es decir:
// 0+1= 1
// 1+1=2
// 1+2=3
// 2+3=5
// 3+5=8

let n = parseInt(prompt("¿Cuántos números de Fibonacci quiere generar? : "));
let array = []; //sucesion de números entrero en orden: 0, 1, 2...

for (let i=0; i<n; i++){
    if(i==0){
        array.push(0);
    }else if(i==1){
        array.push(1);
    }else{
        array.push(array[i-1]+array[i-2]);
    }
}
console.log(array);




