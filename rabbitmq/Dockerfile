FROM rabbitmq:3.7-management

RUN apt-get update && \
apt-get install -y curl unzip

RUN curl https://dl.bintray.com/rabbitmq/community-plugins/3.7.x/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-3.7.x.zip > rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
unzip rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
rm -f rabbitmq_delayed_message_exchange-20171201-3.7.x.zip && \
mv rabbitmq_delayed_message_exchange-20171201-3.7.x.ez plugins/

RUN rabbitmq-plugins enable rabbitmq_delayed_message_exchange && \
	rabbitmq-plugins enable rabbitmq_mqtt && \
	rabbitmq-plugins enable rabbitmq_web_mqtt && \
	rabbitmq-plugins enable rabbitmq_management && \
	rabbitmq-plugins enable rabbitmq_auth_backend_cache && \
	rabbitmq-plugins enable rabbitmq_auth_backend_http && \
	rabbitmq-plugins enable rabbitmq_peer_discovery_aws

COPY definitions.json /etc/rabbitmq/definitions.json
COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
