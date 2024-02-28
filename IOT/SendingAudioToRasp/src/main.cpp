#include <driver/i2s.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "SSID";
const char* password = "Passwd";
const char* mqttServer = "IP";
// const char* ssid = "SSID";
// const char* password = "PASSwd";
// const char* mqttServer = "IP";
const int mqttPort = 1883;
const char* mqttUser = "user";
const char* mqttPassword = "passwd";
const char* topic = "audio";

WiFiClient espClient;
PubSubClient client(espClient);

#define I2S_SD 32
#define I2S_WS 15
#define I2S_SCK 14
#define I2S_PORT I2S_NUM_0
#define bufferCnt 10
#define bufferLen 1024
int16_t sBuffer[bufferLen];

void reconnect() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP32AudioClient", mqttUser, mqttPassword)) {
      Serial.println("Connected to MQTT");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds");
      delay(5000);
    }
  }
}

  // Setup I2S
void i2s_install() {
  // Set up I2S Processor configuration
  const i2s_config_t i2s_config = {
    .mode = i2s_mode_t(I2S_MODE_MASTER | I2S_MODE_RX),
    // .sample_rate = 44100,
    .sample_rate = 16000,
    .bits_per_sample = i2s_bits_per_sample_t(16),
    .channel_format = I2S_CHANNEL_FMT_ONLY_LEFT,
    .communication_format = i2s_comm_format_t(I2S_COMM_FORMAT_STAND_I2S),
    .intr_alloc_flags = 0,
    .dma_buf_count = bufferCnt,
    .dma_buf_len = bufferLen,
    .use_apll = false
  };

  i2s_driver_install(I2S_PORT, &i2s_config, 0, NULL);
}

void i2s_setpin() {
  // Set I2S pin configuration
  const i2s_pin_config_t pin_config = {
    .bck_io_num = I2S_SCK,
    .ws_io_num = I2S_WS,
    .data_out_num = -1,
    .data_in_num = I2S_SD
  };

  i2s_set_pin(I2S_PORT, &pin_config);
}

void connectWiFi() {
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println(WiFi.localIP());
}

void connectMQTT(){
  client.setServer(mqttServer, mqttPort);
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP32AudioClient", mqttUser, mqttPassword)) {
      Serial.println("Connected to MQTT");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds");
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
    Serial.println("Message arrived in topic: " + String(topic));
    Serial.println("Message: " + String((char*)payload));}

void micTask(void* parameter) {

  i2s_install();
  i2s_setpin();
  i2s_start(I2S_PORT);

  size_t bytesIn = 0;
  while (1) {
    esp_err_t result = i2s_read(I2S_PORT, &sBuffer, bufferLen, &bytesIn, portMAX_DELAY);
    // if (result == ESP_OK) {
      client.publish(topic, (char*)sBuffer, bytesIn);
    // }
  }
}

void setup() {
  Serial.begin(115200);
  connectWiFi();
  connectMQTT();
    if (!client.connected()) {
    reconnect();
  }
  xTaskCreatePinnedToCore(micTask, "micTask", 10000, NULL, 1, NULL, 0);
  client.setCallback(callback);
  client.subscribe(topic);
  

}
void loop() {
}


