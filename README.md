# VCCAssignment2
Set up a virtual machine in Google Cloud Platform (GCP), implement auto-scaling policies based on workload, and configure security measures like firewall rules and IAM.
Google Cloud Platform Autoscaling Architecture

Overview

This repository contains the system architecture for implementing autoscaling in Google Cloud Platform (GCP). The architecture leverages managed instance groups (MIG), autoscalers, cloud monitoring, and logging to ensure efficient scaling based on CPU utilization.

Architecture Components

1. Google Cloud Platform (GCP)

The overall cloud environment where all the infrastructure components are hosted.

2. Load Balancer (Optional)

Distributes traffic among instances.

Helps in load management and balancing incoming requests.

3. Managed Instance Group (MIG)

A collection of identical virtual machine instances managed together.

Ensures high availability and automatic scaling.

4. Virtual Machines (Instances)

Instances in the MIG handle application execution and request processing.

Logs CPU usage for monitoring and scaling decisions.

5. Cloud Monitoring (Stackdriver)

Monitors CPU usage of instances.

Provides real-time insights into system performance.

6. Cloud Logging

Records scaling events for auditing and troubleshooting.

7. Autoscaler

Monitors CPU utilization of instances.

Adds new instances when CPU usage exceeds 60%.

Removes instances when CPU usage drops below 40%.

8. Instance Template

Defines virtual machine configuration.

Specifies machine type, disk size, and preconfigured startup scripts.
