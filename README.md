# vivadocker

From windows admin terminal:

1. Find bus id:
```
> usbipd list
...
4-11   0403:6010  USB Serial Converter A, USB Serial Converter B                Not shared
```

2. Attach and bind
```
> usbipd bind --busid 4-11
> usbipd attach --wsl --busid 4-11
```

*Optional if systemd is not running* From linux:
```
sudo modprobe ftdi_sio
```

Then from windows terminal:

```
docker run --rm -it --privileged -v /dev/bus/usb/:/dev/bus/usb
```

