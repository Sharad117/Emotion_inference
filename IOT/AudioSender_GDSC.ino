// #include <Arduino.h>
// #include <WiFi.h>
// #include <driver/i2s.h>

// #define AUDIO_BUFFER_MAX 800

// uint8_t audioBuffer[AUDIO_BUFFER_MAX];
// uint8_t transmitBuffer[AUDIO_BUFFER_MAX];
// uint32_t bufferPointer = 0;

// const char* ssid     = "SSID";
// const char* password = "Passd";
// const char* host     = "IP";

// bool transmitNow = false;

// WiFiClient client;

// i2s_config_t i2s_config = {
//    .mode = i2s_mode_t(I2S_MODE_MASTER | I2S_MODE_RX), // Receive, not transfer
//    .sample_rate = 44100, // 44.1KHz stereo => 44100 sample rate
//    .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT, // could only get it to work with 32bits
//    .channel_format = I2S_CHANNEL_FMT_RIGHT_LEFT, // although the SEL config should be left, it seems to transmit on right
//    .communication_format = i2s_comm_format_t(I2S_COMM_FORMAT_I2S | I2S_COMM_FORMAT_I2S_MSB),
//    .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1, // Interrupt level 1
//    .dma_buf_count = 8, // number of buffers
//    .dma_buf_len = 64   // samples per buffer
// };

// void setup() {
//   Serial.begin(115200);

//   WiFi.mode(WIFI_STA);
//   WiFi.begin(ssid, password);

//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }

//   Serial.println("");
//   Serial.println("WiFi connected");
//   Serial.println("MY IP address: ");
//   Serial.println(WiFi.localIP());

//   i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL); //install and start i2s driver
//   i2s_set_pin(I2S_NUM_0, NULL); //for internal DAC

//   const int port = 1883;
//   while (!client.connect(host, port)) {
//     Serial.println("connection failed");
//     delay(1000);
//   }

//   Serial.println("connected to server");
// }

// void loop() {
//   size_t bytesRead = 0;
//   i2s_read(I2S_NUM_0, (char*)audioBuffer, AUDIO_BUFFER_MAX, &bytesRead, portMAX_DELAY);
//   if(bytesRead > 0) {
//     client.write(audioBuffer, bytesRead);
//   }
// }






#include <Arduino.h>
#include <WiFi.h>
#include <driver/i2s.h>

#define AUDIO_BUFFER_MAX 800

uint8_t audioBuffer[AUDIO_BUFFER_MAX];
uint8_t transmitBuffer[AUDIO_BUFFER_MAX];
uint32_t bufferPointer = 0;

const char* ssid     = "SSID";
const char* password = "Passed";
const char* host     = "IP";
// const char* ssid = "SSID";
// const char* password = "Passwd";
// const char* host = "IP";

bool transmitNow = false;

WiFiClient client;

i2s_config_t i2s_config = {
   .mode = i2s_mode_t(I2S_MODE_MASTER | I2S_MODE_RX), // Receive, not transfer
   .sample_rate = 16000, // 44.1KHz stereo => 44100 sample rate
   .bits_per_sample = I2S_BITS_PER_SAMPLE_16BIT, // could only get it to work with 32bits
   .channel_format = I2S_CHANNEL_FMT_RIGHT_LEFT, // although the SEL config should be left, it seems to transmit on right
   .communication_format = i2s_comm_format_t(I2S_COMM_FORMAT_I2S | I2S_COMM_FORMAT_I2S_MSB),
   .intr_alloc_flags = ESP_INTR_FLAG_LEVEL1, // Interrupt level 1
   .dma_buf_count = 8, // number of buffers
   .dma_buf_len = 64   // samples per buffer
};

