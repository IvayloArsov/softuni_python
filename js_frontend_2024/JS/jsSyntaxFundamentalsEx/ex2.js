function vacation(num, typeGroup, dayWeek) {
    let output;
    const timetable = {
        'Students': {
            'Friday': 8.45,
            'Saturday': 9.80,
            'Sunday': 10.46
        },
        'Business': {
            'Friday': 10.90,
            'Saturday': 15.60,
            'Sunday': 16
        },
        'Regular': {
            'Friday': 15,
            'Saturday': 20,
            'Sunday': 22.50
        }
    };

    const price = timetable[typeGroup][dayWeek];
    output = num * price;

    if (typeGroup === 'Students' && num >= 30) {
        output *= 0.85;
    } else if (typeGroup === 'Business' && num >= 100) {
        num -= 10;
        output = num * price;
    } else if (typeGroup === 'Regular' && num >= 10 && num <= 20) {
        output *= 0.95;
    }

    console.log(`Total price: ${output.toFixed(2)}`);
}

vacation(30,
    "Business",
    "Sunday");
vacation(110,
    "Business",
    "Sunday");

vacation(30,
    "Students",
    "Sunday");
vacation(40,
    "Regular",
    "Saturday");
