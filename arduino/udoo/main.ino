// serialProtocol.ino

void setup() {
	Serial.begin(9600);
	Serial.setTimeout(10);
}

String data;

void loop() {
	data = Serial.readStringUntil('%'); //By default the delimiter is '\n' newline
	Serial.println(data);
}

