function circleArea (radius) {
    let result;
    if (typeof radius === 'number') {        
        result = (Math.PI * ( radius ** 2)).toFixed(2)
        
    } else {
        result = `We can not calculate the circle area, because we receive a ${typeof radius}.` 
        
    }
    console.log(result);
}

circleArea('a')
circleArea(5)