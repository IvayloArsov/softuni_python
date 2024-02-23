function wordsUppercase(inputString) {
    const words = inputString.match(/\b\w+/g)
    const upperCaseWords = words.map(word => word.toUpperCase())
    console.log(upperCaseWords.join(', '));
}

wordsUppercase('Hi, how are you?')
wordsUppercase('hello')