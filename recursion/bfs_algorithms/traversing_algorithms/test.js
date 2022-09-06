// let arr = [1, 2, 2, 3, 4, 5, 6, 6, 4, 6, 8, 9, 10, 10]

// function removeDuplicates(arr) {
//     const set1 = new Set(arr);
//     let sums = 0
//     set1.forEach(element => {
//         if (element % 2 == 0) {
//             sums += element
//         }
//     });
//     return sums
// }

let wordStr = "WeAreTogether"
    // We are together
function strOut(wordStr) {
    //split into arr via Capital letters
    let wordArr = wordStr.split(/(?=[A-Z])/)
    wordArr[0].toUpperCase()
    for (let i = 1; i < wordArr.lengh; i++) {
        wordArr[i].toLowerCase()
    }
    let sents = wordArr.join(" ")
    return sents
}


console.log(strOut(wordStr))