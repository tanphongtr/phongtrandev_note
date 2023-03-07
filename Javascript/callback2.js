// sample promise

function test4() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("success");
    }, 2000);
  });
}

async function test5() {
  console.time("test");
  // const result = await test4();
  // const result2 = await test4();

  let [a, b] = await Promise.all([test4(), test4()]);
  // console.log(result);

  console.log(a, b)
}

test5();
