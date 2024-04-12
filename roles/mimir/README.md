# ansible-role-mimir
Grafana Mimir
=========

This role installs and configures a Mimir standalone application.

Role Variables
--------------
| Name | Type | Default | Description |
|---|---|---|---|
mimir_working_path|str|/usr/share/mimir|Used to specify the directory path where Mimir, a component of the Grafana Agent, stores its working files and temporary data.|
mimir_ruler_alert_path|str|/data/ruler|Used to specify the directory path where the Mimir ruler component of the Grafana Agent stores its alert files.|
mimir_http_listen_port|str|8080|Used to specify the port number on which the Mimir component of the Grafana Agent listens for incoming HTTP requests.|
mimir_http_listen_address|str|0.0.0.0|Used to specify the network address on which the Mimir component of the Grafana Agent listens for incoming HTTP requests.|
mimir_ruler.rule_path|str|/data/ruler|Used to specify the directory path where the Mimir ruler component of the Grafana Agent looks for rule files.|
mimir_ruler.alertmanager_url|str|http://127.0.0.1:8080/alertmanager|Used to specify the URL or address of the Alertmanager API that the Mimir ruler component of the Grafana Agent should communicate with.|
mimir_ruler.ring.heartbeat_period|str|2s|Used to specify the interval at which the Mimir ruler component of the Grafana Agent sends heartbeat signals to the ring.|
mimir_ruler.heartbeat_timeout|str|10s|Used to specify the maximum duration of time that the Mimir ruler component of the Grafana Agent will wait for a heartbeat signal from other components in the ring.|
mimir_alertmanager.data_dir|str|/data/alertmanager|sed to specify the directory path where the Mimir Alertmanager component of the Grafana Agent stores its data files.|
mimir_alertmanager.fallback_config_file|str|/etc/alertmanager-fallback-config.yaml|Used to specify the path to a fallback configuration file for the Mimir Alertmanager component of the Grafana Agent.|
mimir_alertmanager.external_url|str|http://localhost:9009/alertmanager|Used to specify the external URL or address at which the Mimir Alertmanager component of the Grafana Agent can be accessed.|
mimir_server.log_level|str|warn|Used to specify the log level of the server. Possible configurations error, warn, info, debug|
mimir_memberlist.join_members|[]| List of members for the Mimir cluster|
