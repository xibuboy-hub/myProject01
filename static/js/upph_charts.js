var myChart1 = echarts.init(document.getElementById('main_sub'));
var myChart2 = echarts.init(document.getElementById('main_tnb'));
// const myChart = echarts.init(document.getElementById('upph_echarts'));
let sub_qty_hr, tnb_qty_hr, sub_upph, tnb_upph
// 实时UPPH达成率仪表盘
function yibiaopan(data) {
    // sub仪表盘
    $('#sub_ew').val() === '' ? sub_qty_hr = data.data.qty_hr_sub : sub_qty_hr = (data.data.qty_hr_sub + parseFloat($('#sub_ew').val())).toFixed(2)
    // $('#tnb_ew').val() === '' ? tnb_qty_hr = data[1].qty_hr : tnb_qty_hr = (data[1].qty_hr + parseFloat($('#tnb_ew').val())).toFixed(2)

    $('#sub_ew').val() === '' ? sub_upph = (data.data.product_qty_sub / data.data.qty_hr_sub).toFixed(2) : sub_upph = (data.data.product_qty_sub / sub_qty_hr).toFixed(2)
    // $('#tnb_ew').val() === '' ? tnb_upph = (data[1].product_qty / data[1].qty_hr).toFixed(2) : tnb_upph = (data[1].product_qty / tnb_qty_hr).toFixed(2)
    var option1;
    option1 = {
        series: [
            {
                type: 'gauge',
                axisLine: {
                    lineStyle: {
                        width: 25,
                        color: [
                            [0.45, '#fd666d'],
                            // [0.7692, '#37a2da'],
                            [0.5, '#A9F5C5'],
                            // [1.3, '#67e0e3']
                            [1.0, 'green']
                        ]
                    }
                },
                pointer: {
                    itemStyle: {
                        color: 'auto'
                    }
                },
                axisTick: {
                    distance: -25,
                    length: 8,
                    lineStyle: {
                        color: '#fff',
                        width: 2
                    }
                },
                splitLine: {
                    distance: -25,
                    length: 25,
                    lineStyle: {
                        color: '#fff',
                        width: 4
                    }
                },
                axisLabel: {
                    color: 'black',
                    distance: 36,
                    fontSize: 12
                },
                detail: {
                    valueAnimation: true,
                    formatter: '{value} %',
                    color: 'inherit',
                    fontSize:20
                },
                data: [
                    {
                        value: (sub_upph / 9.21 * 100).toFixed(2)
                    }
                ]
            }
        ]
    };
    option1.series[0].max = 200;
    option1 && myChart1.setOption(option1);

    // TNB仪表盘
        // $('#sub_ew').val() === '' ? sub_qty_hr = data[0].qty_hr : sub_qty_hr = (data[0].qty_hr + parseFloat($('#sub_ew').val())).toFixed(2)
    $('#tnb_ew').val() === '' ? tnb_qty_hr = data.data.qty_hr_tnb : tnb_qty_hr = (data.data.qty_hr_tnb + parseFloat($('#tnb_ew').val())).toFixed(2)

    // $('#sub_ew').val() === '' ? sub_upph = (data[0].product_qty / data[0].qty_hr).toFixed(2) : sub_upph = (data[0].product_qty / sub_qty_hr).toFixed(2)
    $('#tnb_ew').val() === '' ? tnb_upph = (data.data.product_qty_tnb / data.data.qty_hr_tnb).toFixed(2) : tnb_upph = (data.data.product_qty_tnb / tnb_qty_hr).toFixed(2)
    var option2;
    option2 = {
        series: [
            {
                type: 'gauge',
                axisLine: {
                    lineStyle: {
                        width: 25,
                        color: [
                            [0.45, '#fd666d'],
                            // [0.7692, '#37a2da'],
                            [0.5, '#A9F5C5'],
                            // [1.3, '#67e0e3']
                            [1.0, 'green']
                        ]
                    }
                },
                pointer: {
                    itemStyle: {
                        color: 'auto'
                    }
                },
                axisTick: {
                    distance: -25,
                    length: 8,
                    lineStyle: {
                        color: '#fff',
                        width: 2
                    }
                },
                splitLine: {
                    distance: -25,
                    length: 25,
                    lineStyle: {
                        color: '#fff',
                        width: 4
                    }
                },
                axisLabel: {
                    color: 'black',
                    distance: 36,
                    fontSize: 12
                },
                detail: {
                    valueAnimation: true,
                    formatter: '{value} %',
                    color: 'inherit',
                    fontSize:20
                },
                data: [
                    {
                        value: (tnb_upph / 10.85 * 100).toFixed(2)
                    }
                ]
            }
        ]
    };
    option2.series[0].max = 200;
    option2 && myChart2.setOption(option2);
}

