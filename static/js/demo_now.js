//时间插件，只需要引入此文件，html页面创建一个使用nowTime类的容器就可以，例如：<div class="nowTime">此处会显示当前时间</div>
const doms = {
    nowTime: document.querySelector('.nowTime'),
    }
function nowTime() {
    const currentDate = new Date();
    const D = currentDate.getDay()
    const dateTimeString = currentDate.toLocaleString();
    const arr = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    doms.nowTime.innerHTML = '现在时间: ' + dateTimeString + ' ' + arr[D];
}
nowTime()
setInterval(nowTime, 1000)