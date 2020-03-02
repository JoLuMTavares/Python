/*
  +++++++++++++++++++++ This one in Javascript +++++++++++++++++++++

  You are at the gym and you would like to do some squats.You want to put some weight on barbell but first you must check if it is possible to do so.Weight on each side of the barbell must be equal.Each integer value is in kilograms so dont worry about units.Assume that barbell weights nothing.

  Guys i need your help with performance,right now tests cases are very small Max number of plates is 10,possible types [0.25,0.5,1,2,5]; Max total weight is 10.If you can send solution with better performance than mine i will make tests a bit harder with better performance too,Thanks!


*/

/*
 * @param  {Array} [availablePlates] array of positive integers/floats.
 * @param  {Integer} [requiredWeight]   total weight,integer/float >= 0;
 * @return False if barbell cannot be load with availablePlates,
 *         Otherwise possible combination in following format:
 *       [ [plates on left side] , [plates on right side]]
 *
 */

function putWeightsOnBarbell(availablePlates, requiredWeight) {
  if (requiredWeight === 0) return [[], []];
  var sideW = 0;
  lastPos = 0;
  leftPlates = [];
  rightPlates = [];
  for (i = 0; i < availablePlates.length; i++) {
    sideW += availablePlates[i];
    leftPlates[i] = availablePlates[i];
    if (sideW >= requiredWeight / 2) {
      lastPos = i;
      break;
    }
  }
  if (
    sideW < requiredWeight / 2 ||
    sideW > requiredWeight ||
    sideW > requiredWeight / 2 ||
    lastPos === availablePlates.length - 1
  )
    return false;
  else {
    sideW = 0;
    counter = 0;
    for (j = lastPos + 1; j < availablePlates.length; j++) {
      sideW += availablePlates[j];
      rightPlates[counter] = availablePlates[j];
      counter++;
      if (sideW > requiredWeight / 2) return false;
    }
  }
  // return [
  //   leftPlates.forEach(element => {
  //     console.log(element);
  //   }),
  //   rightPlates.forEach(element => {
  //     console.log(element);
  //   })
  // ];
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
