##### Tool: [ssh](https://www.openssh.com/)

###### Escape Sequence

```
# Supported escape sequences:
~.  - terminate connection (and any multiplexed sessions)
~B  - send a BREAK to the remote system
~C  - open a command line
~R  - Request rekey (SSH protocol 2 only)
~^Z - suspend ssh
~#  - list forwarded connections
~&  - background ssh (when waiting for connections to terminate)
~?  - this message
~~  - send the escape character by typing it twice
```

###### Compare a remote file with a local file

```bash
ssh user@host cat /path/to/remotefile | diff /path/to/localfile -
```

###### SSH connection through host in the middle

```bash
ssh -t reachable_host ssh unreachable_host
```

###### Run command over SSH on remote host

```bash
cat > cmd.txt << __EOF__
cat /etc/hosts
__EOF__

ssh host -l user $(<cmd.txt)
```

###### Get public key from private key

```bash
ssh-keygen -y -f ~/.ssh/id_rsa
```

###### Get all fingerprints

```bash
ssh-keygen -l -f .ssh/known_hosts
```

###### SSH authentication with user password

```bash
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@remote_host
```

###### SSH authentication with publickey

```bash
ssh -o PreferredAuthentications=publickey -o PubkeyAuthentication=yes -i id_rsa user@remote_host
```

###### Simple recording SSH session

```bash
function _ssh_sesslog() {

  _sesdir="<path/to/session/logs>"

  mkdir -p "${_sesdir}" && \
  ssh $@ 2>&1 | tee -a "${_sesdir}/$(date +%Y%m%d).log"

}

# Alias:
alias ssh='_ssh_sesslog'
```

###### Using Keychain for SSH logins

```bash
### Delete all of ssh-agent's keys.
function _scl() {

  /usr/bin/keychain --clear

}

### Add key to keychain.
function _scg() {

  /usr/bin/keychain /path/to/private-key
  source "$HOME/.keychain/$HOSTNAME-sh"

}
```

###### SSH login without processing any login scripts

```bash
ssh -tt user@host bash
```

###### SSH local port forwarding

Example 1:

```bash
# Forwarding our local 2250 port to nmap.org:443 from localhost through localhost
host1> ssh -L 2250:nmap.org:443 localhost

# Connect to the service:
host1> curl -Iks --location -X GET https://localhost:2250
```

Example 2:

```bash
# Forwarding our local 9051 port to db.d.x:5432 from localhost through node.d.y
host1> ssh -nNT -L 9051:db.d.x:5432 node.d.y

# Connect to the service:
host1> psql -U db_user -d db_dev -p 9051 -h localhost
```

  * `-n` - redirects stdin from `/dev/null`
  * `-N` - do not execute a remote command
  * `-T` - disable pseudo-terminal allocation

###### SSH remote port forwarding

```bash
# Forwarding our local 9051 port to db.d.x:5432 from host2 through node.d.y
host1> ssh -nNT -R 9051:db.d.x:5432 node.d.y

# Connect to the service:
host2> psql -U postgres -d postgres -p 8000 -h localhost
```

___
