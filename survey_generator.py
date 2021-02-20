# -*- coding: utf-8 -*-entsprechenden 
import json
import copy
import sys

dataList = ['europe', 'usa', 'world']
taskList = [1, 2, 3, 4]
repetitionList = [1, 2]
geometryList = ['2d_line', '3d_band', '3d_tube']

currentFlowId = 1

# DATA ===

taskQuestions = {
  "europe":{
    "task1": "Which of the three countries has the <b>largest number of connected flows</b>. Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task2": "Which of the three countries has <b>several small flows</b> and <b>a single significantly larger flow</b>? Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task3": "Which flow between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span> and the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span> has the <b>largest magnitude</b>. Click on the correct <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green node</span>.",
    "task4": "Which flow has the <b>larger magnitude</b>: the one between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue nodes</span> or the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span>? Click on one of the two correct nodes."
  },
  "usa":{
    "task1": "Which of the three states has the <b>largest number of connected flows</b>. Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task2": "Which of the three states has <b>several small flows</b> and <b>a single significantly larger flow</b>? Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task3": "Which flow between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span> and the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span> has the <b>largest magnitude</b>. Click on the correct <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green node</span>.",
    "task4": "Which flow has the <b>larger magnitude</b>: the one between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue nodes</span> or the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span>? Click on one of the two correct nodes."
  },
  "world":{
    "task1": "Which of the three countries has the <b>largest number connected of flows</b>. Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task2": "Which of the three countries has <b>several small flows</b> and <b>a single significantly larger flow</b>? Click on the correct <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span>.",
    "task3": "Which flow between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue node</span> and the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span> has the <b>largest magnitude</b>. Click on the correct <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green node</span>.",
    "task4": "Which flow has the <b>larger magnitude</b>: the one between the <span class=\"blue-node\" style=\"font-family: sans-serif; color: rgb(132, 197, 243); -webkit-text-stroke: 1px rgb(0, 141, 242);\">blue nodes</span> or the <span class=\"green-node\" style=\"font-family: sans-serif; color: rgb(171, 254, 141); -webkit-text-stroke: 1px rgb(56, 191, 0);\">green nodes</span>? Click on one of the two correct nodes."
  }
}

# ========

