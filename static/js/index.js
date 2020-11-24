let board;

$(document).ready(function () {

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
    $(".board-button-container").show();
    $("#board").show();
    $(".btn-edit-size").show();
}

function hideBoard() {
    $(".board-button-container").hide();
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
    if ($("#board-height").val() != "" &&
        $("#board-width").val() != "" &&
        $("#board-normal").val() != "" &&
        $("#board-big").val() != "") {
        hideStepTwo();
        createBoard();
        showBoard();
    }
    else {
        alert("Pastikan semua data terisi terlebih dahulu.");
    }
}

function createBoard() {
    let height = $("#board-height").val();
    let width = $("#board-width").val();
    board = new Board(height, width);
    board.init();
}

function toggleBoard(position) {
    let element = $("#" + `${position}`);
    let coordinates = position.split("-");
    let r = parseInt(coordinates[0]);
    let c = parseInt(coordinates[1]);

    if (element.hasClass("normal")) {
        element.removeClass("normal");
        element.addClass("obstacle");
        board.boardArr[r][c] = "obstacle";
    }
    else {
        element.removeClass("obstacle");
        element.addClass("normal");
        board.boardArr[r][c] = "normal";
    }
}