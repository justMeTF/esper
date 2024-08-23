import smi2sublist as ss
import printer as p

#smi_files='test_timeNotyet.smi'
smi_files="C:/esper/subtitles/Godzilla.Mothra.And.King.Ghidorah.Giant.Monsters.All-Out.Attack.2001.JAPANESE.1080p.BluRay.H264.AAC-VXT.smi"
subtitles=ss.smi2sub(smi_files)
#print(subtitles)
p.printing(subtitles)