# Regions
worldYDelta = -19
regionsInfo = {
  "europe": {
    "NO": {"h": 70, "w": 70, "x": 637, "y": 100},
    "SE": {"h": 70, "w": 70, "x": 792, "y": 111},
    "DK": {"h": 70, "w": 70, "x": 654, "y": 262},
    "CH": {"h": 70, "w": 70, "x": 556, "y": 570},
    "ES": {"h": 70, "w": 70, "x": 267, "y": 779},
    "NL": {"h": 70, "w": 70, "x": 496, "y": 374},
    "AT": {"h": 70, "w": 70, "x": 745, "y": 554},
    "BE": {"h": 70, "w": 70, "x": 468, "y": 438},
    "FR": {"h": 70, "w": 70, "x": 414, "y": 534},
    "IT": {"h": 70, "w": 70, "x": 704, "y": 747},
    "DE": {"h": 70, "w": 70, "x": 647, "y": 396},
    "GB": {"h": 70, "w": 70, "x": 337, "y": 392},
    "HR": {"h": 70, "w": 70, "x": 784, "y": 619},
    "TR": {"h": 70, "w": 70, "x": 1120, "y": 853}
  },
  "usa": {
    "IL": {"h": 70, "w": 70, "x": 1071, "y": 334},
    "OH": {"h": 70, "w": 70, "x": 1230, "y": 383},
    "PA": {"h": 70, "w": 70, "x": 1375, "y": 361},
    "CA": {"h": 70, "w": 70, "x": 175, "y": 548},
    "TX": {"h": 70, "w": 70, "x": 749, "y": 697},
    "NY": {"h": 70, "w": 70, "x": 1442, "y": 280},
    "MI": {"h": 70, "w": 70, "x": 1177, "y": 266},
    "MO": {"h": 70, "w": 70, "x": 949, "y": 455},
    "NC": {"h": 70, "w": 70, "x": 1329, "y": 558},
    "WDC": {"h": 70, "w": 70, "x": 1404, "y": 430},
    "FL": {"h": 70, "w": 70, "x": 1255, "y": 802},
    "AL": {"h": 70, "w": 70, "x": 1113, "y": 655},
    "SC": {"h": 70, "w": 70, "x": 1286, "y": 616},
    "GA": {"h": 70, "w": 70, "x": 1211, "y": 660},
    "TN": {"h": 70, "w": 70, "x": 1128, "y": 549},
    "MN": {"h": 70, "w": 70, "x": 896, "y": 141},
    "WI": {"h": 70, "w": 70, "x": 1021, "y": 212},
    "IN": {"h": 70, "w": 70, "x": 1129, "y": 397}
  },
  "world": {
    "PE": {"h": 80, "w": 54, "x": 170, "y": 498 + worldYDelta},
    "BR": {"h": 80, "w": 54, "x": 281, "y": 527 + worldYDelta},
    "AR": {"h": 80, "w": 54, "x": 263, "y": 661 + worldYDelta},
    "CA": {"h": 80, "w": 54, "x": 190, "y": 135 + worldYDelta},
    "GB": {"h": 80, "w": 54, "x": 508, "y": 144 + worldYDelta},
    "AU": {"h": 80, "w": 54, "x": 1109, "y": 589 + worldYDelta},
    "CN": {"h": 80, "w": 54, "x": 949, "y": 243 + worldYDelta},
    "AE": {"h": 80, "w": 54, "x": 759, "y": 311 + worldYDelta},
    "BD": {"h": 80, "w": 54, "x": 921, "y": 309 + worldYDelta},
    "GE": {"h": 80, "w": 54, "x": 688, "y": 209 + worldYDelta},
    "KZ": {"h": 80, "w": 54, "x": 764, "y": 180 + worldYDelta},
    "KG": {"h": 80, "w": 54, "x": 813, "y": 214 + worldYDelta},
    "MY": {"h": 80, "w": 54, "x": 997, "y": 421 + worldYDelta},
    "ID": {"h": 80, "w": 54, "x": 1053, "y": 449 + worldYDelta},
    "SA": {"h": 80, "w": 54, "x": 720, "y": 308 + worldYDelta},
    "PH": {"h": 80, "w": 54, "x": 1081, "y": 371 + worldYDelta},
    "US": {"h": 80, "w": 54, "x": 130, "y": 236 + worldYDelta},
    "IN": {"h": 80, "w": 54, "x": 875, "y": 327 + worldYDelta},
    "RU": {"h": 80, "w": 54, "x": 829, "y": 116 + worldYDelta}
  } #,
  # "world": {
  #   "PE": {"h": 90, "w": 70, "x": 170, "y": 498},
  #   "BR": {"h": 90, "w": 70, "x": 281, "y": 527},
  #   "AR": {"h": 90, "w": 70, "x": 263, "y": 661},
  #   "CA": {"h": 90, "w": 70, "x": 190, "y": 135},
  #   "GB": {"h": 90, "w": 70, "x": 508, "y": 144},
  #   "AU": {"h": 90, "w": 70, "x": 1109, "y": 589},
  #   "CN": {"h": 90, "w": 70, "x": 949, "y": 243},
  #   "AE": {"h": 90, "w": 70, "x": 759, "y": 311},
  #   "BD": {"h": 90, "w": 70, "x": 921, "y": 309},
  #   "GE": {"h": 90, "w": 70, "x": 688, "y": 209},
  #   "KZ": {"h": 90, "w": 70, "x": 764, "y": 180},
  #   "UZ": {"h": 90, "w": 70, "x": 773, "y": 214},
  #   "MY": {"h": 90, "w": 70, "x": 997, "y": 421},
  #   "ID": {"h": 90, "w": 70, "x": 1053, "y": 449},
  #   "SA": {"h": 90, "w": 70, "x": 720, "y": 308},
  #   "PH": {"h": 90, "w": 70, "x": 1081, "y": 371},
  #   "US": {"h": 90, "w": 70, "x": 130, "y": 236},
  #   "IN": {"h": 90, "w": 70, "x": 875, "y": 327}
  # }
}

worldExceptions = {
  "map11": {
    "BR": {
      "dh": 0,
      "dw": 0,
      "dx": -5,
      "dy": 0
    },
    "AR": {
      "dh": 0,
      "dw": 0,
      "dx": +5,
      "dy": -3
    }
  },
  "map12": {
    "AU": {
      "dh": -10,
      "dw": 16,
      "dx": 10,
      "dy": 7
    }
  },
  "map21": {
    "AU": {
      "dh": -10,
      "dw": 16,
      "dx": 10,
      "dy": 7
    },
    "CN": {
      "dh": -2,
      "dw": 6,
      "dx": 8,
      "dy": 2
    },
    "MY": {
      "dh": -2,
      "dw": 6,
      "dx": 8,
      "dy": 2
    }
  },
  "map32": {
    "KZ": {
      "dh": 0,
      "dw": 0,
      "dx": -7,
      "dy": 0
    }
  }
}

