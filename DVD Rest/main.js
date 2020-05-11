const gel = (element) => document.querySelector(element)
const ball = gel(".ball")
const container = gel(".container")

const max = +getComputedStyle(container).width.split("px").join("")

let speedY = 80
let speedX = 90
setInterval(()=>{
    let positionX = getComputedStyle(ball).left.split("px").join("")
    if (positionX > max
        || positionX < 0) {
        speedX *= -1
    }
    let aux = +ball.style.left.split("px").join("")
    ball.style.left = `${aux+speedX}px`

    
}, 100)