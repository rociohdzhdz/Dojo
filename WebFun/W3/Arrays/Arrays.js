//Predict 1
var arr1 = [8,6,7,5,3,0,9]
for(var i = 0; i < arr1.length; i++){    
    console.log(arr1[i]);
}

//Predict 2
var arr2 = [7,3,8,4,2,0,1];
for(var i = 0; i < arr2.length; i++){ 
    if(arr2[i] % 2 == 0){
        console.log(arr2[i]);
    } 
    else{
        console.log("That is odd!");
    }
}

//Predict 3
var arr3 = [1,3,8,-5,0,-2,4,-1];
var newArr = [];
for(var i = 0; i< arr3.length; i++){
    if(arr3[i] < 0){
        newArr.push(arr3[i]);
        arr3[i] = arr3[i] * -1;
    }
    else if(arr3[i] == 0){
        arr3[i] = "Zero";
    }
    else{
        arr3[i] = arr3[i] * -1;
    }
}
console.log(arr3);
console.log(newArr);