regionsByStimuli = {
  "europe": {
    "map11": ["NO", "SE", "DK"],
    "map12": ["SE", "CH", "ES"],
    "map21": ["NL", "AT", "NO"],
    "map22": ["SE", "BE", "CH"],
    "map31": ["FR", "AT", "IT"],
    "map32": ["DE", "NL", "IT"],
    "map41": ["GB", "ES", "DE", "HR"],
    "map42": ["BE", "DE", "IT", "TR"]
  },
  "usa": {
    "map11": ["IL", "OH", "PA"],
    "map12": ["CA", "TX", "NY"],
    "map21": ["MI", "MO", "TN"],
    "map22": ["NC", "WDC", "IN"],
    "map31": ["FL", "AL", "SC"],
    "map32": ["GA", "TN", "IL"],
    "map41": ["MN", "WI", "PA", "TN"],
    "map42": ["IL", "GA", "CA", "PA"]
  },
  "world": {
    "map11": ["PE", "BR", "AR"],
    "map12": ["CA", "GB", "AU"],
    "map21": ["AU", "CN", "MY"],
    "map22": ["CA", "PE", "RU"],
    "map31": ["AU", "AE", "BD"],
    "map32": ["GE", "KZ", "KG"],
    "map41": ["BD", "MY", "ID", "SA"],
    "map42": ["AE", "PH", "US", "IN"]
  }
}

stimulusWH = {
  "europe": {"w": 1158, "h": 1040},
  "usa": {"w": 1700, "h": 930},
  "world": {"w": 1250, "h": 890}
}

stimulusDummyGraphicId = {
  "europe": {
    "2d_line": "IM_eV94SMmrJ5KgcCh",
    "3d_band": "IM_erGzTPGpy1Jdr13",
    "3d_tube": "IM_erGzTPGpy1Jdr13"
  },
  "usa": {
    "2d_line": "IM_e9EDDsme8ldNxs1",
    "3d_band": "IM_26usON5pDYuOyCF",
    "3d_tube": "IM_26usON5pDYuOyCF"
  },
  "world": {
    "2d_line": "IM_4OUIRUnTIK2SrOZ",
    "3d_band": "IM_3F1mOp2GvL4HnjT",
    "3d_tube": "IM_3F1mOp2GvL4HnjT"
  }
}

