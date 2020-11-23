$(document).ready(function () {

    $(".button-start").click(function () {
        hideHomePage();
        showStepOne();
    });

});

function hideStepOne() {
    $(".panah-1").hide();
    $(".step1-text").hide();
    $(".step1-desc").hide();
    $(".form-1").hide();
}

function showStepOne() {
    $(".panah-1").show();
    $(".step1-text").show();
    $(".step1-desc").show();
    $(".form-1").show();
}

function hideStepTwo() {
    $(".panah-2").hide();
    $(".step2-text").hide();
    $(".step2-desc").hide();
    $(".form-2").hide();
}

function hideHomePage() {
    $(".description-text").hide();
    $(".my-button").hide();

}