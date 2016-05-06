Role Name
=========

Uses firewalld on CentOS/Redhat 7 or Fedora 21/22 to configure the firewall

Requirements
------------

The ansible module firewalld is used for the configuration.

Role Variables
--------------

There are two hashes:
 - firewalld_allow_services
 - firewalld_allow_ports

Values for firewalld_allow_services:

    firewalld_allow_services:
      service: <service name>
      zone: [zone]			(default: public)
      permanent: [True|False]	(default: True)
      state: [enabled|disabled]	(default: enabled)

Only service is required!

Values for firewalld_allow_ports:

    firewalld_allow_ports:
      port: <port/protocol>
      zone: [zone]			(default: public)
      permanent: [True|False]	(default: True)
      state: [enabled|disabled]	(default: enabled)


Example Playbook
----------------

    - hosts: servers
      vars:
        firewalld_allow_services:
        - { service: "http" }
        - { service: "telnet", zone: "dmz", permanent: True, state: "disabled" }
      roles:
      - marcelnijenhof.firewalld


License
-------

BSD

Author Information
------------------

Marcel Nijenhof <marceln@pion.xs4all.nl>