def getQuestionJS(stimulusId, stimulusBaseName, data, task):
  stimulusH = stimulusWH[data]["h"]
  stimulusW = stimulusWH[data]["w"]
  stimulusBaseNamePlus = "_".join(stimulusBaseName.split("_")[:-1])
  #baseUrl = "https://monash.az1.qualtrics.com/CP/Graphic.php?urlimage=true&IM="
  baseUrl = "https://cityunilondon.eu.qualtrics.com/ControlPanel/Graphic.php?urlimage=true&IM="
  storageUrl = "http://vu2044.serv01.menkisys.de/3dflowmaps/output_web/stimuli/"
  timingStimulus = 60
  newline = '\n'  # Avoids SyntaxError: f-string expr cannot include a backslash
  if data == "world":
    stimulusWidth = "jQuery(\".SkinInner\").css(\"width\", \"1024px\");"
  elif data == "usa":
    stimulusWidth = "jQuery(\".SkinInner\").css(\"width\", \"960px\");"
  else:
    stimulusWidth = "jQuery(\".SkinInner\").css(\"width\", \"770px\");"
  with open('stimulus_template.js', 'r') as file:
    jsCode = f"{file.read().replace('{', '{{').replace('}', '}}').replace('{*', '').replace('*}', '')}".format(**locals())
  # jsCode = f"// FUNCTION 1 - IMAGE LOADER\nfunction initStimulus(image_srcs, qHtml, mTQ, mTFS, tEDK) {{\n  var _i, _len;\n  var images = [];\n  var loadedImages = 0;\n  for (_i = 0, _len = image_srcs.length; _i < _len; _i++) {{\n    images.push(new Image);\n    images[images.length - 1].src = image_srcs[_i];\n    images[images.length - 1].onload = function() {{\n      loadedImages++;\n      if (loadedImages == images.length) return startStimulus(images, qHtml, mTQ, mTFS, tEDK);\n    }};\n  }}\n  return images;\n}};\n\n// FUNCTION 2 - IMAGES LOADED, INIT PROCESS\nfunction startStimulus(imgs, qHtml, maxTimeQuestion, maxTimeFullStimulus, timingEmbeddedDataKey) {{\n  var start;\n  var stimulus = jQuery(\"img\")\n  jQuery(\"#3DFMLoading\").hide();\n  jQuery(\"#3DFMQuestion\").html(qHtml);\n  var progBar = jQuery(\"#progBar\");\n  progBar.css(\"width\", \"0%\");\n  \n  //Timer and Stimuli Control\n  var i = 0;\n  var timerFullStimulus;\n  var timerQuestion = setInterval(function() {{\n    progBar.css(\"width\", (100 / maxTimeQuestion * i).toString()+\"%\");\n    if (i === maxTimeQuestion) {{\n      clearInterval(timerQuestion);\n      stimulus.attr('src', imgs[0].src)\n    stimulus.show();\n      start = Date.now();\n      var j = 0;\n      timerFullStimulus = setInterval(function() {{\n        progBar.css(\"width\", (100 / maxTimeFullStimulus * j).toString()+\"%\");\n        if (j === maxTimeFullStimulus) {{\n          clearInterval(timerFullStimulus);\n          stimulus.attr(\"src\", imgs[1].src);\n        }}\n        j++;\n      }}, 100);\n    }}\n    i++;\n  }}, 100);\n  \n  // Stimulus Click\n  stimulus.on(\"touchstart\", function(event, element){{\n\tevent.preventDefault();\n\talert(\"Please do not use the touch input of your device!\")\n\t}});\n  stimulus.on(\"click\", function(event, element) {{\n    //Get and Save Timing\n    var end = Date.now();\n    Qualtrics.SurveyEngine.setEmbeddedData(timingEmbeddedDataKey, end-start);\n    //Clear Timers\n    clearInterval(timerQuestion);\n    clearInterval(timerFullStimulus);\n    //Advance Page\n    $('NextButton').click();\n  }});\n}}\nQualtrics.SurveyEngine.addOnload(function()\n{{\n\t/*Place your JavaScript here to run when the page loads*/\n\tthis.hideNextButton();\n\tjQuery(\"img\").hide();\n\n}});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\t var imageSrcs = [\n    \t\"https://monash.az1.qualtrics.com/CP/Graphic.php?urlimage=true&IM=http://vu2044.serv01.menkisys.de/3dflowmaps/output_web/stimuli/{stimulusBaseName}.png\",\n    \t\"https://monash.az1.qualtrics.com/CP/Graphic.php?urlimage=true&IM=http://vu2044.serv01.menkisys.de/3dflowmaps/output_web/stimuli/{stimulusBaseNamePlus}_plus.png\"\n  \t];\n  \tvar qHtml = '<div style=\"width:100%; background-color:#ccc;\"><div id=\"progBar\" style=\"height:10px;width:0%; background-color:#999\"></div></div><br>{questionText}';\n\tinitStimulus(imageSrcs, qHtml, {timingQuestion}, {timingStimulus}, \"timing_{stimulusId}\");\n}});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n}});"
  return jsCode

def getQuestionText(data, task):
  questionText = taskQuestions[data][f"task{task}"]
  questionHtml = f"Question <span id=\"questionCount\">n</span> of 72"
  questionHtml += "<div style=\"width:100%;background-color:#ccc;\"><div id=\"progBar\" style=\"height:10px;width:0%;background-color:#999;\"></div></div><br>"
  questionHtml += f"{questionText}<br><br>"
  questionHtml += f"<div id=\"showContainer\" style=\"width:100%;height:300px;background-color:#E5E5E5;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;\"><b>Read the question above.<br>To show the map click on the blue square.</b><br><button id=\"showStimulus\" style=\"width:20px;height:20px;cursor:crosshair;background-color:#cccccc;border:none\"></button><br>If you need a break, you can do this now before you continue.<br>Please stay on this page and in front of your computer.</div>"
  return questionHtml

def generateRegionShape(x,y, h, w):
  shape = []
  shape.append({"X": x - w/2, "Y": y - h/2})
  shape.append({"X": x + w/2, "Y": y - h/2})
  shape.append({"X": x + w/2, "Y": y + h/2})
  shape.append({"X": x - w/2, "Y": y + h/2})
  return [shape]

def getRegions(data, task, repetition):
  regions = []
  for r in regionsByStimuli[data][f"map{task}{repetition}"]:
    reg = regionsInfo[data][r]
    m = f"map{task}{repetition}"
    if data == "world" and m in worldExceptions and r in worldExceptions[m]:
      dH = worldExceptions[m][r]["dh"]
      dW = worldExceptions[m][r]["dw"]
      dX = worldExceptions[m][r]["dx"]
      dY = worldExceptions[m][r]["dy"]
      # print(data, m, r, dH, dW, dX, dY)
    else:
      dH = 0
      dW = 0
      dX = 0
      dY = 0
    regions.append({
      "Description": r,
      "Shapes": generateRegionShape(reg["x"]+dX, reg["y"]+dY, reg["h"]+dH, reg["w"]+dW),
      "Type": "Polygon",
      "Height": reg["h"]+dH,
      "Width": reg["w"]+dW,
      "X": (reg["x"]+dX) - ((reg["w"]+dW)/2),
      "Y": (reg["y"]+dY) - ((reg["h"]+dH)/2)
    })

  return regions

