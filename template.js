async function geturlcontent(url) {
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

var bodycontent = geturlcontent("../template.txt").then(
console.log(bodycontent))