function get_shift() {
    if (new Date().getHours() >= 8 && new Date().getHours() < 20) {
        $('input[type="radio"]:first').prop('checked', true);
        $('#area_sub').text('SUB白_UPPH')
        $('#area_tnb').text('TNB白_UPPH')
        // console.log('获取班别成功',$('input:radio:first')[0].checked)
    } else {
        $('input[name="shift"]').get(1).checked = true;
        $('#area_sub').text('SUB夜_UPPH')
        $('#area_tnb').text('TNB夜_UPPH')
    }
}

get_shift()
const sub_em = document.querySelector('#sub_em')
const tnb_em = document.querySelector('#tnb_em')
const sub_ew = document.querySelector('#sub_ew')
const tnb_ew = document.querySelector('#tnb_ew')
const table = document.querySelector('.table-group-divider')

let timerId = null;
let n = 12;

//输入框sub_em_Input失去焦点
sub_em.addEventListener('blur', function () {
    console.log('sub_em_Input失去了焦点');
    sub_em.disabled = true;
    // 在这里执行你的代码，比如验证输入等
});
sub_ew.addEventListener('blur', function () {
    console.log('sub_em_Input失去了焦点');
    this.disabled = true;
    // 在这里执行你的代码，比如验证输入等
});
tnb_ew.addEventListener('blur', function () {
    console.log('sub_em_Input失去了焦点');
    this.disabled = true;
    // 在这里执行你的代码，比如验证输入等
});
//按钮解锁，输入框sub_em_Input获得焦点
document.querySelector('#sub').addEventListener('click', function () {
    console.log('sub_em_Input获得了焦点');
    sub_em.disabled = false;
    sub_ew.disabled = false
    $('#btn')[0].disabled = false;
    $('#btn')[0].classList.remove('btn-secondary')
    clearInterval(timerId)
    n = 3
    // 在这里执行你的代码，比如验证输入等
});
//输入框tnb_em_Input失去焦点
tnb_em.addEventListener('blur', function () {
    console.log('tnb_em_Input失去了焦点');
    tnb_em.disabled = true;
    // 在这里执行你的代码，比如验证输入等
});
//按钮解锁，输入框tnb_em_Input获得焦点
document.querySelector('#tnb').addEventListener('click', function () {
    console.log('tnb_em_Input获得了焦点');
    tnb_em.disabled = false;
    tnb_ew.disabled = false
    clearInterval(timerId)
    n = 3
    $('#btn')[0].disabled = false;
    $('#btn')[0].classList.remove('btn-secondary')
    // 在这里执行你的代码，比如验证输入等
});

// 检测时间是否在16:00~16:10
function checkAlert() {
    const now = new Date();
    const startTime = new Date().setHours(16, 0, 0)
    const endTime = new Date().setHours(16, 5, 0)
    const isInTimeRange = (now >= startTime && now <= endTime);
    if (isInTimeRange && $('#sub_em').val() !== '' && $('#tnb_em').val() !== '') {
        console.log('该起床啦~')
        var sub_o_hr = Math.ceil((parseInt($('#sub_gs').text().split(":")[1]) - parseInt($('#sub_cl').text().split(":")[1]) / 9.21) / ((new Date() - new Date().setHours(8, 0, 0)) / 1000 / 3600 - 1))
        var tnb_o_hr = Math.ceil((parseInt($('#tnb_gs').text().split(":")[1]) - parseInt($('#tnb_cl').text().split(":")[1]) / 10.86) / ((new Date() - new Date().setHours(8, 0, 0)) / 1000 / 3600 - 1))
        alert(`SUB产能预计还差:${parseInt(parseInt($('#sub_em').val()) * 10 * 9.21) - parseInt($('#sub_cl').text().split(":")[1])},或预计放${sub_o_hr}人下班
TNB产能预计还差:${parseInt(parseInt($('#tnb_em').val()) * 10 * 10.86) - parseInt($('#tnb_cl').text().split(":")[1])},或预计放${tnb_o_hr}人下班`)
    } else {
        clearInterval(intervalId);
        intervalId = undefined;
        flag = true;
        console.log('已经起床。')
    }
}

var intervalId = undefined;
let flag = true

function alarm_detect() {
    if (new Date() >= new Date().setHours(16, 0, 0) && new Date() <= new Date().setHours(16, 0, 11)) {
        // const div=document.getElementById('marquee_text')
        // var p=document.createElement('div')
        // p.style.width="100%;"
        // p.innerHTML=`<marquee loop="1" behavior="slide">test</marquee>`
        // div.appendChild(p)
        if (flag) {
            checkAlert();
            intervalId = setInterval(checkAlert, 60000)
            flag = false
        }
        console.log('任务已启动~')
    }
    // console.log('时间未到~，任务不启动~')
}

//启动定时器
function js() {
    n--;
    $('#js')[0].innerText = `${n - 1}秒后刷新`
    if (n === 5) {
        // 自动获取班别
        get_shift();
        // 弹窗提示产能差异
        alarm_detect();
        // 获取upph数据
        get_upph_data();
    }
    if (n < 3) {
        n = 12;
    }
}

function qidongInterval() {
    get_upph_data();
    $('#btn')[0].disabled = true;
    $('#btn')[0].classList.toggle('btn-secondary')
    timerId = setInterval(js, 1000)
}

