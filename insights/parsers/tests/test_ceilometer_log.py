from insights.parsers.ceilometer_log import CeilometerCentralLog
from insights.parsers.ceilometer_log import CeilometerCollectorLog
from insights.tests import context_wrap


CENTRAL_LOG = """
2016-11-09 14:38:08.484 31654 WARNING oslo_reports.guru_meditation_report [-] Guru meditation now registers SIGUSR1 and SIGUSR2 by default for backward compatibility. SIGUSR1 will no longer be registered in a future release, so please use SIGUSR2 to generate reports.
2016-11-09 14:38:09.711 31723 INFO ceilometer.declarative [-] Definitions: {'metric': [{'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.10.1.3.1', 'type': 'lambda x: float(str(x))', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.cpu.load.1min', 'unit': 'process'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.10.1.3.2', 'type': 'lambda x: float(str(x))', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.cpu.load.5min', 'unit': 'process'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.10.1.3.3', 'type': 'lambda x: float(str(x))', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.cpu.load.15min', 'unit': 'process'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.11.9.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.cpu.util', 'unit': '%'}, {'snmp_inspector': {'post_op': '_post_op_disk', 'oid': '1.3.6.1.4.1.2021.9.1.6', 'type': 'int', 'matching_type': 'type_prefix', 'metadata': {'device': {'oid': '1.3.6.1.4.1.2021.9.1.3', 'type': 'str'}, 'path': {'oid': '1.3.6.1.4.1.2021.9.1.2', 'type': 'str'}}}, 'type': 'gauge', 'name': 'hardware.disk.size.total', 'unit': 'KB'}, {'snmp_inspector': {'post_op': '_post_op_disk', 'oid': '1.3.6.1.4.1.2021.9.1.8', 'type': 'int', 'matching_type': 'type_prefix', 'metadata': {'device': {'oid': '1.3.6.1.4.1.2021.9.1.3', 'type': 'str'}, 'path': {'oid': '1.3.6.1.4.1.2021.9.1.2', 'type': 'str'}}}, 'type': 'gauge', 'name': 'hardware.disk.size.used', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.5.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.memory.total', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.6.0', 'type': 'int', 'matching_type': 'type_exact', 'post_op': '_post_op_memory_avail_to_used'}, 'type': 'gauge', 'name': 'hardware.memory.used', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.3.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.memory.swap.total', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.4.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.memory.swap.avail', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.14.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.memory.buffer', 'unit': 'KB'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.4.15.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.memory.cached', 'unit': 'KB'}, {'snmp_inspector': {'post_op': '_post_op_net', 'oid': '1.3.6.1.2.1.2.2.1.10', 'type': 'int', 'matching_type': 'type_prefix', 'metadata': {'mac': {'oid': '1.3.6.1.2.1.2.2.1.6', 'type': "lambda x: x.prettyPrint().replace('0x', '')"}, 'speed': {'oid': '1.3.6.1.2.1.2.2.1.5', 'type': 'lambda x: int(x) / 8'}, 'name': {'oid': '1.3.6.1.2.1.2.2.1.2', 'type': 'str'}}}, 'type': 'cumulative', 'name': 'hardware.network.incoming.bytes', 'unit': 'B'}, {'snmp_inspector': {'post_op': '_post_op_net', 'oid': '1.3.6.1.2.1.2.2.1.16', 'type': 'int', 'matching_type': 'type_prefix', 'metadata': {'mac': {'oid': '1.3.6.1.2.1.2.2.1.6', 'type': "lambda x: x.prettyPrint().replace('0x', '')"}, 'speed': {'oid': '1.3.6.1.2.1.2.2.1.5', 'type': 'lambda x: int(x) / 8'}, 'name': {'oid': '1.3.6.1.2.1.2.2.1.2', 'type': 'str'}}}, 'type': 'cumulative', 'name': 'hardware.network.outgoing.bytes', 'unit': 'B'}, {'snmp_inspector': {'post_op': '_post_op_net', 'oid': '1.3.6.1.2.1.2.2.1.20', 'type': 'int', 'matching_type': 'type_prefix', 'metadata': {'mac': {'oid': '1.3.6.1.2.1.2.2.1.6', 'type': "lambda x: x.prettyPrint().replace('0x', '')"}, 'speed': {'oid': '1.3.6.1.2.1.2.2.1.5', 'type': 'lambda x: int(x) / 8'}, 'name': {'oid': '1.3.6.1.2.1.2.2.1.2', 'type': 'str'}}}, 'type': 'cumulative', 'name': 'hardware.network.outgoing.errors', 'unit': 'packet'}, {'snmp_inspector': {'oid': '1.3.6.1.2.1.4.10.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'cumulative', 'name': 'hardware.network.ip.outgoing.datagrams', 'unit': 'datagrams'}, {'snmp_inspector': {'oid': '1.3.6.1.2.1.4.3.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'cumulative', 'name': 'hardware.network.ip.incoming.datagrams', 'unit': 'datagrams'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.11.11.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'gauge', 'name': 'hardware.system_stats.cpu.idle', 'unit': '%'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.11.57.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'cumulative', 'name': 'hardware.system_stats.io.outgoing.blocks', 'unit': 'blocks'}, {'snmp_inspector': {'oid': '1.3.6.1.4.1.2021.11.58.0', 'type': 'int', 'matching_type': 'type_exact'}, 'type': 'cumulative', 'name': 'hardware.system_stats.io.incoming.blocks', 'unit': 'blocks'}]}
2016-11-09 14:38:09.986 31723 WARNING oslo_config.cfg [-] Option "rpc_backend" from group "DEFAULT" is deprecated for removal.  Its value may be silently ignored in the future.
2016-11-09 14:38:10.040 31723 INFO ceilometer.pipeline [-] Config file: {'sources': [{'interval': 600, 'meters': ['*'], 'name': 'meter_source', 'sinks': ['meter_sink']}, {'interval': 600, 'meters': ['cpu'], 'name': 'cpu_source', 'sinks': ['cpu_sink', 'cpu_delta_sink']}, {'interval': 600, 'meters': ['disk.read.bytes', 'disk.read.requests', 'disk.write.bytes', 'disk.write.requests', 'disk.device.read.bytes', 'disk.device.read.requests', 'disk.device.write.bytes', 'disk.device.write.requests'], 'name': 'disk_source', 'sinks': ['disk_sink']}, {'interval': 600, 'meters': ['network.incoming.bytes', 'network.incoming.packets', 'network.outgoing.bytes', 'network.outgoing.packets'], 'name': 'network_source', 'sinks': ['network_sink']}], 'sinks': [{'publishers': ['notifier://'], 'transformers': None, 'name': 'meter_sink'}, {'publishers': ['notifier://'], 'transformers': [{'name': 'rate_of_change', 'parameters': {'target': {'scale': '100.0 / (10**9 * (resource_metadata.cpu_number or 1))', 'type': 'gauge', 'name': 'cpu_util', 'unit': '%'}}}], 'name': 'cpu_sink'}, {'publishers': ['notifier://'], 'transformers': [{'name': 'delta', 'parameters': {'target': {'name': 'cpu.delta'}, 'growth_only': True}}], 'name': 'cpu_delta_sink'}, {'publishers': ['notifier://'], 'transformers': [{'name': 'rate_of_change', 'parameters': {'source': {'map_from': {'name': '(disk\\.device|disk)\\.(read|write)\\.(bytes|requests)', 'unit': '(B|request)'}}, 'target': {'map_to': {'name': '\\1.\\2.\\3.rate', 'unit': '\\1/s'}, 'type': 'gauge'}}}], 'name': 'disk_sink'}, {'publishers': ['notifier://'], 'transformers': [{'name': 'rate_of_change', 'parameters': {'source': {'map_from': {'name': 'network\\.(incoming|outgoing)\\.(bytes|packets)', 'unit': '(B|packet)'}}, 'target': {'map_to': {'name': 'network.\\1.\\2.rate', 'unit': '\\1/s'}, 'type': 'gauge'}}}], 'name': 'network_sink'}]}
2016-11-09 14:38:10.041 31723 INFO ceilometer.pipeline [-] detected decoupled pipeline config format
"""


COLLECTOR_LOG = """
2016-11-09 14:32:41.099 4259 WARNING oslo_config.cfg [-] Option "max_retries" from group "database" is deprecated. Use option "max_retries" from group "storage".
2016-11-09 14:36:35.464 4204 INFO cotyledon [-] Caught SIGTERM signal, graceful exiting of master process
2016-11-09 14:36:35.465 4259 INFO cotyledon [-] Caught signal (15) during service initialisation, delaying it
2016-11-09 14:38:07.280 31638 WARNING oslo_reports.guru_meditation_report [-] Guru meditation now registers SIGUSR1 and SIGUSR2 by default for backward compatibility. SIGUSR1 will no longer be registered in a future release, so please use SIGUSR2 to generate reports.
"""


def test_ceilometer_central_log():
    log = CeilometerCentralLog(context_wrap(CENTRAL_LOG))
    assert len(log.get('INFO')) == 3


def test_ceilometer_collector_log():
    log = CeilometerCollectorLog(context_wrap(COLLECTOR_LOG))
    assert len(log.get('INFO')) == 2