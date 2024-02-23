function printAndSum(start,end) {
    let sumOfLoop=0;
    let oneLine='';
    for (let i=start; i<=end; i++) {
        sumOfLoop += i;
        oneLine += i + ' ' 
    }
    console.log(oneLine);
    console.log(`Sum: ${sumOfLoop}`);
}

printAndSum(50, 60)
printAndSum(5, 10)
printAndSum(0, 26)