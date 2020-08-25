var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];
//Print jhon's age

console.log(users[1].age);

//Print the name of the first object
console.log(users[0].name);

//Print the name and age of each user using a for loop
for (var namesA in users){
    console.log(users[namesA].name, " - ", users[namesA].age);
}