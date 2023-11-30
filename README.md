# rapa

# 작물의 온습도 관리 시스템
# 1️. 작품소개
MQTT와 Node-Red를 이용하여 사용자가 작물의 상태를 확인하고 센서를 작동하는 시스템


MQTT를 이용하여 각 센서의 측정값(메세지)를 송수신

Node-Red를 통해 측정값을 시각화 및 센서 작동

# 2. MQTT
![image](https://github.com/2023rapa-project/rapa/assets/132196804/f8a23178-36cc-44a3-83ee-41f327a02ee5)

MQTT는 발행/구독 메시징 송수신 프로토콜입니다.

MQTT는 보통 M2M(machine to machine)이나 IoT에서 사용됩니다.

구성 : publisher, broker, subscriber

# 3. Node-Red
![image](https://github.com/2023rapa-project/rapa/assets/132196804/4f2fbb07-eb6e-4e74-a2f3-7e9609e8b0d1)

Node-RED는 하드웨어 장치, API 및 온라인 서비스를 서로 쉽게 연결할 수 있는 그래픽 개발 도구입니다.

Node-RED는 사전 구축된 수많은 노드와 함께 배송됩니다. 개발자는 애플리케이션에서 이러한 노드를 사용하여 MQTT 프로토콜, Modbus/TCP 프로토콜을 사용하거나 이메일을 통해 데이터를 전송하는 것과 같은 복잡한 작업을 쉽게 수행할 수 있습니다.

# 4. 블록도
![image](https://github.com/2023rapa-project/rapa/assets/132196804/444923cb-db94-4eac-a61b-0d3ea322be90)

# 5. 영상
https://youtu.be/HpI33QaASJ0