def generateHeatMapQuestions(surveyData, currentQid):
  heatmaps = []
  for r in repetitionList:
    for t in taskList:
      for d in dataList:
        for g in geometryList:
          currentQid += 1
          stimulusId = f"{d}_map{t}{r}_{g}"
          stimulusBaseName = f"{d}_map{t}{r}{'a' if t < 4 else ''}_{g}"
          heatmaps.append(generateHeatMapQuestion(surveyData["SurveyEntry"]["SurveyID"], currentQid, stimulusId, stimulusBaseName, t, r, d, g))
  return heatmaps

def generateHeatMapQuestion(surveyId, currentQid, stimulusId, stimulusBaseName, task, repetition, data, geometry):
  heatmap = {}
  heatmap["SurveyID"] = surveyId
  heatmap["Element"] = "SQ"
  heatmap["PrimaryAttribute"] = f"QID{currentQid}"
  heatmap["SecondaryAttribute"] = stimulusId
  heatmap["TertiaryAttribute"] = None

  payload = {}
  payload["QuestionText"] = f"<div id=\"3DFMQuestion\">{getQuestionText(data, task)}</div>"
  payload["QuestionJS"] = getQuestionJS(stimulusId, stimulusBaseName, data, task)
  payload["DefaultChoices"] = False
  payload["DataExportTag"] = f"QID{currentQid}"
  payload["QuestionID"] = f"QID{currentQid}"
  payload["QuestionType"] = "HeatMap"
  payload["Selector"] = "Image"
  payload["DataVisibility"] = {"Private": False, "Hidden": False}
  payload["Configuration"] = {"QuestionDescriptionOption": "SpecifyLabel"}
  payload["QuestionDescription"] = stimulusId
  payload["Choices"] = {"1": {"Display": "X,Y"}}
  payload["Validation"] = {"Settings": {"ForceResponse": "OFF", "Type": "None"}}
  payload["GradingData"] = []
  payload["Language"] = []
  # payload["NextChoiceId"] = 305 # FICME
  # payload["NextAnswerId"] = 1
  payload["Height"] = stimulusWH[data]["h"]
  payload["Width"] = stimulusWH[data]["w"]
  payload["GraphicVersion"] = 1608739073008 # FIXME
  payload["GraphicID"] = stimulusDummyGraphicId[data][geometry] # getStimulusDummy(data, geometry) dummy for each data Needs to be uploaded 
  payload["Clicks"] = 1
  payload["Regions"] = getRegions(data, task, repetition)
  payload["QuestionText_Unsafe"] = f"<div id=\"3DFMQuestion\">{getQuestionText(data, task)}</div>"
  heatmap["Payload"] = payload

  return heatmap


