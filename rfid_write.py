from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
print("Hold a tag on the reader to WRITE…")
reader.write("HELLO-RPI-ACCESS")
print("Done!")
