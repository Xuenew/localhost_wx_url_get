#Author:xue yi yang
# with open("audio/tes_ab.text","rb") as f:
#     with open("audio/tes.wav","wb") as k:
#         k.write(f.read())
#     #print("ok")
# with open("audio/tes_ab.text","rb") as f:
#     #print("ab : ",len(f.read()))
# with open("audio/tes_wb.text","rb") as g:
#     #print("wb : ",len(g.read()))
# import sox
# create combiner
# cbn = sox.Combiner()
# pitch shift combined audio up 3 semitones
#cbn.pitch(3.0)
# convert output to 8000 Hz stereo
#cbn.convert(samplerate=8000, channels=2)
# create the output file
# cbn.build(
#     ['t1.wav', 't2.wav',],'t3.wav', 'concatenate'
# )

from pydub import AudioSegment
song = AudioSegment.from_wav("t1.wav")
song2 = AudioSegment.from_wav("t2.wav")
without_the_middle = song + song2
without_the_middle.export("mashup.wav", format="wav")
#print("ok")