//发送异步请求获取数据
function get_upph_data() {
    // get_shift()
    localStorage.setItem('sub_hr', sub_em.value || 15)
    localStorage.setItem('tnb_hr', tnb_em.value || 25)
    //获取请求参数
    const data = {
        'sub_hr': localStorage.getItem('sub_hr' || 8),
        'tnb_hr': localStorage.getItem('tnb_hr' || 17),
        'shift': $("input[name='shift']:checked").val()
    };
    var key='qazwsxedcrfvtgby';
    var encrypted=CryptoJS.AES.encrypt(JSON.stringify(data),key,{
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    }).toString()
    //测试打印数据到控制台
    //console.log(sub_em.value,tnb_em.value)
    fetch('/other/upph', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({"encrypted":encrypted,"st":Date.now(),"sign":parseInt(Math.random()*10)}),
    })
        .then((res) => res.json())
        .then((data) => {
            //测试打印数据到控制台
            //console.log(data);
            let sub_qty_hr, tnb_qty_hr, sub_upph, tnb_upph
            $('#sub_ew').val() === '' ? sub_qty_hr = data[0].qty_hr : sub_qty_hr = (data[0].qty_hr + parseFloat($('#sub_ew').val())).toFixed(2)
            $('#tnb_ew').val() === '' ? tnb_qty_hr = data[1].qty_hr : tnb_qty_hr = (data[1].qty_hr + parseFloat($('#tnb_ew').val())).toFixed(2)

            $('#sub_ew').val() === '' ? sub_upph = (data[0].product_qty / data[0].qty_hr).toFixed(2) : sub_upph = (data[0].product_qty / sub_qty_hr).toFixed(2)
            $('#tnb_ew').val() === '' ? tnb_upph = (data[1].product_qty / data[1].qty_hr).toFixed(2) : tnb_upph = (data[1].product_qty / tnb_qty_hr).toFixed(2)


            $('#sub_cl').text(`产量:${data[0].product_qty}`)
            $('#sub_gs').text(`工时:${sub_qty_hr}`)
            $('#sub_upph').text(`UPPH:${sub_upph}-${(sub_upph / 9.21 * 100).toFixed(2)}%`)
            $('#tnb_cl').text(`产量:${data[1].product_qty}`)
            $('#tnb_gs').text(`工时:${tnb_qty_hr}`)
            $('#tnb_upph').text(`UPPH:${tnb_upph}-${(tnb_upph / 10.85 * 100).toFixed(2)}%`)
            // 变色提醒
            if (parseFloat($('#sub_upph')[0].innerText.split(':')[1]) > 9.21) {
                $('#sub_upph')[0].classList.add('up1')
            } else if (parseFloat($('#sub_upph')[0].innerText.split(':')[1].split('-')[0]) > 9.21 * 0.9) {
                $('#sub_upph')[0].classList.add('goal')
                $('#sub_upph')[0].classList.remove('up1')

            } else {
                $('#sub_upph')[0].classList.remove('goal')
                $('#sub_upph')[0].classList.remove('up1')
            }
            if (parseFloat($('#tnb_upph')[0].innerText.split(':')[1]) > 10.86) {
                $('#tnb_upph')[0].classList.add('up1')
            } else if (parseFloat($('#tnb_upph')[0].innerText.split(':')[1].split('-')[0]) > 10.86 * 0.9) {
                $('#tnb_upph')[0].classList.add('goal')
                $('#tnb_upph')[0].classList.remove('up1')
            } else {
                $('#tnb_upph')[0].classList.remove('up1')
                $('#tnb_upph')[0].classList.remove('goal')
            }
            // 显示下方趋势图
            // show_upph_to_html();
        })
        .catch((error) => {
            console.log(error, '这个有问题~');
            alert('数据获取出错了，请联系管理员处理。'+ error)
        })
}
$("#refresh").click(()=>{
    alert("开始手动刷新！")
    get_upph_data()
})
// 异步添加数据至数据库
function add_upph() {
    if ((new Date().getHours() === 20 && new Date().getMinutes() === 0) || (new Date().getHours() === 8 && new Date().getMinutes() === 0)) {
        console.log('时间到了，开始添加数据！')
        data = {
            "u_date": new Date().toLocaleString().split(' ')[0].replaceAll('/', '-').replace('2025-', ''),
            "u_sub": parseFloat($('#sub_upph')[0].innerText.split(':')[1]),
            "u_tnb": parseFloat($('#tnb_upph')[0].innerText.split(':')[1])
        }
        fetch('/other/add_upph', {
            method: 'POST',
            body: JsonStringfy(data),
            headers: {ContentType: 'application/json'}
        }).then(response => response.json()).then((data) => {
            console.log(data, '恭喜你，添加数据成功！')
        }).catch((error) => {
            alert(error, '添加数据出错了！')
        })
    } else {
        console.log('时间没到，数据暂时不添加！')
    }

}


// 白夜班切换，变更对应文字
// $('input[name="shift"]').click((e) => {
//     if (e.target.defaultValue === '夜') {
//         $('#area_sub').text('SUB夜_UPPH')
//         $('#area_tnb').text('TNB夜_UPPH')
//     } else {
//         $('#area_sub').text('SUB白_UPPH')
//         $('#area_tnb').text('TNB白_UPPH')
//     }
//     get_upph_data();
// })

