/bin/dbus-send --print-reply --type=method_call --system --dest=net.connman /net/connman/technology/cellular net.connman.Technology.SetProperty string:Powered variant:boolean:false
