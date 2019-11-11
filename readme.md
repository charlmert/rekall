# Using rekall to analyze memory (live or dump) to find hidden rootkits

Rekall is a python program which can inspect memory using plugins which traverse the memory in order to see things like
which processes were running on the host when the memory dump was performed. Rekall can also inspect live memory (volatility cannot do this).

## Get rekall

On mac best to check the releases:
https://github.com/google/rekall/releases/tag/1.7.2rc1

Download the python binary packaged (including all so's) https://github.com/google/rekall/releases/download/1.7.2rc1/rekall-OSX-1.7.2rc1.zip
In there you can run

```bash
./rekal
```

Anywhere else I'm sure the following would work (I tested on debian 9.9)

```bash
pip3 install rekall
```

## Profiles

The profiles for rekall are here: https://github.com/google/rekall-profiles
The ~/.rekallrc should have been created and set to contain the following lines:

```bash
profile_path:
  - https://raw.githubusercontent.com/google/rekall-profiles
```

It's possible to use volatility profiles but these will need to be converted to rekall format using the rekall convert_profile plugin
I'm analyzing for debian 9.9 and macosx mojave 10.14.6 and could not find any rekall profiles so going to try using/converting volatility profiles.

(I could not find any profiles for debian 9.9 or macosx 10.14.6 for volatility either, will updated below when using existing profile)
You can find volatility profiles here: https://github.com/volatilityfoundation/profiles
To convert I'm going to get the volatility profiles by fetching them from git (raw).

```bash

```

### Generating profile

To build a profile from a clean (uncompromised) system once would need a fresh install of your os.

Open up a rekal shell

```bash
./rekal
```

Run the following:

```bash
build_local_profile('Memory')
```

## Checking syscall table against clean profile

```bash
./rekal --live --profile 
```