// TNB实时UPPH达成率仪表盘
function yibiaopan_tnb(data) {

    // $('#sub_ew').val() === '' ? sub_qty_hr = data[0].qty_hr : sub_qty_hr = (data[0].qty_hr + parseFloat($('#sub_ew').val())).toFixed(2)
    $('#tnb_ew').val() === '' ? tnb_qty_hr = data.data.qty_hr_tnb : tnb_qty_hr = (data.data.qty_hr_tnb + parseFloat($('#tnb_ew').val())).toFixed(2)

    // $('#sub_ew').val() === '' ? sub_upph = (data[0].product_qty / data[0].qty_hr).toFixed(2) : sub_upph = (data[0].product_qty / sub_qty_hr).toFixed(2)
    $('#tnb_ew').val() === '' ? tnb_upph = (data.data.product_qty_tnb / data.data.qty_hr_tnb).toFixed(2) : tnb_upph = (data.data.product_qty_tnb / tnb_qty_hr).toFixed(2)
    var option2;
    option2 = {
        series: [
            {
                type: 'gauge',
                axisLine: {
                    lineStyle: {
                        width: 25,
                        color: [
                            [0.45, '#fd666d'],
                            // [0.7692, '#37a2da'],
                            [0.5, '#A9F5C5'],
                            // [1.3, '#67e0e3']
                            [1.0, 'green']
                        ]
                    }
                },
                pointer: {
                    itemStyle: {
                        color: 'auto'
                    }
                },
                axisTick: {
                    distance: -25,
                    length: 8,
                    lineStyle: {
                        color: '#fff',
                        width: 2
                    }
                },
                splitLine: {
                    distance: -25,
                    length: 25,
                    lineStyle: {
                        color: '#fff',
                        width: 4
                    }
                },
                axisLabel: {
                    color: 'black',
                    distance: 36,
                    fontSize: 12
                },
                detail: {
                    valueAnimation: true,
                    formatter: '{value} %',
                    color: 'inherit',
                    fontSize:20
                },
                data: [
                    {
                        value: (tnb_upph / 10.85 * 100).toFixed(2)
                    }
                ]
            }
        ]
    };
    option2.series[0].max = 200;
    option2 && myChart2.setOption(option2);
}
// 显示UPPH图表到html页面
function show_upph_to_html(data1) {
    fetch('/other/upph_get', { method: 'get' }).then(res => res.json()).then(data => {
        // 增加当日UPP实时数据
        let shift = ''
        if (new Date().getHours() >= 8 && new Date().getHours() < 20) {
            shift = 'D'
        } else {
            shift = 'N'
        }
        data.u_date.push(new Date().toISOString().split('T')[0].slice(5, 10) + shift)
        data.u_sub.push((data1.data.product_qty_sub / data1.data.qty_hr_sub).toFixed(2))
        data.u_sub_g.push('9.21')
        data.u_tnb_g.push('10.85')
        data.u_tnb.push((data1.data.product_qty_tnb / data1.data.qty_hr_tnb).toFixed(2))
        // 显示函数
        show_upph(data)
    }).catch(error => {
        console.log('Error', error)
    })
}
// 显示UPPH图表函数
function show_upph(data) {
    var option;
    option = {
        title: {
            text: 'SUB&TNB UPPH Tracking',
            left: 'center',
            top: 20,
            textStyle: {
                fontSize: 16,
            }
        },
        tooltip: {},
        legend: {
            data: ['SUB', 'SUB_GOAL', 'TNB', 'TNB_GOAL'],
            top: '5%',
            right: '14%'
        },
        xAxis: {
            type: 'category',
            data: data.u_date
        },
        yAxis: {
            type: 'value',
        },
        series: [
            {
                data: data.u_sub,
                name: 'SUB',
                label: { show: true },
                type: 'line',
                smooth: true
            },
            {
                data: data.u_sub_g,
                name: 'SUB_GOAL',
                show: true,
                endLabel: {
                    show: true,
                },
                type: 'line',
                smooth: true,
                showSymbol: false,
                lineStyle: {
                    width: 2,
                    type: 'dashed'
                }
            },
            {
                data: data.u_tnb,
                name: 'TNB',
                label: { show: true },
                type: 'line',
                smooth: true
            },
            {
                data: data.u_tnb_g,
                name: 'TNB_GOAL',
                endLabel: {
                    show: true,
                },
                type: 'line',
                smooth: true,
                showSymbol: false,
                lineStyle: {
                    width: 2,
                    type: 'dashed'
                }
            },
        ]
    };

    option && myChart.setOption(option);
}