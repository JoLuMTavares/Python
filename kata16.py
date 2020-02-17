"""
++++++++++++++ Back to Python ++++++++++++++


In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!

"""

# Auxiliary function to determine the peak values
def get_peak(peak_arr):
  final_p_list = []
  if len(peak_arr) > 2:    
    p_val = max(peak_arr)
    if peak_arr.index(p_val) == 0:
      final_p_list +=  get_peak([peak_arr[i] for i in range(1, len(peak_arr))])
    elif peak_arr.index(p_val) == len(peak_arr)-1:
      final_p_list +=  get_peak([peak_arr[i] for i in range(len(peak_arr)-1)])
    else:
      final_p_list.append(p_val)
      final_p_list += get_peak([peak_arr[i] for i in range(peak_arr.index(p_val))]) + get_peak([peak_arr[i] for i in range(peak_arr.index(p_val)+1, len(peak_arr))])
  return final_p_list


# Auxiliary function to determine the peak positions
def get_peak_pos(original_arr, f_p_list, pos = 0):
  peak_pos_list = []
  for i in range (len(original_arr)):
    if original_arr[i] in f_p_list:
      peak_pos_list.append(i)
  return peak_pos_list


def pick_peaks(arr):
  main_peak_list = []
  main_peak_list_pos = []
  if len(arr) == 0:
    return []
  fElem = arr[0]
  # equals = True
  for elem in arr:
    if not elem == fElem:
      break
  else:
    return []
  pos_l = []
  peaks_l = []
  firstPeak = max(arr)
  pos = arr.index(firstPeak)
  if arr[pos+1] == None:
    subListP1 = [arr[i] for i in range(pos)]
    main_peak_result = pick_peaks(subListP1)
  elif arr[pos-1] == None:
    subListP2 = [arr[i] for i in range(pos, len(arr))]
    main_peak_result = pick_peaks(subListP2)
  else:
    main_peak_list.append(firstPeak)
    pos_l.append(pos)
    peaks_l.append(firstPeak)
    subList1 = [arr[i] for i in range(0, pos)]
    subList2 = [arr[i] for i in range(pos, len(arr))]
    main_peak_list += get_peak(subList1) + get_peak(subList2)
    main_peak_list_pos = get_peak_pos(arr, main_peak_list)
  return {"pos": main_peak_list_pos, "peaks": main_peak_list}



pick_peaks([1,2,3,6,4,1,2,3,2,1])
pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])
pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])
pick_peaks([2,1,3,1,2,2,2,2,1])
pick_peaks([2,1,3,1,2,2,2,2])
pick_peaks([2,1,3,2,2,2,2,5,6])
pick_peaks([2,1,3,2,2,2,2,1])
pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])
pick_peaks([])
pick_peaks([1,1,1,1])