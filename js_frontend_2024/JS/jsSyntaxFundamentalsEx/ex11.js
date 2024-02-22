function roadRadar(speed, area) {
    const speedLimits = {
        'motorway': 130,
        'interstate': 90,
        'city':50,
        'residential':20
    }
    let outputMsg = '';
    if (speed <= speedLimits[area]) {
        outputMsg = `Driving ${speed} km/h in a ${speedLimits[area]} zone`;
    } else {
        let overLimit = speed - speedLimits[area];
        let status = '';
        if (overLimit <= 20) {
            status = 'speeding';
        } else if (overLimit <= 40) {
            status = 'excessive speeding';
        } else if (overLimit > 40) {
            status = 'reckless driving';
        }
        outputMsg = `The speed is ${overLimit} km/h faster than the allowed speed of ${speedLimits[area]} - ${status}`
        
    }
    console.log(outputMsg)
}

roadRadar(40,'city')
roadRadar(21,'residential')
roadRadar(120,'interstate')
roadRadar(200,'motorway')
roadRadar(0, 'motorway')