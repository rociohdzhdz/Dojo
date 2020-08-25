
//1
var arr1 = [];
function array1(num) {
    for (var i = 1; i <= num; i++) {
        arr1.push(i);
    }
    return arr1;
}
var num = array1(255);
console.log(num);

//2

function evensum() {
    sum=0;
    for (var j = 1; j <= 1000; j++) {
        if(j % 2 == 0){
          sum +=j;  
        }
    }
    return sum;
}
console.log(evensum());

//3
var sum=0;
function oddsum (num3){
    for (var y=1; y<=num3; y+=2){
       sum+=y; 
    }
    return sum;
}
num3=oddsum(5000);
console.log("this is the sum of odd numbers", num3);

//4
var sumelem=0;
function sumarray(arr4){
    for(var z=0; z<arr4.length; z++ ){
        sumelem+=arr4[z];
    }
    return sumelem;

}
console.log(sumarray([2,5,-9]));

//5
function maxarray(arr5){
    var max=arr5[0];
    for( var ma=0; ma<arr5.length; ma++){
        if(max<arr5[ma]){
            max=arr5[ma];
        }
    }
return max;
}
console.log(maxarray([3,5,9,-11]));

//6

function averagearr(arr6){
var avg=0;
for(var av=0; av<arr6.length; av++){
    avg+=arr6[av];
} 
 return(avg/arr6.length);
}
console.log(averagearr([1,3,5,7,20]))

//7
newarr7=[];
function oddarray (arr7){
    for(od=1; od<=arr7; od+=2){
        newarr7.push(od)
    }
    return newarr7;
}
var arr7=oddarray(50);
console.log(arr7);

/*8
newarr8=[];
function greaterarr(arr8,n8){
    for(var gr=0; gr< arr8.length; gr++){
        if(arr8[gr]>n8){
            newarr8.push(arr8[gr]);
        }
    }
    return (newarr8.length);

}
arr8=greaterarr([1,2,4]);
n8=greaterarr(2);
console.log (res);*/

//9
newarr9=[];
function squarearray (arr9){
    for(sq=0;sq<arr9.length; sq++){
        newarr9.push(arr9[sq]*arr9[sq]);
    }
    return newarr9;
}
console.log(squarearray([1,5,10,-2]));

//10
newarr10=[];
function negativearr(arr10){
    for(ng=0; ng<arr10.length; ng++){
        if(arr10[ng]<0){
            var temp=arr10[ng]=0;
            newarr10.push(temp);
        }
        else {
            newarr10.push(arr10[ng]);
        }
    }
    return newarr10;
}
console.log(negativearr([1,-5,-7,9]));

//11
function MaxMinAvgArr(arr11){
    var newArr11=[];
    var Max11=arr11[0];
    var min11=arr11[0];
    var sum11=0;
    for (mma=1; mma<arr11.length;mma++){
        if(Max11<arr11[mma]){
            Max11=arr11[mma];
        }
        if(min11>arr11[mma]){
            min11=arr11[mma];
        }
        sum11+=arr11[mma];
        var avg11=sum11/arr11.length
    }
    newArr11.push(Max11);
    newArr11.push(min11);
    newArr11.push(avg11);
    return newArr11;
}
console.log(MaxMinAvgArr([1,5,10,-2]));

//12

function swapvaluesarr(arr12){
    var newarr12=[];
    for( sw=0; sw<arr12.length; sw++){
        var p1=arr12[0];
        if (sw==0){
            newarr12.push(arr12[arr12.length-1]);
        }
        else if(sw!=(arr12.length-1)){
            newarr12.push(arr12[sw]);
        }
        else {
            newarr12.push(p1);
        }   
    }
    return newarr12;
}
console.log(swapvaluesarr([1,5,10,-2]));



//13

function numToStringArr(arr13){
    for(nts=0; nts<arr13.length; nts++){
        if(arr13[nts] < 0){
            arr13[nts] = 'Dojo';
        }
    }
    return arr13;
}
console.log(numToStringArr([-1,-3,2]));
