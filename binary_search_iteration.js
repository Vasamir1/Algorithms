/*
Binary search in JavaScript 
*/


function binarySearch(arr, n){

    // Variables for start and end of the array
    let start = 0;
    let end = arr.length - 1;
    let mid = 0;
    
    // Condition for avoiding endless loop
    while(start <= end) {
        
        // Calculating middle of array
        mid = Math.floor((end + start) / 2);

        // If we found our number, lets return it 
        if (n === arr[mid]){
            return mid;
        }
        // If not, erease smaller side of array...
        else if (n > arr[mid]){
            start = mid + 1;
        }
        // ...or bigger size
        else {
            end = mid - 1;
        }
    }
    // If the number does not exist in array
    return -1;
}


// Variables for test
const test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
const searchedNumber = 2;
// Finding our number
let index = binarySearch(test, searchedNumber);

// Printing index of searched number or message that number was not found
if (index === -1){
    console.log("Number " + searchedNumber + " does not exist in given array.");
}
else{
    console.log("Number " + searchedNumber + " is on the index " + index + ".");
}
