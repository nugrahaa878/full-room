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

    $(".step-2-next").click(function () {
        validate();
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
    $("#board").show();
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
    console.log($("#board-height").val())
    if ($("#board-height").val() != "" &&
        $("#board-width").val() != "" &&
        $("#board-normal").val() != "" &&
        $("#board-big").val() != "") {
        hideStepTwo();
        showBoard();
    }
    else {
        alert("Pastikan semua data terisi terlebih dahulu.");
    }
}