const gel = (element) => document.querySelector(element);

const ball = gel('.ball');
const container = gel('.container');

const convert = (text) => +text.split('px').join('');

const screenWidth = document.body.offsetWidth;
const screenHeight = convert(getComputedStyle(container).height);
const ballWidth = convert(getComputedStyle(ball).width);

let positionX = 0;
let speedX = 10;

let positionY = 0;
let speedY = 8;

setInterval(() => {
  positionX += speedX;
  positionY += speedY;

  if (
    positionX >= screenWidth - ballWidth
    || positionX <= 0
  ) {
    speedX *= -1;
  }
  
  if (
    positionY >= screenHeight - ballWidth
    || positionY <= 0
  ) {
    speedY *= -1;
  }

  ball.style.left = `${positionX}px`;
  ball.style.top = `${positionY}px`;
}, 1);

