/*
  +++++++++++++++++++++ This one in Javascript +++++++++++++++++++++

  You are at the gym and you would like to do some squats.You want to put some weight on barbell but first you must check if it is possible to do so.Weight on each side of the barbell must be equal.Each integer value is in kilograms so dont worry about units.Assume that barbell weights nothing.

  Guys i need your help with performance,right now tests cases are very small Max number of plates is 10,possible types [0.25,0.5,1,2,5]; Max total weight is 10.If you can send solution with better performance than mine i will make tests a bit harder with better performance too,Thanks!


*/

/*
 * ######### Fourth version #########
 *
 * @param  {Array} [availablePlates] array of positive integers/floats.
 * @param  {Integer} [requiredWeight]   total weight,integer/float >= 0;
 * @return False if barbell cannot be load with availablePlates,
 *         Otherwise possible combination in following format:
 *       [ [plates on left side] , [plates on right side]]
 *
 */

// Auxiliary function to get the min value of an array
const arrMin = arr => Math.min(...arr);

// Auxiliary function to get the max value of an array
const arrMax = arr => Math.max(...arr);

// Auxiliary function to make the sum of all elements in an array
const arrSum = arr => arr.reduce((a, b) => a + b, 0);

// Auxiliary function that tries to find the combination of barbells
// that equals half of the required weight
function findCombination(availablePlates, halfW) {
  sideW = 0;
  count = 0;
  lastPos = 0;
  lastBarb = 0;
  resultPlates = [];
  flBarbT = 0;
  flBarb = [];
  sum = 0;
  testArr = [...availablePlates];

  if (availablePlates.indexOf(halfW) !== -1) {
    resultPlates.push(availablePlates[availablePlates.indexOf(halfW)]);
    testArr.splice(testArr.indexOf(halfW), 1);
    return [resultPlates, testArr];
  }
  if (arrSum(availablePlates) === halfW) return [availablePlates, testArr];

  for (i = 0; i < availablePlates.length; i++) {
    if (lastPos !== i) {
      lastPos = i;
      sum = 0;
    }
    if (availablePlates[i] > halfW) continue;
    if (
      !Number.isInteger(availablePlates[i]) &&
      (Number.isInteger(halfW) || availablePlates[i] < halfW / 5)
    ) {
      if (flBarbT === 0) flBarbT = 1;
      flBarb.push(availablePlates[i]);
      continue;
    }
    if (sideW === 0 && count === 0) {
      count++;
      sideW += availablePlates[i];
      resultPlates.push(availablePlates[i]);
      testArr.splice(i, 1);
      sum = 1;
    }
    if (arrSum(resultPlates) === halfW) return [resultPlates, testArr];
    for (j = i + 1; j < availablePlates.length; j++)
      if (sideW + availablePlates[j] === halfW) {
        sideW += availablePlates[j];
        resultPlates.push(availablePlates[j]);
        testArr.splice(testArr.indexOf(availablePlates[j]), 1);
        break;
      } else if (
        !Number.isInteger(availablePlates[j]) ||
        sideW + availablePlates[j] > halfW
      )
        continue;
    if (
      resultPlates.length > 0 &&
      (arrSum(resultPlates) === halfW || arrSum(resultPlates) > halfW)
    )
      break;
    else if (count > 0 && i !== availablePlates.length && sum == 0) {
      count++;
      // sum = 0;
      if (sideW + availablePlates[i] <= halfW) {
        sideW += availablePlates[i];
        resultPlates.push(availablePlates[i]);
        testArr.splice(testArr.indexOf(availablePlates[i]), 1);
      }
    }
  }
  if (sideW > halfW) return false;
  else if (lastPos === availablePlates.length - 1 && sideW < halfW) {
    if (flBarb.length > 0) {
      flBarbSum = arrSum(flBarb);
      if (sideW + flBarbSum === halfW)
        for (s = 0; s < flBarb.length; s++) resultPlates.push(flBarb[s]);
      else {
        c = 0;
        while (c < flBarb.length) {
          for (j = c; j < flBarb.length; j++) {
            if (sideW + flBarb[j] === halfW) {
              sideW += flBarb[j];
              resultPlates.push(flBarb[j]);
              break;
            }
          }
          if (sideW < halfW && flBarb[c] >= halfW / 6) {
            sideW += flBarb[c];
            resultPlates.push(flBarb[c]);
            c++;
          } else c++;
        }
      }
    }
  }
  return [resultPlates, testArr];
}

