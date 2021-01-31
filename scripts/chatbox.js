var messages = [], //array that hold the record of each string in chat
  lastUserMessage = "", //keeps track of the most recent input string from the user
  userName = 'user',
  botMessage = "", //var keeps track of what the chatbot is going to say
  botName = 'AA-RON', //name of the chatbot
  talking = true; //when false the speach function doesn't work

//flags
var flav_empty = false;
var flav_notempty = false;
var ffood = false;
var fcomp = false;
var lavatory_waitlist;

//edit this function to change what the chatbot says
function chatbotResponse() {
  talking = true;
  botMessage = "I'm sorry, I couldn't quite catch that."; //the default message

  user_in = lastUserMessage.toLowerCase();
  if (flav_empty) {
      botMessage = "You may go now.";
      flav_empty = false;
  } else if (flav_notempty) {
      var newList = lavatory_waitlist+1;
      var line_pos;
      switch (newList) {
          case 1:
              line_pos = "st";
              break;
          case 2:
              line_pos = "nd";
              break;
          case 3:
              line_pos = "rd";
              break;
          default:
              line_pos = "th";
      }
      botMessage = "You are " + newList + line_pos + " person in line.";
  } else if (ffood) {
      botMessage = "I will get it sent to you shortly.";
      ffood = false;
  } else if (fcomp) {
      botMessage = "A human attendant will be notified of your complaint."
      fcomp = false;
  } else if (user_in == "hi" || user_in == "hello") {
      botMessage = "Hello, my name is AA-RON and I will be your personal flight bot-tendant today. Feel free to ask me for anything you may need. For a detailed list of what I can help you with, send “Help” in chat. Thank you for choosing American Airlines.";
  } else if (user_in.includes("help")) {
      botMessage = "Things I can help with:\n• Lavatory wait list\n• Food & beverage delivery\n• Complaints\n• Call human attendant\n• Flight stats";
  } else if ((!flav_empty || !flav_notempty) && (user_in.includes("lavatory") || user_in.includes("bathroom") || user_in.includes("restroom"))) {
      lavatory_waitlist = 0;
      if (lavatory_waitlist == 0) {
          botMessage = "Available ✓\nWould you like to be admitted?";
          flav_empty = true;
      } else if (lavatory_waitlist > 0) {
          botMessage = lavatory_waitlist + " people waiting in line.\nWould you like to be added to the waiting list?";
          flav_notempty = true;
      }
  }
  else if (!ffood && (user_in.includes("food") || user_in.includes("drink") || user_in.includes("beverage") || user_in.includes("eat") || user_in.includes("snack"))) {
      botMessage = "What would you like?";
      ffood = true;
  } else if (!fcomp && user_in.includes("complaint")) {
      botMessage = "What complaints do you have?";
      fcomp = true;
  } else if (user_in.includes("attendant")) {
      botMessage = "A human attendant will be with you shortly.";
  } else if (user_in.includes("about")) {
      botMessage = "My name is AA-RON, short for American Airlines-Responsive Online Network. To learn more about my namesake, watch this video: https://www.youtube.com/watch/Dd7FixvoKBw";
  }
}

//this runs each time enter is pressed.
//It controls the overall input and output
function newEntry() {
  //if the message from the user isn't empty then run
  if (document.getElementById("chatbox").value != "") {
    //pulls the value from the chatbox ands sets it to lastUserMessage
    lastUserMessage = document.getElementById("chatbox").value;
    //sets the chat box to be clear
    document.getElementById("chatbox").value = "";
    //adds the value of the chatbox to the array messages
    messages.push("<b>" + userName + ":</b> " + lastUserMessage);
    //Speech(lastUserMessage);  //says what the user typed outloud
    //sets the variable botMessage in response to lastUserMessage
    chatbotResponse();
    //add the chatbot's name and message to the array messages
    messages.push("<b>" + botName + ":</b> " + botMessage);
    // says the message using the text to speech function written below
    Speech(botMessage);
    //outputs the last few array elements of messages to html
    for (var i = 1; i < 11; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
  }
}

//text to Speech
function Speech(say) {
  if ('speechSynthesis' in window && talking) {
    var utterance = new SpeechSynthesisUtterance(say);
    speechSynthesis.speak(utterance);
  }
}

//runs the keypress() function when a key is pressed
document.onkeypress = keyPress;
//if the key pressed is 'enter' runs the function newEntry()
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  if (key == 13 || key == 3) {
    //runs this function when enter is pressed
    newEntry();
  }
}

//clears the placeholder text ion the chatbox
//this function is set to run when the users brings focus to the chatbox, by clicking on it
function placeHolder() {
  document.getElementById("chatbox").placeholder = "";
}
