# ModbusDockerBridgeN
A testing repo for establishing modbus conn to plc device within the host network from Docker Container attatched to bridge network instead of host network

# TO Create a docker network that enable to communicate with other device in host network
docker network create --driver bridge \
  --subnet=172.16.0.0/16 \
  --gateway=172.16.0.1 \
  --opt "com.docker.network.bridge.enable_ip_masquerade=true" \
  --opt "com.docker.network.bridge.host_binding_ipv4=0.0.0.0" \
  --opt "com.docker.network.bridge.enable_icc=true" \
  lan-bridge