// Auxiliary function that tries to find the sequence that equals half
// of the required weight. If this one is called, is because the first
// on didn't work. This function makes restrictions by dealing with the
// max value of the array and also the min. If the sum including the min
// value didn't work out, this one is separated from the array and the
// function calls it self again. This goes until a good combination is found.
// Otherwise, an empty array is returned.
function findSecCombination(arr, minV = 0, halfW) {
  minVal = 0;
  rightPlates = [];
  if (arr.length <= 2) {
    if (arrSum(arr) == halfW) return arr;
    else return [];
  }
  maxV = arrMax(arr);
  if (maxV === halfW) return [maxV];
  else if (maxV > halfW) arr.splice(arr.indexOf(maxV), 1);

  testArr = arr;
  if (minV === 0) {
    minVal = arrMin(arr);
    testArr.splice(arr.indexOf(minVal), 1);
    rightPlates.push(minVal);
  } else rightPlates.push(minV);

  if (minV > halfW || minVal > halfW) return false;
  if (minVal === halfW) return rightPlates;
  firstPos = 0;

  for (j = 0; j < testArr.length; j++) {
    nextSum = arrSum(rightPlates) + testArr[j];
    if (nextSum === halfW) {
      rightPlates.push(testArr[j]);
      return rightPlates;
    } else if (nextSum > halfW) continue;
    else if (j < testArr.length - 1) continue;
    rightPlates.push(arr[firstPos]);
  }
  if (arrSum(rightPlates) !== halfW)
    return findSecCombination(testArr, 0, halfW);

  if (arrSum(rightPlates) === halfW) return rightPlates;
  else return [];
}

function putWeightsOnBarbell(availablePlates, requiredWeight) {
  if (requiredWeight === 0) return [[], []];
  else if (requiredWeight < 0) return false;
  else if (availablePlates.length <= 2) {
    if (
      arrSum(availablePlates) !== requiredWeight ||
      arrMax(availablePlates) > requiredWeight / 2
    )
      return false;
    else if (
      availablePlates.length <= 1 ||
      arrMin(availablePlates) > requiredWeight / 2
    )
      return false;
    else return [[availablePlates[0]], [availablePlates[1]]];
  }

  var sideW = 0;
  count = 0;
  lastPos = 0;
  lastBarb = 0;
  // leftPlates = [];
  rightPlates = [];
  flBarbT = 0;
  flBarb = [];
  halfW = requiredWeight / 2;

  firstRes = findCombination(availablePlates, halfW);
  if (firstRes === false) return false;
  leftPlates = firstRes[0];
  testArr = firstRes[1];
  secondRes = [];
  rightPlates = [];
  secondTestArr = [...testArr];
  secondRes = findCombination(testArr, halfW);
  if (
    secondRes === false ||
    secondRes.length === 0 ||
    arrSum(secondRes[0]) !== halfW
  ) {
    secondRes = findSecCombination(secondTestArr, 0, halfW);
    if (secondRes === false || secondRes.length === 0) return false;
    else rightPlates = secondRes;
  } else rightPlates = secondRes[0];

  return [[...leftPlates], [...rightPlates]];
}

console.log(putWeightsOnBarbell([1, 5], 6));
console.log(putWeightsOnBarbell([1, 1, 1, 3], 6));
console.log(putWeightsOnBarbell([1, 1], 2));
console.log(putWeightsOnBarbell([1, 1], 0));
console.log(putWeightsOnBarbell([1, 1, 2, 7, 6], 16));
console.log(putWeightsOnBarbell([5, 1, 1, 4, 2, 8], 9));
console.log(putWeightsOnBarbell([4, 4, 4, 4], 16));
console.log(putWeightsOnBarbell([1, 1], 0));
console.log(putWeightsOnBarbell([1, 1, 3, 7, 4, 6], 16));
console.log(putWeightsOnBarbell([1, 0.5, 2, 0.25, 2, 1, 5, 1, 2], 8));
console.log(putWeightsOnBarbell([0.5, 0.5, 5, 5, 2, 1, 2, 0.5, 1], 5));
console.log(putWeightsOnBarbell([2, 0.25, 1, 0.5, 1, 2, 0.5, 0.5], 3));
console.log(putWeightsOnBarbell([1, 1, 3, 7, 4, 6], 16));
console.log(putWeightsOnBarbell([5, 5, 2, 5, 0.5, 2, 1, 1], 3));
console.log(putWeightsOnBarbell([1, 2, 1, 2, 2, 2, 0.5], 1));
console.log(putWeightsOnBarbell([0.5, 0.25, 1, 1, 0.5, 2, 2, 2, 0.5], 1));
console.log(putWeightsOnBarbell([0.5, 2, 5, 0.5, 1, 5, 1, 0.25, 1], 6));
console.log(putWeightsOnBarbell([0.25, 2, 5, 1, 1, 0.25, 0.25, 0.25, 2], 3));
console.log(putWeightsOnBarbell([0.5, 5, 0.25, 0.5, 2, 0.5, 0.5, 0.5], 4));
console.log(putWeightsOnBarbell([0.5, 1, 1, 1, 2, 2, 0.25], 8));
console.log(putWeightsOnBarbell([1, 1, 3, 7, 4, 6], 16));

// One single excellent solution made by Unnamed
function putWeightsOnBarbellUnamed(availablePlates, requiredWeight) {
  for (let i = 0; i < 3 ** availablePlates.length; i++) {
    const c = [...i.toString(3)].reverse();
    let ws = [, [], []];
    for (let [j, w] of availablePlates.entries()) if (+c[j]) ws[c[j]].push(w);
    const sw1 = ws[1].reduce((a, b) => a + b, 0),
      sw2 = ws[2].reduce((a, b) => a + b, 0);
    if (sw1 + sw2 == requiredWeight && sw1 == sw2) return [ws[1], ws[2]];
  }
  return false;
}
