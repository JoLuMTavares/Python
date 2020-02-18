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
  first_p_l = []
  final_p_list = []
  if len(peak_arr) > 2:    
    p_val = max(peak_arr)
    if peak_arr.index(p_val) == 0:
      final_p_list +=  get_peak([peak_arr[i] for i in range(1, len(peak_arr))])
    elif peak_arr.index(p_val) == len(peak_arr)-1:
      final_p_list +=  get_peak([peak_arr[i] for i in range(len(peak_arr)-1)])
    else:
      for j in range(peak_arr.index(p_val)+1, len(peak_arr)):
        if peak_arr[j] != p_val:
          first_p_l.append(p_val)
          final_p_list = get_peak([peak_arr[i] for i in range(peak_arr.index(p_val))]) + first_p_l + get_peak([peak_arr[i] for i in range(peak_arr.index(p_val)+1, len(peak_arr))])
          return final_p_list
      else:
        final_p_list = get_peak([peak_arr[i] for i in range(peak_arr.index(p_val))])
  return final_p_list


# Auxiliary function to determine the peak positions
def get_peak_pos(original_arr, f_p_list, pos = 0):
  # Important. The comparison must be always in ascending order
  f_p_l_c = 0 
  peak_pos_list = []
  i = 1
  if len(original_arr) > 0:
    while i < len(original_arr):
      if original_arr[i] == f_p_list[f_p_l_c]:
        if original_arr[i] != original_arr[i-1]:
          f_p_l_c += 1
          peak_pos_list.append(i)
        if f_p_l_c == len(f_p_list):
          break
        i += 2
      else:
        i += 1
  return peak_pos_list


def pick_peaks(arr):
  main_peak_list = []
  main_peak_list_pos = []
  if len(arr) == 0:
    return {"pos": [], "peaks": []}
  fElem = arr[0]
  # equals = True
  for elem in arr:
    if not elem == fElem:
      break
  else:
    return {"pos": [], "peaks": []}
  pos_l = []
  peaks_l = []
  firstPeak = max(arr)
  pos = arr.index(firstPeak)
  if pos == len(arr)-1:
    subListP1 = [arr[i] for i in range(pos)]
    main_peak_result = pick_peaks(subListP1)
    return main_peak_result
  elif pos == 0:
    subListP2 = [arr[i] for i in range(pos, len(arr))]
    main_peak_result = pick_peaks(subListP2)
    return main_peak_result
  else:
    main_peak_list.append(firstPeak)
    pos_l.append(pos)
    peaks_l.append(firstPeak)
    subList1 = [arr[i] for i in range(0, pos)]
    subList2 = [arr[i] for i in range(pos+1, len(arr))]
    final_p_list = get_peak(subList1) + main_peak_list + get_peak(subList2)
    main_peak_list_pos = get_peak_pos(arr, final_p_list)
  return {"pos": main_peak_list_pos, "peaks": final_p_list}



print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
print(pick_peaks([2,1,3,1,2,2,2,2,1]))
print(pick_peaks([2,1,3,1,2,2,2,2]))
print(pick_peaks([2,1,3,2,2,2,2,5,6]))
print(pick_peaks([2,1,3,2,2,2,2,1]))
print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
print(pick_peaks([]))
print(pick_peaks([1,1,1,1]))
print(pick_peaks([1,2,3,9,17, 9, 18, 10, 17, 1, 4, 20, 4, 3, 1]))
print(pick_peaks([1,2,3,11,4, 17, 9, 16, 10, 17, 1, 10, 3, 4, 16, 3, 18, 12, 9, 5, 19, 3, 15, 12]))

print(pick_peaks([13, 8, -5, 16, 16, 3, 9, 4, 11, 11, 13, 1, 5, 9, -2, 18, 1, 4, 9, 1, 4, 10, 5, 2, 1, 14, 2, -4]))

# {'pos': [3, 10, 13, 15, 18, 21, 25], 'peaks': [16, 13, 9, 18, 9, 10, 14]} should equal {'pos': [3, 6, 10, 13, 15, 18, 21, 25], 'peaks': [16, 9, 13, 9, 18, 9, 10, 14]}

print(pick_peaks([11, 8, -2, 18, -3, 5, 11, -2, 20, 5, 6, -5, 19, -2, -5, 4, -4, -5, 9, 17, 0, 3, 19]))

# print(pick_peaks([1,2,3,11,4, 17, 9, 16, 10, 17, 1, 10, 3, 4, 16, 3, 18, 12, 9, 5, 19, 3, 15, 12]))

# print(pick_peaks([1,2,3,11,4, 17, 9, 16, 10, 17, 1, 10, 3, 4, 16, 3, 18, 12, 9, 5, 19, 3, 15, 12]))