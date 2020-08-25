//1
function numtoStr(arr1){
    for(nts=0; nts<arr1.length; nts++){
        if(arr1[nts] > 0){
            arr1[nts] = 'big';
        }
    }
    return arr1;
}
console.log(numtoStr([-1,-3,2]));

//2

function MinMaxArr(arr2){
    var newArr2=[];
    var Max2=arr2[0];
    var min2=arr2[0];
    var sum2=0;
    for (mm=1; mm<arr2.length;mm++){
        if(Max2<arr2[mm]){
            Max2=arr2[mm];
        }
        if(min2>arr2[mm]){
            min2=arr2[mm];
        }
    }
    newArr2.push(min2);
    newArr2.push(Max2);
    return newArr2;
}
console.log(MinMaxArr([1,5,10,-2]));

//3

function printreturn(arr3){
    var newarr3=[];
    for(pr=1; pr<arr3.length; pr++){
        if (arr3[0]%2==1){
            var numodd=arr3[0];
            console.log("The first odd number is: ", numodd);
        }
            newarr3.push(arr3[pr]);
    }
    return newarr3;  
}
console.log(printreturn([7,5,6,9]))

//4
function doublevision(arr4){
    var newarr4=[];
    for (dv=0; dv<arr4.length; dv++){
        newarr4.push((arr4[dv]*arr4[dv]));
    }
    return newarr4;
}
console.log(doublevision([4,8,16]));

//5
function countpositives (arr5){
    var newarr5=[];
    var counting=0;
    for(cp=0; cp<arr5.length; cp++){
        if(arr5[cp]>0){
            counting +=1;
            newarr5.push(arr5[cp]);
        }
        else{
            newarr5.push(arr5[cp]);
        }
    }
    newarr5.pop()
    newarr5.push(counting);
    //console.log(counting);
    return newarr5;
}
console.log(countpositives([-1,2,2,2]))

/*6-----
function evenodds(arr6){
    var newodds=[];
    var neweven=[];
    for(eo=0; eo<arr6.length; eo++){
        if(arr6[eo]%2==1){
            newodds.push(arr6);
        }
        else{
            neweven.push(arr6);
        }
        return neweven;
    }
    return newodds;
    
}

console.log(evenodds([2,2,2,5,6,7,8,9,9,9]));*/

//7
function incrementseconds(arr7){
    var newarr7=[];
    for( ins=1; ins<arr7.length; ins+=2){
        var sum7=arr7[ins]+1;
        newarr7.push(sum7);
    }
    return newarr7;
}
console.log(incrementseconds([2,5,7,23,35,42]));

//8
function previouslengths(arr8){
    var newarr8=[];
    for(pl=arr8.length-1; pl>=1; pl--){
        if (pl==1){
            newarr8[0]=arr8[0];
        }
        newarr8[pl]=(arr8[pl-1].length);
    }
    return newarr8;
}
console.log(previouslengths(["hello", "dojo", "awesome"]));

//9
function addseven(arr9){
    var newarr9=[];
    for (as=0; as<arr9.length; as++){
        newarr9.push((arr9[as]+7));
    }
    return newarr9;
}
console.log(addseven([4,8,16]));

//10
function reversearr(arr10){
    for(ra=0; ra<arr10.length/2; ra++){
        var temp10=arr10[ra];
        arr10[ra]=arr10[arr10.length-1-ra];
        arr10[arr10.length-1-ra]=temp10;
    }
    return arr10;
}
console.log(reversearr([1,2,3,4])); 

//11
function outnegative(arr11){
    var newarr11=[];
    for(on=0; on<arr11.length; on++){
        if(arr11[on]<0){
            newarr11.push(arr11[on]);
        }
        else{
            newarr11.push((arr11[on]*-1));
        }   
    }
    return newarr11;
}
console.log(outnegative([1,-2,-3,6]));

//12
function alwayshungry(arr12){
    var out12="";
    for(ah=0; ah<arr12.length; ah++){
        if(arr12[ah]="food"){
            console.log("yummy");
        }    
    }
    console.log("I´m hungry");
}
console.log(alwayshungry(["food", "food", "hamburger"]))

//13
function swapTowardCenter(arr13){
    for (var stc = 0; stc < arr13.length/2; stc+=2){
        var temparr13 = arr13[stc];
        arr13[stc] = arr13[arr13.length-1-stc];
        arr13[arr13.length-1-stc] = temparr13;
    }
    return arr13;
}
console.log(swapTowardCenter([1,2,3,4,5,6]));

//14
function scalearray(arr14, num14){
    for (var sca14 = 0; sca14 < arr14.length; sca14++){
        arr14[sca14] = arr14[sca14]*num14;
    }
    return arr14;
}
console.log(scalearray([1,2,3],3));
