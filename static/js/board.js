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
    var myArray = [];

    for (let r = 0; r < this.height; r++) {
        let curRow = [];
        let curHTMLRow = `<tr id="row ${r}">`;
        for (let c = 0; c < this.width; c++) {
            let node = `${r}-${c}`;
            let status = ["normal", "obstacle"].random();
            let img_src = (status == "normal") ? IMG_METAL : IMG_BARRIER;

            curRow.push(status);
            curHTMLRow += `<td id="${node}" onclick="toggleBoard('${node}')"><img src="${img_src}" class="metal" alt="Responsive Image"/></td>`;
        }
        myArray.push(toArray(curRow));
        tableHTML += `${curHTMLRow}</tr>`;
    }
    this.boardArr.push(myArray);
    $("#boardMap").val(this.boardArr);
    let board = document.getElementById("board");
    board.innerHTML = tableHTML;
    return myArray;
}

Array.prototype.random = function () {
    return this[Math.floor((Math.random() * this.length))];
}

function toArray(mArray) {
    var newArr = [];
    mArray.forEach(element => {
        if (element == "normal") {
            newArr.push("_");
        } else {
            newArr.push("#");
        }
    });
    return newArr
}
