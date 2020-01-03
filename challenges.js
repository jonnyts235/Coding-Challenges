const alphabetizer = str => {
  return str
    .split("")
    .sort()
    .join("")
    .trim();
};

console.log(alphabetizer("hello"));

/* Coding Challenge 1 */

const dictionary = {
  josh: 5,
  jonny: 7,
  jackson: 5
};

const add = num => {
  const arr = Object.values(num);
  return arr.reduce((a, b) => a + b);
};

add(dictionary);

/* Coding Challenge 2 */

const rotator = times => {
  const array = [1, 2, 3, 4, 5, 6, 7];
  let counter = 0;
  while (counter < times) {
    const first = array.shift();
    array.push(first);
    counter++;
  }
  return array;
};
rotator(5);

/* Coding Challenge 3 */

const addingFunction = () => {
  list = [1, 2, 3, 4, 5];
  return list.reduce((a, b) => a + b);
};

addingFunction();

/* Weighted Lottery Function */

const weightedLottery = weights => {
  // keep track of your  weights
  // ['green', 'yellow', 'yellow', 'red', 'red', 'red']
  let containerArray = [];

  Object.keys(weights).forEach(key => {
    for (let i = 0; i < weights[key]; i++) {
      containerArray.push(key);
    }
  });

  return containerArray[(Math.random() * containerArray.length) | 0];
};

const weights = {
  winning: 1,
  losing: 1000
};

weightedLottery(weights);
