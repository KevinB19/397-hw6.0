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

import pytest
import numpy as np

# from main import bubble_sort, quick_sort, insertion_sort
from basic_sort_UNIQUE_SUFFIX.int_sort import bubble, quick, insertion


def is_sorted(arr):
    """
    Helper function to check if an array is sorted.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


@pytest.fixture
def int_lists():
    """
    Fixture that creates testing data for all tests.
    """
    return [
        [3, 2, 1],
        [1, 1, 1],
        list(np.random.randint(low=-10, high=200, size=5)),
        [],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ]


@pytest.mark.parametrize("sort_function", [bubble, quick, insertion])
def test_sort(int_lists, sort_function):
    """
    Parametrized test that applies each sorting function to different lists.
    """
    for arr in int_lists:
        arr_copy = arr[:]  # Make a copy to preserve the original list
        sort_function(arr_copy)
        assert is_sorted(
            arr_copy
        ), f"List was not sorted by {sort_function.__name__}: {arr_copy}"
