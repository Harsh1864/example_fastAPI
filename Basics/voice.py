import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["harsh","pako","sahil","bhauto","prashiyo","hepin"]
for item in l:
 speaker.Speak(f"big shoutout to you {item}")