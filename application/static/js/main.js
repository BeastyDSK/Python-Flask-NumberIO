function checker(type) {
    var p = document.querySelector(".res" + type);
    p.style.visibility = "hidden";
   
    fetch(`/check/${type}/${document.querySelector(".in" + type).value}`).then(data => {
        return data.json();
    }).then(res => {
        p.textContent = res.res;
        p.style.visibility = "visible";
    }).catch(err => {
        console.error(err);
    });
}