var isValid = function(s) {  
    let stack = []
    let open = ['(', '[', '{']
    let pairs = {'(': ')', '[': ']', '{': '}'}
    for(let i = 0; i < s.length; i++){
        if(open.includes(s[i])) {
            stack.push(s[i])
        } else if(pairs[stack.pop()] !== s[i]) {
            return false
        }
    }
    if(stack.length === 0){
        return true
    }
    return false
};