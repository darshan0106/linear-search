##Linear Search Algorithm##
**Introduction**
Linear search, also known as sequential search, is the simplest search algorithm. It works by iterating through each element of a list until the desired element (key) is found or the end of the list is reached.

**Time Complexity**
Best Case: O(1) - The key is found at the first position.
Average Case: O(n) - The key is somewhere in the middle of the list.
Worst Case: O(n) - The key is either at the last position or not present in the list at all.
Here, n is the number of elements in the list.

**Code Explanation**

**Function Definition:**
The linearSearch function takes two parameters: arr (a list of integers) and key (the integer to search for).

**Iterating through the List:**
A for loop iterates through each element in arr.
For each element i, it checks if i is equal to key.

**Return Index if Found:**
If i is equal to key, it returns the index of i in arr using arr.index(i).

**Key Not Found:**
If the loop completes without finding key, the function returns "Key not Found".

**User Input:**
The user is prompted to enter the elements of the list as a space-separated string. This input is converted to a list of integers using map and list.
The user is then prompted to enter the key to search for.

**Function Call and Result:**
The linearSearch function is called with the user-provided list and key.
The result of the search (index of the key or "Key not Found") is printed to the console.

**Usage**
1) Run the code.
2) Enter the elements of the list when prompted. Separate each element with a space.
3) Enter the key to search for.
4) The program will output the index of the key if it is found in the list or "Key not Found" if the key is not present in the list.
