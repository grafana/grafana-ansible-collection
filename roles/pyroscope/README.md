# Ansible Role: Pyroscope

Deploy and manage [Grafana Pyroscope](https://grafana.com/oss/pyroscope/), a continuous profiling platform that helps you analyze your application performance.

## Requirements

- Ansible >= 2.12
- Supported operating systems:
  - Ubuntu 20.04, 22.04, 24.04
  - Debian 11, 12
  - RHEL/CentOS/Rocky/AlmaLinux 8, 9
  - Fedora 38, 39, 40

## Role Variables

### Installation Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `pyroscope_version` | `latest` | Version of Pyroscope to install |
| `pyroscope_manage_repo` | `true` | Whether to manage the package repository |

### Repository Configuration

#### YUM/DNF Repository
| Variable | Default | Description |
|----------|---------|-------------|
| `pyroscope_yum_repo` | `https://packages.grafana.com/oss/rpm` | YUM repository URL |
| `pyroscope_yum_key` | `https://packages.grafana.com/gpg.key` | YUM repository GPG key |
| `pyroscope_rhsm_subscription` | `""` | Red Hat Subscription Management subscription |
| `pyroscope_rhsm_repo` | `""` | Red Hat Subscription Management repository |

#### APT Repository
| Variable | Default | Description |
|----------|---------|-------------|
| `pyroscope_apt_release_channel` | `stable` | APT release channel |
| `pyroscope_apt_arch` | Auto-detected | Architecture (arm64 or amd64) |
| `pyroscope_apt_repo` | Auto-configured | APT repository configuration |
| `pyroscope_apt_key` | `https://apt.grafana.com/gpg.key` | APT repository GPG key |

### Installation Paths

| Variable | Default | Description |
|----------|---------|-------------|
| `pyroscope_config_dir` | `/etc/pyroscope` | Configuration directory |
| `pyroscope_data_dir` | `/var/lib/pyroscope` | Data storage directory |
| `pyroscope_log_dir` | `/var/log/pyroscope` | Log directory |
| `pyroscope_pid_file` | `/var/run/pyroscope/pyroscope.pid` | PID file location |

### Service Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `pyroscope_service_name` | `pyroscope` | Systemd service name |
| `pyroscope_user` | `pyroscope` | System user for running Pyroscope |
| `pyroscope_group` | `pyroscope` | System group for Pyroscope |
| `pyroscope_cap_net_bind_service` | `false` | Enable capability to bind to ports below 1024 |

### Pyroscope Configuration

The main configuration is defined in `pyroscope_config` dictionary:

#### Server Configuration

```yaml
pyroscope_config:
  target: all  # Target modules to load (default: all)

  server:
    http_listen_address: "0.0.0.0"
    http_listen_port: 4040
    grpc_listen_address: "0.0.0.0"
    grpc_listen_port: 4041
    log_level: info
    log_format: logfmt
    graceful_shutdown_timeout: 30s
```

#### Storage Configuration

Pyroscope supports multiple storage backends:

##### Filesystem (default)
```yaml
pyroscope_config:
  storage:
    backend: filesystem
    filesystem:
      dir: /var/lib/pyroscope/data  # Default: {{ pyroscope_data_dir }}/data
```

##### S3
```yaml
pyroscope_config:
  storage:
    backend: s3
    s3:
      bucket_name: my-pyroscope-bucket
      endpoint: s3.amazonaws.com
      region: us-east-1
      access_key_id: YOUR_ACCESS_KEY
      secret_access_key: YOUR_SECRET_KEY
      insecure: false
```

##### Google Cloud Storage
```yaml
pyroscope_config:
  storage:
    backend: gcs
    gcs:
      bucket_name: my-pyroscope-bucket
      service_account: /path/to/service-account.json
```

##### Azure Blob Storage
```yaml
pyroscope_config:
  storage:
    backend: azure
    azure:
      container_name: my-pyroscope-container
      account_name: myaccount
      account_key: YOUR_ACCOUNT_KEY
```

#### Distributor Configuration

```yaml
pyroscope_config:
  distributor:
    pushtimeout: 30s  # Push timeout duration
```

#### Ingester Configuration

```yaml
pyroscope_config:
  ingester:
    lifecycler:
      address: 127.0.0.1
      ring:
        kvstore:
          store: inmemory  # Options: inmemory, consul, etcd, memberlist
        replication_factor: 1
```

#### Querier Configuration

```yaml
pyroscope_config:
  querier:
    query_store_after: 0s  # Query store delay
```

#### Query Scheduler Configuration

```yaml
pyroscope_config:
  query_scheduler:
    max_outstanding_requests_per_tenant: 100
```

#### Compactor Configuration

```yaml
pyroscope_config:
  compactor:
    compaction_interval: 10m
```

#### Store Gateway Configuration

Configure for object storage backends:

```yaml
pyroscope_config:
  store_gateway: {}  # Additional store gateway settings
```

#### Memberlist Configuration (Clustering)

For running Pyroscope in clustered mode:

```yaml
pyroscope_config:
  memberlist:
    bind_port: 7946
    join_members: []  # List of cluster members to join
      # - pyroscope-1.example.com
      # - pyroscope-2.example.com
```

#### Limits Configuration

Configure ingestion and query limits:

```yaml
pyroscope_config:
  limits:
    max_label_name_length: 1024
    max_label_value_length: 2048
    max_label_names_per_series: 30
    # Additional limits can be configured as needed:
    # max_global_series_per_user: 1000000
    # max_global_series_per_metric: 0
    # ingestion_rate: 100000
    # ingestion_burst_size: 200000
```

#### Multi-tenancy

Enable multi-tenancy for isolating data between different tenants:

```yaml
pyroscope_config:
  multitenancy_enabled: false  # Default: false
```

#### Analytics Configuration

Control telemetry and usage reporting:

```yaml
pyroscope_config:
  analytics:
    reporting_enabled: true  # Default: true
```

#### API Configuration

Configure the API base URL:

```yaml
pyroscope_config:
  api:
    base_url: ""  # API base URL if needed
```

### Configuration Overrides

You can override any configuration using `pyroscope_config_overrides`. This dictionary will be merged with the default `pyroscope_config`:

```yaml
pyroscope_config_overrides:
  server:
    http_listen_port: 8080
  compactor:
    block_retention: 48h
  # Any other configuration options can be overridden here
```

### Environment Variables

Set environment variables for the Pyroscope service:

```yaml
pyroscope_environment_variables:
  GOGC: "100"
  GOMAXPROCS: "4"
  # Add any other environment variables as needed
```

### Systemd Service Overrides

Override systemd service settings for performance tuning:

```yaml
pyroscope_systemd_service_overrides:
  LimitNOFILE: 65536
  TimeoutStartSec: 300
  # Add any other systemd service overrides as needed
```

## Dependencies

None.

## Example Playbook

### Basic Installation

```yaml
- hosts: pyroscope
  become: true
  roles:
    - role: grafana.grafana.pyroscope
```

### Production Setup with S3 Storage

```yaml
- hosts: pyroscope
  become: true
  roles:
    - role: grafana.grafana.pyroscope
      vars:
        pyroscope_version: "1.2.0"
        pyroscope_config_overrides:
          storage:
            backend: s3
            s3:
              bucket_name: production-pyroscope
              region: us-west-2
              access_key_id: "{{ vault_aws_access_key }}"
              secret_access_key: "{{ vault_aws_secret_key }}"
          server:
            http_listen_port: 4040
            log_level: warn
          limits:
            ingestion_rate: 500000
            ingestion_burst_size: 1000000
          compactor:
            block_retention: 72h
```

### Clustered Setup

```yaml
- hosts: pyroscope_cluster
  become: true
  roles:
    - role: grafana.grafana.pyroscope
      vars:
        pyroscope_config_overrides:
          storage:
            backend: s3
            s3:
              bucket_name: shared-pyroscope-storage
          memberlist:
            bind_port: 7946
            join_members: "{{ groups['pyroscope_cluster'] }}"
          ingester:
            lifecycler:
              ring:
                kvstore:
                  store: consul
                  consul:
                    host: consul.example.com:8500
                replication_factor: 3
```

### Development Setup

```yaml
- hosts: dev
  become: true
  roles:
    - role: grafana.grafana.pyroscope
      vars:
        pyroscope_config_overrides:
          server:
            log_level: debug
          storage:
            backend: filesystem
            filesystem:
              directory: /tmp/pyroscope-data
          analytics:
            reporting_enabled: false
```

## Configuration Reference

For a complete list of configuration options, see the [Pyroscope Configuration Documentation](https://grafana.com/docs/pyroscope/latest/configure-server/reference-configuration-parameters/).

## Tags

- `pyroscope_install` - Installation tasks only
- `pyroscope_configure` - Configuration tasks only
- `pyroscope_run` - Service management tasks

## Testing

This role includes Molecule tests for multiple scenarios:

```bash
# Run default test scenario
molecule test

# Run alternative scenario (S3 backend, multi-tenancy)
molecule test -s alternative

# Test specific platform
molecule test --platform-name ubuntu-22.04
```

## License

Apache License 2.0

## Author Information

This role was created by Grafana Labs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please use the [GitHub issue tracker](https://github.com/grafana/grafana-ansible-collection/issues).