function sameNumbers(integer){
    let numSum = 0;
    let numString = integer.toString()
    for (let i=0; i < numString.length; i++){
        numSum += parseInt(numString[i])
    }
    if (numSum/numString.length != numString[0] ) {
        console.log('false');
    } else {
        console.log('true');
    }
    console.log(numSum);
}


//another solution using .every to check each element with the first
//both work for the task 100/100 

// function sameNumbers(integer) {
//     let numSum = 0;
//     let numString = integer.toString();

//     for (let i = 0; i < numString.length; i++) {
//         numSum += parseInt(numString[i]);
//     }

//     const allSame = numString.split('').every(digit => digit === numString[0]);

//     console.log(allSame);
//     console.log(numSum);
// }

