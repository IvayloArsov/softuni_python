function sumDigits (num) {
    let numSum = 0;
    let numString = num.toString()
    for (let i=0; i < numString.length; i++){
        numSum += parseInt(numString[i])
    }
    console.log(numSum);
}

sumDigits(245678)
sumDigits(97561)
sumDigits(543)