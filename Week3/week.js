fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
.then(response=>{
    return response.json();  //取得 JSON 再轉 JavaScript
}).then(data=>{
    let arr= data['result']['results'];
    // console.log(arr);
    let tittleArr=[]; //標題arr
    let urlArr=[];  //圖片網址arr
    for(let i=0;i<arr.length;i++){
        tittleArr.push(arr[i]['stitle']);
        let url = arr[i]['file'].split('http')[1];
        urlArr.push('http'+url)
    };
    console.log(tittleArr);
    console.log(urlArr);
    let img = document.createElement("img");
    img.src=urlArr[0]
    document.getElementById('title1').appendChild(img)
    // return [tittleArr,urlArr]
})
// .then(newElement=>{
//     console.log(newElement);
//     console.log(newElement[0][0]);
//     console.log(newElement[1][0]);
//     let img = document.createElement("img");
//     img.src=newElement[1][0]
//     document.getElementById('title1').appendChild(img)
// })
// let arr2=[1,2,3,4]  //這行不加的話，14、15log出來的array就會有兩個
// console.log(arr);   