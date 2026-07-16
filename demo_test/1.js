export function ev(event) {
    const file = event.target.files[0]; // 获取选中的文件
    console.log(file)
    if (file) {
        const reader = new FileReader(); // 创建FileReader实例
        reader.onload = function (e) { // 设置读取完成后的回调函数
            const base64String = e.target.result; // 获取Base64编码的字符串
            document.getElementById('outputImage').src = base64String; // 显示图片
            console.log(base64String); // 在控制台输出Base64字符串，或者你可以在这里做其他处理
        };
        reader.readAsDataURL(file); // 读取文件内容为DataURL，即Base64编码的字符串
    }
}