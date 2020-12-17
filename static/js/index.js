let board;

$(document).ready(function () {

    $(".generate-text").hide();
    $(".submit-map").hide();
    $(".description-about").hide();

    $(".button-about").click(function () {
        hideHomePage();
        $(".description-about").show();
    });

    $(".button-start").click(function () {
        hideHomePage();
        showStepOne();
    });

    $(".step-1-back").click(function () {
        hideStepOne();
        showHomePage();
    });

    $(".step-1-next").click(function () {
        hideStepOne();
        showStepTwo();
    });

    $(".step-2-back").click(function () {
        hideStepTwo();
        showStepOne();
    });

    $(".btn-edit-size").click(function () {
        hideBoard();
        showStepOne();
    })

    $(".step-2-next").click(function () {
        validate();
    });

    $(".board-random").click(function () {
        board.makeGrid();
    });

});

function hideStepOne() {
    $(".panah-1").hide();
    $(".step1-text").hide();
    $(".step1-desc").hide();
    $(".form-1").hide();
    $(".nav-step-1").hide();
}

function showStepOne() {
    $(".panah-1").show();
    $(".step1-text").show();
    $(".step1-desc").show();
    $(".form-1").show();
    $(".nav-step-1").show();
}

function hideStepTwo() {
    $(".panah-2").hide();
    $(".step2-text").hide();
    $(".step2-desc").hide();
    $(".form-2").hide();
    $(".nav-step-2").hide();
}

function showBoard() {
    $(".generate-text").show();
    $(".submit-map").show();
    $(".board-submit").show();
    $("#board").show();
    $(".btn-edit-size").show();
}

function hideBoard() {
    $(".generate-text").hide();
    $(".submit-map").hide();
    $(".board-submit").hide();
    $(".btn-edit-size").hide();
    $("#board").hide();
    $(".btn-edit-size").hide();
}

function showStepTwo() {
    $(".panah-2").show();
    $(".step2-text").show();
    $(".step2-desc").show();
    $(".form-2").show();
    $(".nav-step-2").show();
}

function hideHomePage() {
    $(".description-text").hide();
    $(".my-button").hide();
}

function showHomePage() {
    $(".description-text").show();
    $(".my-button").show();
}

function validate() {
    if ($("#id_length").val() != "" &&
        $("#id_width").val() != "" &&
        $("#id_healthy").val() != "" &&
        $("#id_sick").val() != "") {
        hideStepTwo();
        createBoard();
        showBoard();
    }
    else {
        alert("Pastikan semua data terisi terlebih dahulu.");
    }
}

function createBoard() {
    let height = $("#id_length").val();
    let width = $("#id_width").val();
    board = new Board(height, width);
    board.init();
}

function toggleBoard(position) {
    let element = $("#" + `${position} > img`);
    let coordinates = position.split("-");
    let r = parseInt(coordinates[0]);
    let c = parseInt(coordinates[1]);

    if (element.attr("src") == `${IMG_BARRIER}`) {
        element.attr("src", IMG_METAL);
        board.boardArr[0][r][c] = "_";
    }
    else {
        element.attr("src", IMG_BARRIER);
        board.boardArr[0][r][c] = "#";
    }
    console.log(board.boardArr);
    $("#boardMap").val(board.boardArr);
}