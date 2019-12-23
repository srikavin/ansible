# http_status

This module fetches the status code of a given webpage.

## Usage

This module returns the status code in `out.status_code`.

### Sample Playbook
```yaml
- name: Test http_status
  hosts: localhost
  tasks:
  - name: Check HTTP status code of google.com
    http_status:
      url: 'https://google.com'
    register: out
  - name: Dump output
    debug:
      msg: '{{ out }}'
```

An Asciinema of it running can be found [here](https://asciinema.org/a/dCv5vSsJHqXvimhwlPwATzJJ7).