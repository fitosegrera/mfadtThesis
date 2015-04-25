// serialProtocol.ino

int rotMot1 = 62;//Reed switch connected to analog 0 == digital 56

void setup() {
	Serial.begin(9600);
	Serial.setTimeout(10);
	Serial1.begin(9600);
	pinMode(rotMot1, INPUT);
}

String data;

void loop() {
	data = Serial.readStringUntil('%'); //By default the delimiter is '\n' newline
	Serial.println(data);
	if(digitalRead(rotMot1)==HIGH){
		Serial1.println(rotMot1);
	}
}

