console.log('Executed First');
setTimeout(() => {
 console.log('Executed Last, even if we set 0 seconds');
}, 2000);
console.log('Executed Second');
