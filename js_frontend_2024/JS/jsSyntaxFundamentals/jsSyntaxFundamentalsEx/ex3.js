function isLeapYear(year) {
    switch (true) {
        case (year % 4 === 0 && year % 100 !== 0):
        case (year % 400 === 0):
            console.log('yes');
            break;
        default:
        console.log('no');
    }
    
}

isLeapYear(1984)
isLeapYear(2003)
isLeapYear(4)