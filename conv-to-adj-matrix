const test = "0 1 2 3 4\n1 2 3\n2 0 1 4\n3 4\n4 1 2"

const convMatrix = (textIn) => {
    const tSplit = textIn.split('\n')
    const length = tSplit.length
    const adjMat = adjMatInit(length)
    
    tSplit.forEach((x, i) => {
        x.split(' ').forEach((node, j) => {
            if(j !== 0) {
                adjMat[i][parseInt(node)] = 1
            }
        })
    })
    
    return matToString(adjMat)
}

const adjMatInit  = (dim) => {
    return Array.apply(null, Array(dim)).map(function (x, i) { return Array.apply(null, Array(dim)).map(function (x, i) { return 0; }); })
}

const matToString = (mat) => {
    let str = ''
    const length = mat.length
    
    mat.forEach((x, i) => {
        x.forEach((y, j) => {
            str = str + y + ' '
        })
        if(length - 1 !== i) {
            str = str + '\n'
        }
    })
    
    return str
}

console.log(convMatrix(test))
