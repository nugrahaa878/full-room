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

Board.prototype.makeGrid = function () {
    let tableHTML = "";
    for (let r = 0; r < this.height; r++) {
        let curRow = [];
        let curHTMLRow = `<tr id="row ${r}">`;
        for (let c = 0; c < this.width; c++) {
            let node = `${r}-${c}`;
            curRow.push(node);
            curHTMLRow += `<td id="${node}"></td>`;
        }
        this.boardArr.push(curRow);
        tableHTML += `${curHTMLRow}</tr>`;
    }
    let board = document.getElementById("board");
    board.innerHTML = tableHTML;
}