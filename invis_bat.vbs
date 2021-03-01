Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "D:\my-documents\code\python\time-recorder\time-recorder.bat" & Chr(34), 0
Set WshShell = Nothing