i2s_pin_config_t pin_config = {
    .bck_io_num = 14, // BCKL
    .ws_io_num = 15, // LRCL
    .data_out_num = -1, // not used (only for speakers)
    .data_in_num = 32 // DOUT
};
const int port = 8000;
void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("MY IP address: ");
  Serial.println(WiFi.localIP());

  i2s_driver_install(I2S_NUM_0, &i2s_config, 0, NULL); //install and start i2s driver
  i2s_set_pin(I2S_NUM_0, &pin_config); //for internal DAC

    while (!client.connect(host, port)) {
    Serial.println("connection failed");
    delay(1000);
  }
  Serial.println("Connected");
  
}
void loop() {
  size_t bytesRead = 0;
  i2s_read(I2S_NUM_0, (char *)audioBuffer, AUDIO_BUFFER_MAX, &bytesRead, portMAX_DELAY);
  if (bytesRead > 0) {
    if (!client.connected()) {
      Serial.println("Connection lost. Reconnecting...");
      reconnect();
    }
    client.write(audioBuffer, bytesRead);
  }
}

void reconnect() {
  int attempts = 0;
  const int maxAttempts = 10;
  const int baseDelay = 1000; // 1 second base delay

  while (!client.connect(host, port) && attempts < maxAttempts) {
    Serial.println("Reconnection attempt failed. Retrying...");
    delay(baseDelay * (1 << attempts)); // Exponential backoff
    attempts++;
  }

  if (client.connected()) {
    Serial.println("Reconnected successfully.");
  } else {
    Serial.println("Max reconnection attempts reached. Restarting...");
    ESP.restart(); // Restart the ESP32 if max attempts are reached
  }
}









// #include <WiFi.h>
// #include <WiFiClient.h>

// const char* ssid     = "SSID";
// const char* password = "Passwd";
// const char* host     = "IP";
// const int port = 1883;  // Use the port that your receiving device is listening on

// void setup() {
//   Serial.begin(115200);
//   connectToWiFi();
// }

// void loop() {
//   // Connect to the server
//   WiFiClient client;
//   if (client.connect(host, port)) {
//     Serial.println("Connected to server");

//     // Send the message "Namaste"
//     client.println("Namaste");

//     // Wait for 30 seconds
//     delay(30000);

//     // Close the connection
//     client.stop();
//     Serial.println("Connection closed");
//   } else {
//     Serial.print("Connection failed. Error: ");
//     // Serial.println(client.state());
//   }

//   // Wait for a while before sending the next message
//   delay(5000);
// }

// void connectToWiFi() {
//   Serial.print("Connecting to WiFi");
//   WiFi.begin(ssid, password);
  
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(1000);
//     Serial.print(".");
//   }

//   Serial.println("\nConnected to WiFi");
//   Serial.print("IP Address: ");
//   Serial.println(WiFi.localIP());
// }


























// #include <WiFi.h>
// #include <WiFiClient.h>

// const char* ssid     = "Galaxy";
// const char* password = "Trinetra*281001";
// const char* host     = "192.168.204.126";
// const int port = 1883;

// void setup() {
//   Serial.begin(115200);
//   connectToWiFi();
// }

// void loop() {
//   // Connect to the server
//   WiFiClient client;
//   if (client.connect(host, port)) {
//     Serial.println("Connected to server");

//     // Send a sine wave audio signal
//     sendSineWave(client);

//     // Close the connection
//     client.stop();
//     Serial.println("Connection closed");
//   } else {
//     Serial.print("Connection failed. Error: ");
//     // Serial.println(client.state());
//   }

//   // Wait for a while before sending the next signal
//   delay(5000);
// }

// void connectToWiFi() {
//   Serial.print("Connecting to WiFi");
//   WiFi.begin(ssid, password);
  
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(1000);
//     Serial.print(".");
//   }

//   Serial.println("\nConnected to WiFi");
//   Serial.print("IP Address: ");
//   Serial.println(WiFi.localIP());
// }

// void sendSineWave(WiFiClient& client) {
//   // Sine wave parameters
//   const float frequency = 500.0;  // Hz
//   const float duration = 1.0;     // seconds
//   const int sampleRate = 8000;
//   const int numSamples = duration * sampleRate;

//   for (int i = 0; i < numSamples; i++) {
//     // Generate a sine wave sample (8-bit unsigned)
//     uint8_t sample = 128 + 127 * sin(2 * PI * frequency * i / sampleRate);
    
//     // Send the sample to the server
//     client.write(sample);
//   }
// }
