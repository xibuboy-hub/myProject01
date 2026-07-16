const n = 10;
if (n > 0) {
    setTimeout(() => {
        // console.log('时间到');
        document.querySelector('#djs').innerHTML = '时间到';
    }, 1000 * n);}

for(let i = 0; i < n; i++) {
    setTimeout(() => {
        document.querySelector('#djs').innerHTML = `剩余时间: ${n - i} 秒`;
    }, 1000 * i);}