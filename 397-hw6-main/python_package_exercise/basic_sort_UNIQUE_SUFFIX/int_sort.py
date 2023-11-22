# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp


def bubble(int_list):
    """
    bubble docstring
    """
    print("bubble sort")

    finished_flag = True
    i = 0

    while i < len(int_list) - 1:
        if int_list[i] > int_list[i + 1]:
            finished_flag = False
            swap(int_list, i, i + 1)
        i += 1

    if not finished_flag:
        bubble(int_list)

    return


def quick(int_list):
    """
    qsort docstring
    """
    print("quick sort")
    # root cases
    if len(int_list) == 2:
        if int_list[0] > int_list[1]:
            swap(int_list, 0, 1)
        return
    elif len(int_list) < 2:
        return

    # pick pivot
    pivot = int_list[0]

    arr1 = []
    arr2 = []
    i = 1

    while i < len(int_list):
        if int_list[i] < pivot:
            arr1.append(int_list[i])
        else:
            arr2.append(int_list[i])
        i += 1

    # recurse on both arrays

    quick(arr1)
    quick(arr2)

    # put pivot between both arrays
    arr1.append(pivot)
    arr1.extend(arr2)

    int_list.clear()
    int_list.extend(arr1)

    # return
    return


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
    sorted_arr = []

    for curr_num in int_list:
        i = 0
        if len(sorted_arr) == 0:
            sorted_arr.append(curr_num)
        else:
            while i < len(sorted_arr):
                if curr_num < sorted_arr[i]:
                    sorted_arr.insert(i, curr_num)
                    break
                i += 1
            if i == len(sorted_arr):
                sorted_arr.append(curr_num)

    int_list.clear()
    int_list.extend(sorted_arr)
