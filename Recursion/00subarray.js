const arr = [1,2,3]
const n = arr.length
var res = []

for (let i = 0; i < n; i++){
    for (let j = i+1; j < n+1; j++){
        let temp = arr.slice(i,j)
        res.push(temp)
    }
}

console.log(res)