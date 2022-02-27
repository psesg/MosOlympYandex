const defaultPlaceHolder = [false, false, false, false, false, false, false];

const diffMemory = {
  0: 0,
  10: 4,
  21: 5,
  32: 2,
  43: 3,
  54: 3,
  65: 1,
  76: 5,
  87: 4,
  98: 1,
  90: 2,
};

// Сюда цифры впишите
const numbers = [2, 55555, 3];
const memory = {
    0: 0
};
const calculate = (item) => {
    let index = item;
    while (!memory[index] && index >0) {
        index -= 1;
    }

    let delta = memory[index];
    let tmp = index
    for (let j = tmp + 1; j <= item; j++) {
        const numbersA = j.toString().split('').reverse().map(e => parseInt(e));
        const numbersB = (j-1).toString().split('').reverse().map(e => parseInt(e));
        if (numbersA.length != numbersB.length) {
            delta += 2
        }
        const minLength = Math.min(numbersA.length, numbersB.length);
        for (let i = 0; i < minLength; i++) {
            if (numbersA[i] == numbersB[i]) {
                continue
            }
            delta += diffMemory[Math.max(numbersA[i], numbersB[i]) * 10 + Math.min(numbersA[i], numbersB[i])];
        }
        current = j;
    }
    memory[item] = delta;
    return delta;
};
numbers.forEach((item) => {
    console.log(calculate(item));
});