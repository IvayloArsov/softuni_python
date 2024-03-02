function palindromeIntegers(arr) {
  for (let i = 0; i < arr.length; i++) {
    const isPalindrome =
      arr[i] === parseInt(arr[i].toString().split("").reverse().join(""));
    console.log(isPalindrome);
  }
}

palindromeIntegers([123, 323, 421, 121]);
