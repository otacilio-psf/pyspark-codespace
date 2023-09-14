set -x

cat <<'EOF' >> /usr/local/sdkman/candidates/spark/current/conf/spark-defaults.conf
spark.eventLog.enabled           true
spark.eventLog.dir               file:///usr/local/sdkman/candidates/spark/current/spark-events
spark.history.fs.logDirectory    file:///usr/local/sdkman/candidates/spark/current/spark-events
EOF

mkdir /usr/local/sdkman/candidates/spark/current/spark-events

chmod a+rwx /usr/local/sdkman/candidates/spark/current/spark-events

chmod +x /usr/local/sdkman/candidates/spark/current/sbin/start-history-server.sh