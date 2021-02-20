// FUNCTION 1 - IMAGE LOADER
function initStimulus(image_srcs, qCount, startQuestion, mTFS, tSEDK, tQEDK, tLEDK) {
  var _i, _len;
  var images = [];
  var loadedImages = 0;
  for (_i = 0, _len = image_srcs.length; _i < _len; _i++) {
    images.push(new Image);
    images[images.length - 1].src = image_srcs[_i];
    images[images.length - 1].onload = function() {
      loadedImages++;
      if (loadedImages == images.length) return startStimulus(images, qCount, startQuestion, mTFS, tSEDK, tQEDK, tLEDK);
    };
  }
  return images;
};

// FUNCTION 2 - IMAGES LOADED, INIT PROCESS
function startStimulus(imgs, qCount, startQuestion, maxTimeFullStimulus, timingStimulusEmbeddedDataKey, timingQuestionEmbeddedDataKey, timingLoadingEmbeddedDataKey) {
  var startStimulus;
  var timerFullStimulus;
  var endLoading;
  var stimulus = jQuery("img");
  var progBar = jQuery("#progBar");
  progBar.css("width", "0%");
  var showStimulus = jQuery("#showStimulus");
  showStimulus.on("click", function(event, element) {
    jQuery("#showContainer").hide();
    //Timer and Stimuli Control 
    var i = 0;
    stimulus.attr("src", imgs[0].src)
    stimulus.show();
    startStimulus = Date.now();
    
    timerFullStimulus = setInterval(function() {
      progBar.css("width", (100 / maxTimeFullStimulus * i).toString()+"%");
      if (i === maxTimeFullStimulus) {
          clearInterval(timerFullStimulus);
          stimulus.attr("src", imgs[1].src);
      }
      i++;
    }, 100);
  });
  // Stimulus Click: Prevent Touch
  stimulus.on("touchstart", function(event, element){
    event.preventDefault();
    alert("Please do not use the touch input of your device!")
  });
  // Stimulus Click: Save Answer
  stimulus.on("click", function(event, element) {
    //Clear Timer
    clearInterval(timerFullStimulus);
    //Get and Save Timing
    var endStimulus = Date.now();
    Qualtrics.SurveyEngine.setEmbeddedData(timingQuestionEmbeddedDataKey, startStimulus-startQuestion);
    Qualtrics.SurveyEngine.setEmbeddedData(timingLoadingEmbeddedDataKey, endLoading-startQuestion);
    Qualtrics.SurveyEngine.setEmbeddedData(timingStimulusEmbeddedDataKey, endStimulus-startStimulus);
    Qualtrics.SurveyEngine.setEmbeddedData("question_count", qCount);
    //Advance Page
    $("NextButton").click();
  });
  endLoading = Date.now();
  showStimulus.css("background-color", "#007ac0");
  showStimulus.prop("disabled", false);
}

Qualtrics.SurveyEngine.addOnload(function()
{
  /*Place your JavaScript here to run when the page loads*/
  this.hideNextButton();
  jQuery("img").hide();
});

Qualtrics.SurveyEngine.addOnReady(function()
{
  /*Place your JavaScript here to run when the page is fully displayed*/
  {*stimulusWidth*}
  var imageSrcs = [
    "{*baseUrl*}{*storageUrl*}{*stimulusBaseName*}.png",
    "{*baseUrl*}{*storageUrl*}{*stimulusBaseNamePlus*}_plus.png"
  ];
  var qCount = parseInt("${e://Field/question_count}");
  qCount++;
  jQuery("#questionCount").html(qCount);
  jQuery("#showContainer").height(jQuery("#showContainer").width() * {*stimulusH*} / {*stimulusW*});
  jQuery("#showStimulus").prop("disabled", true);
  initStimulus(imageSrcs, qCount, Date.now(), {*timingStimulus*}, "timing_stimulus_{*stimulusId*}", "timing_question_{*stimulusId*}", "timing_loading_{*stimulusId*}");
});

Qualtrics.SurveyEngine.addOnUnload(function()
{
  /*Place your JavaScript here to run when the page is unloaded*/

});