TAMUHack American Airlines Challenge

https://github.com/AmericanAirlines/Flight-Engine/wiki/TAMUHACK-2021

What does your project do? How will it make a difference? What technologies are used?

AA-RON stands for American Airlines Responsive Online Network. It's a webapp built for the current covid age to not only reduce the transmission of COVID but to improve the in-flight customer experience. Some of the features that we have implemented are an integrated chatbot that emulates a personal flight attendant. It takes orders and keywords to do things to reduce contact with real flight attendants, so the customer stays safe and happy. We also have a flight hub where you can be taken to the duty free store or get information about the menu. Finally you can also look at where your flight is going through a map API that shows the flight path by using the flight engine API. 
	We used two different API’s to allow our program to function. Flight Engine, offered by American Airlines, provided precise coordinate data to accurately track a plane’s location throughout a flight. It also provided flight number information, used to log in to the program itself and track unique individual flights. The second API used was called Folio, used to provide a map service that can display a user’s location during a flight. Google’s Text-to-Speech API was used to integrate a text-to-speech feature for the chat bot. By integrating such technology, the app supports passengers with hearing disabilities, allowing for a broader and more expansive experience mid-flight. Stores and dining menus from the American Airlines website were used to feed data to passengers about their on-board meals or accommodations that they are able to purchase. Multiple external sources and programs allow for AA-RON to ultimately perform as an American Airlines passenger’s guide to safe and ergonomic traveling.



Thousands of people fly American each and every day. This awesome responsibility opens the door to incredible opportunities. Help us elevate the customer travel experience, boost operational efficiency and employee performance (baggage handling, gate agents, etc.), or enhance American's brand image with your innovative hacks!

Purpose: Make people feel safer and be safer on flights

Ideas
Have the app have different stages (pre-flight, on-flight, post-flight)
Contact tracing through the app
Each flight is ‘server room’
Being able to communicate with flight attendants (chat)
Telling them when the food will be coming out
Flight attendants can approve/deny requests to eat/restroom
Saying when the bathroom is available (has been cleaned?) 
Complaints
Noisy passengers
Passengers with mask off
Display arrival/ departure times

Wireframing
Notify/Chat Attendant
Complaints
Requests
Flight Hub
Look at dinner menu/drinks, when food will be served
See if bathroom is open or not
Display Flight Stats
Display flight data


Implementation


https://github.com/AmericanAirlines/Flight-Engine/#running-flight-engine-locally


URL sent to postman >> dev tool >> to API
>> API parses and takes url as info
>> Returns info to postman
-integration into app
>> get input from user
>> put into url form
>> send to api
>> get result, parse, show graphically

Ideas
>> customer experience is king
>> restroom waiting list
>> alarm when turn

AA-RON:
INTRO
Hello, my name is AA-RON and I will be your personal flight bot-tendant today. Feel free to ask me for anything you may need. For a detailed list of what I can help you with, send “Help” in chat. Thank you for choosing American Airlines.

HELP
Keyword: Help (any case) >> convert input to lower and match with “help”
“Things I can help with:
• Lavatory wait list
• Food & beverage delivery
• Complaints
• Call human attendant
• Flight stats
• About me”

*Flight stats = % of flight completed >> (curr time - dep time)/(arr time - dep time)*100

LAVATORY
Keywords: lavatory, bathroom
If empty:
	“Available ✓
	Would you like to be admitted?”
		If ‘yes’:”
			“You may go now.”

Else:
	__ people waiting in line.
	Would you like to be added to the waiting list?
		If ‘yes’:
			You are the __th/nd/etc person in line. 
			**Idea: note >> if you do not come in ~3 min you will be removed from list
FOOD & BEVERAGE
Keywords: food, drinks, beverage, eat, snack
“What would you like?”
“I will get it sent to you shortly.”

COMPLAINTS (Priority 1)
Keywords: complaint
“What complaints do you have?
If !‘~no’:
	“A human attendant will be notified of your complaint.”

HUMAN ATTENDANT
Keywords: attendant
“A human attendant will be with you shortly”

FLIGHT
Keywords: flight stats
“You are __% the way there.”

ABOUT ME
“My name is AA-RON, short for American Airlines - Responsive Online Network. To learn more about my namesake, watch this video.”


