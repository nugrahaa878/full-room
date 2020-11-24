/*
    Inspired from: https://github.com/clementmihailescu/Pathfinding-Visualizer
    with modification to simplify it.
*/

function Board(height, width) {
    this.height = height;
    this.width = width;
    this.boardArr = [];
}

Board.prototype.init = function () {
    this.makeGrid();
}

// Create grid with randomize obstacles
Board.prototype.makeGrid = function () {
    let tableHTML = "";

    for (let r = 0; r < this.height; r++) {
        let curRow = [];
        let curHTMLRow = `<tr id="row ${r}">`;
        for (let c = 0; c < this.width; c++) {
            let node = `${r}-${c}`;
            let status = ["normal", "obstacle"].random();
            curRow.push(status);
            curHTMLRow += `<td id="${node}" class="${status}" onclick="toggleBoard('${node}')"></td>`;
        }
        this.boardArr.push(curRow);
        tableHTML += `${curHTMLRow}</tr>`;
    }
    let board = document.getElementById("board");
    board.innerHTML = tableHTML;
}

Array.prototype.random = function () {
    return this[Math.floor((Math.random() * this.length))];
}
