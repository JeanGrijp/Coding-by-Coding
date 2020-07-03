const game = [
    ['o', 'x', 'o'],
    ['x', 'o', 'o'],
    ['o', 'o', 'x'],
  ];
  
  

const verificaVitoria = (game) => {
  let playRows = [];
  let playColumns = [];
  for (let i = 0; i < 3; i += 1) {
    for (let j = 0; j < 3; j += 1) {
      playRows.push(game[i][j]);
      playColumns.push(game[j][i]);
    }
    const [r1, r2, r3] = playRows;
    const [c1, c2, c3] = playColumns;
  
    if (
      (r1 === r2 && r1 === r3)
      ||
      (c1 === c2 && c2 === c3)
      ) {
          console.log("chegou")
        return true;
      }
  
    playRows = [];
    playColumns = [];
  }
  if (
    (game[0][0] === game[1][1] && game[1][1] === game[2][2]) 
    ||
    (game[2][0] === game[1][1] && game[1][1] === game[0][2])
    ){
        console.log("chegou")
    return true
  }
}

verificaVitoria(game)
