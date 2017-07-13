# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar
export HADOOP_HOME=/opt/current/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_LIBEXEC_DIR=/opt/current/hadoop/libexec
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export HIVE_HOME=/opt/apache-hive-1.2.1-bin
export SPARK_HOME=/opt/spark-2.0.2-bin-hadoop2.7
export HBASE_HOME=/opt/hbase-1.1.9
export HBASE_CONF_DIR=/etc/hbase/conf
export HADOOP_CONF_DIR=/etc/hadoop/conf
export TEZ_HOME="/opt/apache-tez-0.8.5-bin"
export TEZ_CONF_DIR="/etc/tez/conf"
export TEZ_JARS="$TEZ_HOME"
export HIVE_CONF_DIR=/opt/current/hive-client/conf
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$HIVE_HOME/bin:$SPARK_HOME/bin:$HBASE_HOME/bin
export HIVE_AUX_JARS_PATH=/opt/apache-hive-1.2.1-bin/hcatalog/share/hcatalog:$TEZ_JARS:$TEZ_JARS/lib
export HADOOP_CLASSPATH="$TEZ_CONF_DIR:$TEZ_JARS/*:$TEZ_JARS/lib/*:$HADOOP_CLASSPATH"
export PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.3-src.zip:$PYTHONPATH
