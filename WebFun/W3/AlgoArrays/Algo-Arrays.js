var testArr=[6,3,5,1,2,4]
var sum=0;
var mult;
var newArr=[];

for(i=0; i<testArr.length; i++){
    sum+=testArr[i]
    console.log('num:', testArr[i], 'sum:', sum)
    mult=testArr[i]*i;
    newArr.push(mult);
}
console.log (newArr);