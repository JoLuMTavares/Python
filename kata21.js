/*
  +++++++++++++++++++++ This one in Javascript +++++++++++++++++++++

  You are at the gym and you would like to do some squats.You want to put some weight on barbell but first you must check if it is possible to do so.Weight on each side of the barbell must be equal.Each integer value is in kilograms so dont worry about units.Assume that barbell weights nothing.

  Guys i need your help with performance,right now tests cases are very small Max number of plates is 10,possible types [0.25,0.5,1,2,5]; Max total weight is 10.If you can send solution with better performance than mine i will make tests a bit harder with better performance too,Thanks!


*/

/*
 * ######### New version #########
 *
 * @param  {Array} [availablePlates] array of positive integers/floats.
 * @param  {Integer} [requiredWeight]   total weight,integer/float >= 0;
 * @return False if barbell cannot be load with availablePlates,
 *         Otherwise possible combination in following format:
 *       [ [plates on left side] , [plates on right side]]
 *
 */

// Auxiliary function to get the max value of an array
const arrMax = arr => Math.max(...arr);

// Auxiliary function to make the sum of all elements in an array
const arrSum = arr => arr.reduce((a, b) => a + b, 0);

// Auxiliary function that tries to find the combination of barbells
// that equals half of the required weight
function findCombination(arr, maxV = 0, halfW) {
  maxVal = 0;

  if (arr.length <= 2) {
    if (arrSum(arr) == halfW) return arr;
    else return [];
  }
  testArr = [...arr]; // To be continued
  if (maxV === 0) {
    maxVal = arrMax(arr);
    arr.splice(arr.indexOf(maxVal), 1);
    while (maxVal > halfW) {
      maxVal = arrMax(arr);
      arr.splice(arr.indexOf(maxVal), 1);
    }
    rightPlates.push(maxVal);
  } else rightPlates.push(maxV);

  if (arrSum(rightPlates) === halfW) return rightPlates;

  for (j = 0; j < arr.length; j++) {
    if (arrSum(rightPlates) + arr[j] === halfW) {
      rightPlates.push(arr[j]);
      return rightPlates;
    } else if (arrSum(rightPlates) > halfW) {
      maxVal = arrMax(arr);
      arr.splice(arr.indexOf(maxVal), 1);
      return findCombination(arr, maxVal, halfW);
    }
    rightPlates.push(arr[j]);
  }
}

function putWeightsOnBarbell(availablePlates, requiredWeight) {
  if (requiredWeight <= 0) return [[], []];
  testArr = [...availablePlates];
  var sideW = 0;
  count = 0;
  lastPos = 0;
  lastBarb = 0;
  leftPlates = [];
  rightPlates = [];
  for (i = 0; i < availablePlates.length; i++) {
    if (sideW === 0 && count === 0) {
      count++;
      sideW += availablePlates[i];
      leftPlates.push(availablePlates[i]);
      testArr.splice(i, 1);
    }
    for (j = i + 1; j < availablePlates.length; j++)
      if (sideW + availablePlates[j] === requiredWeight / 2) {
        leftPlates.push(availablePlates[j]);
        testArr.splice(testArr.indexOf(availablePlates[j]), 1);
        break;
      } else if (sideW + availablePlates[j] > requiredWeight / 2) break;
    if (leftPlates.length > 0 && arrSum(leftPlates) === requiredWeight / 2)
      break;
    else if (count > 0 && i !== lastPos) {
      lastPos = i;
      count++;
      sideW += availablePlates[i];
      leftPlates.push(availablePlates[i]);
      testArr.splice(testArr.indexOf(availablePlates[i]), 1);
    }
  }
  if (
    sideW > requiredWeight ||
    sideW > requiredWeight / 2 ||
    lastPos === availablePlates.length - 1
  )
    return false;
  else {
    rightPlates = findCombination(testArr, 0, requiredWeight / 2);
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
