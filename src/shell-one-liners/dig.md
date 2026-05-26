##### Tool: [dig](https://en.wikipedia.org/wiki/Dig_(command))

###### Resolves the domain name (short output)

```bash
dig google.com +short
```

###### Lookup NS record for specific domain

```bash
dig @9.9.9.9 google.com NS
```

###### Query only answer section

```bash
dig google.com +nocomments +noquestion +noauthority +noadditional +nostats
```

###### Query ALL DNS Records

```bash
dig google.com ANY +noall +answer
```

###### DNS Reverse Look-up

```bash
dig -x 172.217.16.14 +short
```

___
