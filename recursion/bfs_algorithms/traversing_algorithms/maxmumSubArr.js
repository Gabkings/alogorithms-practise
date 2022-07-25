function getMaxSubArry(inputArr, sizeArr) {
    if (inputArr.length == 0) return [];

    let currentSum = 0;
    let maxSum = 0;
    let startIndex = 0;

    inputArr.forEach((element, index) => {
        currentSum += element;

        if (index < sizeArr) {
            maxSum = currentSum;
        } else {
            currentSum -= inputArr[index - sizeArr];
            if (currentSum > maxSum) {
                maxSum = currentSum;
                startIndex = index - sizeArr + 1;
            }
        }
    });

    return inputArr.slice(startIndex, startIndex + sizeArr);
}

function getSubArr(inputArr, desiredSum) {
    let sum = 0;
    let sumStartIdx = 0;
    const solutions = [];

    inputArr.forEach((element, index) => {
        sum += element;
        while (sum > desiredSum) {
            sum -= inputArr[sumStartIdx];
            sumStartIdx++;
        }
        if (sum === desiredSum)
            solutions.push(inputArr.filter((_, i) => i >= sumStartIdx && i <= index));
    });

    return solutions;
}

// const exampleInput1 = [-1, 2, 3, 0, -3, 9];
// const subarraySize1 = 2;
// const solution1 = [-3, 9];

const exampleInput1 = [1, 7, 9, 4, 3, 2, 2];
const desiredSum1 = 7;
const solution1 = [
    [7],
    [4, 3],
    [3, 2, 2]
];

const calculatedSolution1 = getSubArr(exampleInput1, desiredSum1);

console.log(calculatedSolution1.forEach((item, index) => console.log(item)));