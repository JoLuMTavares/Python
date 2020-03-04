/*
  +++++++++++++++++++++ This one in Javascript +++++++++++++++++++++

  You are at the gym and you would like to do some squats.You want to put some weight on barbell but first you must check if it is possible to do so.Weight on each side of the barbell must be equal.Each integer value is in kilograms so dont worry about units.Assume that barbell weights nothing.

  Guys i need your help with performance,right now tests cases are very small Max number of plates is 10,possible types [0.25,0.5,1,2,5]; Max total weight is 10.If you can send solution with better performance than mine i will make tests a bit harder with better performance too,Thanks!


*/

/*
 * ######### Third version #########
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
function findCombination(arr, minV = 0, halfW) {
  minVal = 0;

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

  if (arrSum(rightPlates) === halfW) return rightPlates;

  for (j = 0; j < testArr.length; j++) {
    nextSum = arrSum(rightPlates) + testArr[j];
    if (nextSum === halfW) {
      rightPlates.push(testArr[j]);
      return rightPlates;
    } else if (nextSum > halfW) continue;
    else if (j < testArr.length - 1) continue;
    rightPlates.push(arr[j]);
    if (arrSum(rightPlates) > halfW) {
      // minVal = arrMin(testArr);
      // testArr.splice(arr.indexOf(minVal), 1);
      return findCombination(testArr, 0, halfW);
    }
  }
  if (arrSum(rightPlates) === halfW) return rightPlates;
  else return [];
}

function putWeightsOnBarbell(availablePlates, requiredWeight) {
  if (requiredWeight === 0) return [[], []];
  else if (requiredWeight < 0) return false;
  testArr = [...availablePlates];
  var sideW = 0;
  count = 0;
  lastPos = 0;
  lastBarb = 0;
  leftPlates = [];
  rightPlates = [];
  flBarbT = 0;
  flBarb = [];
  halfW = requiredWeight / 2;

  for (i = 0; i < availablePlates.length; i++) {
    if (availablePlates[i] > halfW) continue;
    if (!Number.isInteger(availablePlates[i]) && Number.isInteger(halfW)) {
      if (flBarbT === 0) flBarbT = 1;
      flBarb.push(availablePlates[i]);
      continue;
    }
    if (sideW === 0 && count === 0) {
      count++;
      sideW += availablePlates[i];
      leftPlates.push(availablePlates[i]);
      testArr.splice(i, 1);
    }
    for (j = i + 1; j < availablePlates.length; j++)
      if (!Number.isInteger(availablePlates[j])) continue;
      else if (sideW + availablePlates[j] === halfW) {
        leftPlates.push(availablePlates[j]);
        testArr.splice(testArr.indexOf(availablePlates[j]), 1);
        break;
      } else if (sideW + availablePlates[j] > halfW) continue;
    if (leftPlates.length > 0 && arrSum(leftPlates) === halfW) break;
    else if (leftPlates.length > 0 && arrSum(leftPlates) > halfW) break;
    else if (count > 0 && i !== lastPos) {
      lastPos = i;
      count++;
      sideW += availablePlates[i];
      leftPlates.push(availablePlates[i]);
      testArr.splice(testArr.indexOf(availablePlates[i]), 1);
    }
  }
  if (sideW > requiredWeight || sideW > halfW) return false;
  else if (lastPos === availablePlates.length - 1 && sideW < halfW) {
    if (flBarb.length > 0) {
      flBarbSum = arrSum(flBarb);
      if (sideW + flBarbSum === halfW) leftPlates.push(flBarbSum);
      else {
        c = 0;
        while (c < flBarb.length) {
          for (j = c + 1; j < flBarb.length; j++) {
            if (sideW + flBarb[j] === halfW) {
              sideW += flBarb[j];
              leftPlates.push(flBarb[j]);
              break;
            }
          }
          sideW += flBarb[j];
        }
      }
    }
  } else {
    rightPlates = findCombination(testArr, 0, halfW);
    if (rightPlates.length === 0) return false;
  }

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
