# Set up pi cluster

#### On master node
- Load OS - Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1015-raspi aarch64)
- Add `cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory` to the end of the file `/boot/firmware/cmdline.txt`
- reboot
- Install k3s `curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE=644 sh -`
- `git clone https://github.com/carlosedp/cluster-monitoring.git` and follow instructions to install monitoring on master k3s node.


#### On agent node
- Load OS - Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1015-raspi aarch64)
- Add `cgroup_enable=cpuset cgroup_memory=1 cgroup_enable=memory` to the end of the file `/boot/firmware/cmdline.txt`
- reboot
- Install k3s `curl -sfL https://get.k3s.io | K3S_URL=https://192.168.0.100:6443 K3S_TOKEN=K1056b8d6ffb0eded2c4e96b25904f79cb8560666368ffd32059069d4e1968a55c5::server:a5d1e2c37faf1db0f79a5709cb0bce69  K3S_NODE_NAME=worker1 K3S_KUBECONFIG_MODE=644 sh -` (use your own token and IP address)

#### Verify that everything is working on Grafana
And note that persistence is not configured for prometheus
