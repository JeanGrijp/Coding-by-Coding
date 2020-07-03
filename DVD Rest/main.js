const {floor, random} = Math
const valorRandom = (from, to) => {
  return floor(random() * (to - from + 1) + 1)
}
const gel = (element) => document.querySelector(element);
const ball = gel('.ball');
const container = gel('.container');
const convert = (text) => +text.split('px').join('');
const screenWidth = document.body.offsetWidth;
const screenHeight = convert(getComputedStyle(container).height);
const ballWidth = convert(getComputedStyle(ball).width);
let positionX = 0;
let speedX = 1;
let positionY = 0;
let speedY = 1;

setInterval(() => {
  positionX += speedX;
  positionY += speedY;

  if (
    positionX >= screenWidth - ballWidth
    || positionX <= 0
  ) {
    speedX *= -1;
    ball.style.backgroundColor = 'rgb('+`${valorRandom(0, 255)}`+","+ `${valorRandom(0, 255)}`+","+ `${valorRandom(0, 255)})`
  }
  
  if (
    positionY >= screenHeight - ballWidth
    || positionY <= 0
  ) {
    speedY *= -1;
    ball.style.backgroundColor = 'rgb('+`${valorRandom(0, 255)}`+","+ `${valorRandom(0, 255)}`+","+ `${valorRandom(0, 255)})`
  }

  ball.style.left = `${positionX}px`;
  ball.style.top = `${positionY}px`;
}, 1);

