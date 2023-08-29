/*
Binary Search with iteration
*/

#include <algorithm>
#include <iostream>
using namespace std;


int binarySearch(int arr[], int start, int end, int n)
{
    //  Condition to end searching at some point
    while (start <= end){

        //  Calculating the middle of array
        int mid = start + (end - start) / 2;

        //  If we found our number, let's return the index...
        if (n == arr[mid]){
            return mid;
        }
        //  ...if not, let's check if we should erase left or right part of arr
        else if (n > arr[mid]){
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }
    //  If we did not find our number
    return -1;
}


int main()
{
    //  Array variable
    int numbers[12] = {223, 90, 73, 13, 8874, 7, 67, 24, 1212, 56, 48, 11};
    int length = sizeof(numbers)/sizeof(numbers[0]);

    //  Looking number
    int n = 73;
    
    //  Sorting array
    std::sort(numbers, numbers+length);
    
    //  Array afte sorting:
    for(int i=0; i<length; i++)
    {
        cout << numbers[i] << " ";
    }
    cout << endl;

    int binSearch = binarySearch(numbers, 0, length-1, n);

    if (binSearch == -1){
    cout << "There is not such a number in array." << endl;
    }
    else{
cout << "The number "<< n << " is on the index "<< binSearch << "." << endl;
    }
}