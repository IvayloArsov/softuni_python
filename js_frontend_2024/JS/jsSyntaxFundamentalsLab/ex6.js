// function largestNumber(num1, num2, num3) {
//     let result;

//     if (num1 >= num2 && num1 >= num3) {
//         result = num1;
//     } else if (num2 >= num1 && num2 >= num3) {
//         result = num2;
//     } else {
//         result = num3;
//     }

//     console.log(`The largest number is ${result}.`);
// }
// largestNumber(0,2,9)


function largestNumber(num1,num2,num3) {
    let result;
    
    result = Math.max(num1,num2,num3)
    console.log(`The largest number is ${result}.`);
}

largestNumber(3,4,5)
largestNumber(5,3,5)