def addReminderQuestion(surveyData, qid):
  return {
      "SurveyID": surveyData["SurveyEntry"]["SurveyID"],
      "Element": "SQ",
      "PrimaryAttribute": f"QID{qid}",
      "SecondaryAttribute": "reminder_message",
      "TertiaryAttribute": None,
      "Payload": {
        "QuestionText": "<div>\n<p>Unfortunately this was an invalid answer. This was number ${e://Field/fault_count} out of 10 allowed mistakes.<br />\n<br />\n<strong>Please remember:</strong></p>\n\n<ul>\n\t<li>It is important to click on one of the colored nodes to answer the question! If you click somewhere else the answer is not valid.</li>\n\t<li>If you do this more than 10 times during the study, the survey will end and we will not be able to pay you.</li>\n\t<li>Please follow the instructions and click as closely as possible on the colored nodes when answering a question.</li>\n</ul>\n\n<div>&nbsp;</div>\n\n<div>Thank you for your understanding and cooperation.</div>\n\n<div>&nbsp;</div>\n\n<div>Click the Next button to continue.</div>\n</div>",
        "DefaultChoices": False,
        "DataExportTag": f"QID{qid}",
        "QuestionType": "DB",
        "Selector": "TB",
        "Configuration": {
          "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "reminder_message",
        "ChoiceOrder": [],
        "Validation": {
          "Settings": {
            "Type": "None"
          }
        },
        "GradingData": [],
        "Language": [],
        # "NextChoiceId": 4, # FIXME
        # "NextAnswerId": 1,
        "QuestionID": f"QID{qid}",
        "QuestionText_Unsafe": "<div>\n<p>Unfortunately this was an invalid answer. This was number ${e://Field/fault_count} out of 10 allowed mistakes.<br />\n<br />\n<strong>Please remember:</strong></p>\n\n<ul>\n\t<li>It is important to click on one of the colored nodes to answer the question! If you click somewhere else the answer is not valid.</li>\n\t<li>If you do this more than 10 times during the study, the survey will end and we will not be able to pay you.</li>\n\t<li>Please follow the instructions and click as closely as possible on the colored nodes when answering a question.</li>\n</ul>\n\n<div>&nbsp;</div>\n\n<div>Thank you for your understanding and cooperation.</div>\n\n<div>&nbsp;</div>\n\n<div>Click the Next button to continue.</div>\n</div>",
        "DataVisibility": {
          "Private": False,
          "Hidden": False
        }
      }
    }

def addBlocks(surveyBlocks, surveyQuestions):

  # get current Block number
  # blockNumber = max(list(map(int, surveyBlocks["Payload"].keys())))
  blockNumber = 25

  for question in surveyQuestions:
    blockNumber += 1
    block = {
          "Type": "Standard",
          "SubType": "",
          "Description": question["Payload"]["QuestionDescription"],
          "ID": f"BL_{str(blockNumber).zfill(15)}",
          "BlockElements": [
            {
              "Type": "Question",
              "QuestionID": question["Payload"]["QuestionID"]
            }
          ],
          "Options": {
            "BlockLocking": "false",
            "RandomizeQuestions": "false",
            "BlockVisibility": "Collapsed"
          }
        }
    surveyBlocks["Payload"][blockNumber] = block
  surveyBlocks["Payload"] = {str(key):val for key, val in dict(sorted({int(k):v for k,v in surveyBlocks["Payload"].items()}.items())).items()}
  return surveyBlocks

def addSurveyQuestionsFlowEmbeddedData(surveyQuestions):
  dataFields = [
                {"fieldName": "screen_width", "defaultValue": "0"},
                {"fieldName": "screen_height", "defaultValue": "0"},
                {"fieldName": "fault_count", "defaultValue": "0"},
                {"fieldName": "show_reminder_message", "defaultValue": "0"},
                {"fieldName": "question_count", "defaultValue": "0"},
                {"fieldName": "time_intro_end", "defaultValue": "0"},
                {"fieldName": "time_training_end", "defaultValue": "0"},
                {"fieldName": "time_stimulus_end", "defaultValue": "0"}
              ]
  dataFields += [{"fieldName": f"timing_question_{question['Payload']['QuestionDescription']}", "defaultValue": "-1"} for question in surveyQuestions if question["Payload"]["QuestionType"] == "HeatMap"]
  dataFields += [{"fieldName": f"timing_loading_{question['Payload']['QuestionDescription']}", "defaultValue": "-1"} for question in surveyQuestions if question["Payload"]["QuestionType"] == "HeatMap"]
  dataFields += [{"fieldName": f"timing_stimulus_{question['Payload']['QuestionDescription']}", "defaultValue": "-1"} for question in surveyQuestions if question["Payload"]["QuestionType"] == "HeatMap"]

  embeddedData = []

  for dataField in dataFields:
    embeddedData.append({
      "Description": f"{dataField['fieldName']}",
      "Type": "Custom",
      "Field": f"{dataField['fieldName']}",
      "VariableType": "Scale",
      "DataVisibility": [],
      "Value": f"{dataField['defaultValue']}"
    })

  return embeddedData

def generateFlowQuestions(surveyQuestions, surveyBlocks, randomizerBy=None):
  # randomizer by ... data idx=0, geometry idx=3, task idx=1, repetition idx= 2
  global currentFlowId

  if randomizerBy is dataList:
    randIdx = 0
  elif randomizerBy is taskList:
    randIdx = 1
  elif randomizerBy is repetitionList:
    randIdx = 2
  elif randomizerBy is geometryList:
    randIdx = 3
  else:
    randIdx = None
    randomizerBy = ["all"]

  randomizer = {}
  for item in randomizerBy:
    currentFlowId += 1
    randomizer[str(item)] = {
      "Type": "BlockRandomizer",
      "FlowID": f"FL_{currentFlowId}",
      "SubSet": 0,
      "Flow": []
    }

  for question in [q for q in surveyQuestions if q["Payload"]["QuestionType"] == "HeatMap"]:
    currentFlowId += 1
    group = {
      "Type": "Group",
      "FlowID": f"FL_{currentFlowId}",
      "Description": question["Payload"]["QuestionDescription"],
      "Flow": []
    }
    # Question
    block = list(item for key, item in surveyBlocks["Payload"].items() if item["Description"] == question["Payload"]["QuestionDescription"])[0]
    currentFlowId += 1
    questionBlock = {
      "Type": "Standard",
      "ID": block["ID"],
      "FlowID": f"FL_{currentFlowId}",
      "Autofill": []
    }
    group["Flow"].append(questionBlock)

    # Branch To Check Answer Validity
    currentFlowId += 1
    branchValidity = {
      "Type": "Branch",
      "FlowID": f"FL_{currentFlowId}",
      "Description": f"validity_check_{question['Payload']['QuestionDescription']}",
      "BranchLogic": {},
      "Flow": []
    }

    branchValidity["BranchLogic"]["0"] = {}
    rCount = 0
    for region in question["Payload"]["Regions"]:
      locatorOperand = f"q://{question['PrimaryAttribute']}/Region/{rCount}"
      branchValidity["BranchLogic"]["0"][rCount] = {
        "LogicType": "Question",
        "QuestionID": question["PrimaryAttribute"],
        "QuestionIsInLoop": "no",
        "ChoiceLocator": locatorOperand,
        "Operator": "NotClickedIn",
        "QuestionIDFromLocator": question["PrimaryAttribute"],
        "LeftOperand": locatorOperand,
        "Type": "Expression"
      }
      if rCount > 0:
        branchValidity["BranchLogic"]["0"][rCount]["Description"] = f"<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">{question['Payload']['QuestionDescription']}</span> <span class=\"LeftOpDesc\">{locatorOperand}</span> <span class=\"OpDesc\">Is Not Clicked In</span> "
        branchValidity["BranchLogic"]["0"][rCount]["Conjuction"] = "And"
      else:
        branchValidity["BranchLogic"]["0"][rCount]["Description"] = f"<span class=\"ConjDesc\">If</span> <span class=\"QuestionDesc\">{question['Payload']['QuestionDescription']}</span> <span class=\"LeftOpDesc\">{locatorOperand}</span> <span class=\"OpDesc\">Is Not Clicked In</span> "
      rCount += 1
    
    branchValidity["BranchLogic"]["0"]["Type"] = "If"
    branchValidity["BranchLogic"]["Type"] = "BooleanExpression"

    # branch["Flow"] -> Embedded Data > Block Reminder Msg > Branch
    currentFlowId += 1
    branchValidityEmbeddedData = {
      "Type": "EmbeddedData",
      "FlowID": f"FL_{currentFlowId}",
      "EmbeddedData": [
        {
          "Description": "fault_count",
          "Type": "Custom",
          "Field": "fault_count",
          "VariableType": "Scale",
          "DataVisibility": [],
          "Value": "$e{ e://Field/fault_count + 1 }"
        }
      ]
    }
    branchValidity["Flow"].append(branchValidityEmbeddedData)

    currentFlowId += 1
    faultMessageBlock = list(item for key, item in surveyBlocks["Payload"].items() if item["Description"] == "reminder_message")[0]
    branchValidityMessage = {
      "Type": "Block",
      "ID": faultMessageBlock["ID"],
      "FlowID": f"FL_{currentFlowId}",
      "Autofill": []
    }
    branchValidity["Flow"].append(branchValidityMessage)

    currentFlowId += 2
    branchEndOfSurvey = {
      "Type": "Branch",
      "FlowID": f"FL_{currentFlowId - 1}",
      "Description": f"end_of_survey_check_{question['Payload']['QuestionDescription']}",
      "BranchLogic": {
        "0": {
          "0": {
            "LogicType": "EmbeddedField",
            "LeftOperand": "fault_count",
            "Operator": "GreaterThan",
            "RightOperand": "10",
            "_HiddenExpression": False,
            "Type": "Expression",
            "Description": "<span class=\"ConjDesc\">If</span>  <span class=\"LeftOpDesc\">fault_count</span> <span class=\"OpDesc\">Is Greater Than</span> <span class=\"RightOpDesc\"> 10 </span>"
          },
          "Type": "If"
        },
        "Type": "BooleanExpression"
      },
      "Flow": [
        {
          "Type": "EndSurvey",
          "FlowID": f"FL_{currentFlowId}",
          "EndingType": "Advanced",
          "Options": {
            "Advanced": "true",
            "SurveyTermination": "DisplayMessage",
            "EOSMessageLibrary": "UR_em054I1HkwZx7Bb",
            "EOSMessage": "MS_9EPRkTsz4V9c6u9"
          }
        }
      ]
    }
    branchValidity["Flow"].append(branchEndOfSurvey)

    group["Flow"].append(branchValidity)

    if randIdx is None:
      randKey = "all"
    else:
      keys = question["Payload"]["QuestionDescription"].split("_", 2)
      randKeys = [keys[0], keys[1][3], keys[1][4], keys[2]]
      randKey = randKeys[randIdx]
    randomizer[randKey]["Flow"].append(group)
    randomizer[randKey]["SubSet"] += 1

  return [item for key, item in randomizer.items()]


if __name__ == "__main__":
  # read survey template
  with open('3D_Flow_Maps_Template.qsf', encoding="utf8") as jsonFile:
    surveyData = json.load(jsonFile)
    
    surveyBlocks = next((item for item in surveyData["SurveyElements"] if item["Element"] == "BL"), None)
    surveyFlow = next((item for item in surveyData["SurveyElements"] if item["Element"] == "FL"), None)
    surveyOptions = next((item for item in surveyData["SurveyElements"] if item["Element"] == "SO"), None)
    surveyScoring = next((item for item in surveyData["SurveyElements"] if item["Element"] == "SCO"), None)
    surveyProject = next((item for item in surveyData["SurveyElements"] if item["Element"] == "PROJ"), None)
    surveyStatistics = next((item for item in surveyData["SurveyElements"] if item["Element"] == "STAT"), None)
    surveyQuestionCount = next((item for item in surveyData["SurveyElements"] if item["Element"] == "QC"), None)
    surveyDefaultResponseSet = next((item for item in surveyData["SurveyElements"] if item["Element"] == "RS"), None)
    
    # surveyQuestionsTest = next((item for item in surveyData["SurveyElements"] if item["Element"] == "SQ"), None)
    surveyQuestionsBefore = list(filter(lambda item: item["Element"] == "SQ" and int(item["PrimaryAttribute"][3:]) <= 38, surveyData["SurveyElements"]))
    # all after study questions
    surveyQuestionsAfter = list(filter(lambda item: item["Element"] == "SQ" and int(item["PrimaryAttribute"][3:]) >= 112, surveyData["SurveyElements"]))

    surveyQuestionsStudy = []
    # Heatmap Questions
    surveyQuestionsStudy += generateHeatMapQuestions(surveyData, len(surveyQuestionsBefore))
    # Reminder
    surveyQuestionsStudy.append(addReminderQuestion(surveyData, len(surveyQuestionsBefore) + len(surveyQuestionsStudy) + 1))

    surveyQuestions = surveyQuestionsBefore + surveyQuestionsStudy + surveyQuestionsAfter

    # add Blocks
    surveyBlocks = addBlocks(surveyBlocks, surveyQuestionsStudy)

    # generate Flow
    embeddedDataIndex = next((index for (index, d) in enumerate(surveyFlow["Payload"]["Flow"]) if d["Type"] == "EmbeddedData" and d["FlowID"] == "FL_2"), None)
    surveyFlow["Payload"]["Flow"][embeddedDataIndex]["EmbeddedData"] += addSurveyQuestionsFlowEmbeddedData(surveyQuestionsStudy)
    
    surveyStartIndex = next((index for (index, d) in enumerate(surveyFlow["Payload"]["Flow"]) if "ID" in d and d["ID"] == "BL_000000000000025" and d["FlowID"] == "FL_47"), None)
    currentFlowId = surveyFlow["Payload"]["Properties"]["Count"]
    surveyFlow["Payload"]["Flow"][surveyStartIndex + 1: surveyStartIndex + 1] = generateFlowQuestions(surveyQuestionsStudy, surveyBlocks)
    surveyFlow["Payload"]["Properties"]["Count"] = currentFlowId
    surveyElements = []
    # ORDER: BL, FL, SO, SCO, PROJ, 
    surveyElements.append(surveyBlocks)
    surveyElements.append(surveyFlow)
    surveyElements.append(surveyOptions)
    surveyElements.append(surveyScoring)
    surveyElements.append(surveyProject)
    surveyElements.append(surveyStatistics)
    surveyElements.append(surveyQuestionCount)
    surveyElements.append(surveyDefaultResponseSet)
    surveyElements += surveyQuestions

    newServeyData = {}
    newServeyData["SurveyEntry"] = surveyData["SurveyEntry"]
    newServeyData["SurveyElements"] = surveyElements

    # save to new file
    with open('3D_Flow_Maps_Survey.qsf', 'w') as outFile:
      json.dump(newServeyData, outFile)