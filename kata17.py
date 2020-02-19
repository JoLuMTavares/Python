# Auxiliary function to determine the peak values
def get_peak(orig_arr, peak_arr):
  # One for the first peak and the other for the next possible ones
  first_p_l = []
  final_p_list = []
  # Checking if the given array has a length greater than two. Otherwise nothing
  # needs to be done.
  if len(peak_arr) > 2:
    # Getting the peak (always as the max)
    p_val = max(peak_arr)
    # Checking if this peak is at the beginning or at the end of the array
    if peak_arr.index(p_val) == 0 or peak_arr.index(p_val) == len(peak_arr)-1:
      # Another new array without the found peak
      new_arr = peak_arr.copy()
      new_arr.pop(peak_arr.index(p_val))
      # Calling the function recursively
      final_p_list = get_peak(orig_arr, new_arr)
      # returning the result
      return final_p_list
    else:
      # Also checking if there is at least one different element from the peak
      # (from the peak current position until the end of the array)
      for j in range(peak_arr.index(p_val)+1, len(peak_arr)):
        if peak_arr[j] != p_val:
          # If found a different one, we store the peak and split the array in two
          # (both withtout the peak)
          first_p_l.append(p_val) # Peak stored

          # The two temporary arrays must be evaluated separately
          temp_arr1 = get_peak(orig_arr, [peak_arr[i] for i in range(peak_arr.index(p_val))]) 
          temp_arr2 = get_peak(orig_arr, [peak_arr[i] for i in range(peak_arr.index(p_val)+1, len(peak_arr))])

          # The final one will have the result of the first temporary one
          final_p_list = temp_arr1
          # Then the stored peak is added to the end of the array stored on position
          # 1 from this array (since it contains the original array and the result)
          final_p_list[1] += first_p_l
          # Same operation as above, but adding the result from the second temporary
          # array
          final_p_list[1] += temp_arr2[1]
          # returning the result
          return final_p_list
      else:
        # If no different element was found, a new array (range until the peak 
        # position) will be evaluated (by calling the funcion again).
        final_p_list = get_peak(orig_arr, [peak_arr[i] for i in range(peak_arr.index(p_val))])
        # Returning the result
        return final_p_list
  # The original array is also returned
  return [orig_arr, final_p_list]


# Auxiliary function to determine the peak positions
def get_peak_pos(original_arr, f_p_list, pos = 0):
  # Important. The comparison must be always in ascending order
  f_p_l_c = 0 
  peak_pos_list = []
  i = 1
  # Checking if both arrays are not empty
  if len(original_arr) > 0 and len(f_p_list) > 0:
    while i < len(original_arr):
      # Comparison of the position on the original array to the one from the
      # array of peaks
      if original_arr[i] == f_p_list[f_p_l_c]:
        # Important to check if this peak is not a repeated one. This is because
        # the array of peaks may contain equal peak values, but these must be
        # always in different positions on the original array
        if original_arr[i] > original_arr[i-1]:
          f_p_l_c += 1
          peak_pos_list.append(i)
        if f_p_l_c == len(f_p_list):
          break
        # Increasing always i by 2 when a peak is found
        i += 2
      else:
        # Increasing i by 1 when the peak is not found 
        i += 1
  # returning the array of positions at the end
  return peak_pos_list


def pick_peaks(arr):
  # The result array of peaks, array of positions and a temporary
  # array for operations
  main_peak_list = []
  temp_arr = []
  main_peak_list_pos = []
  # Checking if the given array isn't empty
  if len(arr) == 0:
    return {"pos": [], "peaks": []}
  fElem = arr[0]
  # Important to check if there's at least one different element in the array
  for elem in arr:
    if not elem == fElem:
      break
  else:
    return {"pos": [], "peaks": []}
  # Continuing
  pos_l = []
  peaks_l = []
  # Getting the first peak (as max of the array)
  firstPeak = max(arr)
  # Getting its position
  pos = arr.index(firstPeak)
  # If this peak is at the beggining or end of the array, a new one
  # is created without the peak to restart the evaluation
  if pos == len(arr)-1 or pos == 0:
    temp_arr = arr.copy()
    temp_arr.pop(pos)
    main_peak_list = get_peak(arr, temp_arr)
  else:
    # If not, it's stored in a single temporary array
    temp_arr = []
    temp_arr.append(firstPeak)
    pos_l.append(pos)
    peaks_l.append(firstPeak)
    # Two new arrays are created (without the found peak) to divide (but not affect)
    # the current one in two. These two will be evaluated by calling the auyiliary
    # function - get_peak(orignal array, array to be evaluated)
    subList1 = [arr[i] for i in range(0, pos)]
    subList2 = [arr[i] for i in range(pos+1, len(arr))]
    # Evaluating the first new array and affecting this to the final array of peaks
    main_peak_list = get_peak(arr, subList1) 
    # Created a second temporary array to store the result of the second array created above
    temp_arr2 = get_peak(arr, subList2)
    # Adding the temporary array to the end of the array of peaks (stored in 
    # position 1 of the returned result)
    main_peak_list[1] += temp_arr
    # Same operation as above, but adding also the array stored in position 1
    # from the returned result
    main_peak_list[1] += temp_arr2[1]
  # Calling the function to get the positions of the peaks. This is way the original # array need to be transported. This way the found positions will always be the
  # original ones.
  main_peak_list_pos = get_peak_pos(main_peak_list[0], main_peak_list[1])
  # returning the final result.
  return {"pos": main_peak_list_pos, "peaks": main_peak_list[1]}



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

print(pick_peaks([12, -5, 10, 12, 8, 1, 11, 1, 12, -1, 11, -3, 7, -3, -1]))

print(pick_peaks([14, 2, -1, 10, 11, 17, 18]))

"""
This one finally works. 

Now the bad news...

What seems to be a great achievement, it's actually a disgrace compared to other solutions that will be presented bellow.
"""

# Made by roadischosen, angdftyq353554, t304322, user957258, dhk, zhangyh

def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}

# As simple as this. No more than 10 lines.

# Made by Koren, pompeu2004, Miracleyin, yashjain039, 赵月-, Wang Qing En (plus 8 more warriors)

def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }
    
    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]
        
        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    
    return res


# Made by Mr.Relax, didipala

def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    prev, cur = 0, 0
    for next in xrange(1, len(arr)):
        if arr[next] > arr[cur]:
            prev = cur
            cur = next
        elif arr[next] < arr[cur]:
            if arr[cur] > arr[prev]:
                res['pos'].append(cur)
                res['peaks'].append(arr[cur])
            prev = cur
            cur = next
    return res

# Made by biskinis

from itertools import izip


def pick_peaks(a):
    deltas = [(i, x2 - x1) for i, (x1, x2) in enumerate(izip(a, a[1:]), 1) if x1 != x2]
    indexes = [i for (i, dx1), (_, dx2) in izip(deltas, deltas[1:]) if dx1 > 0 > dx2]
    return dict(pos=indexes, peaks=[a[i] for i in indexes])
# Professional this last one.

# One main difference. I focused on getting so well the peaks, that I forgot how 
# easier it would be to get the positions of these peaks and then just getting
# the peaks for each position.
# The lesson here is to always consider every possibilities, but check which one
# is the most efficient.