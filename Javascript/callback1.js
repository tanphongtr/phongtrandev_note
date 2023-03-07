"use strict";

function test1(obj1={}) {
  if (obj1.hasOwnProperty('printName')) {
    console.log(obj1.printName('Phong'));
  }

  if (obj1.hasOwnProperty('printYearOld')) {
    obj1.printYearOld('29', (message) => { console.log(message) })
  }
}


var obj1 = {
  printName: (name) => `I am ${name}`,
  printYearOld: (old, cb) => {
    console.log(old);
    cb('callback run');
  }
}

test1(obj1);


// sample this in function

function test2() {
  console.log(this.name);
  return this;
}

console.log(test2.call({name: 'Phong'}));


// sample callback

function test3(cb) {
  cb();
}
