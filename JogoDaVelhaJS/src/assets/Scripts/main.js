import {verificaVitoria} from "./functions"

const game = [
  ['o', 'x', 'o'],
  ['x', 'o', 'o'],
  ['o', 'o', 'x'],
];

console.log(verificaVitoria(game))