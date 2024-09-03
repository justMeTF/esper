import smi2sublist as ss
import printer as p

#smi_files='test_timeNotyet.smi'
smi_files="C:\esper\subtitles\Jodorowskys.Dune.2013.1080p.BluRay.x264.YIFY.smi"
subtitles=ss.smi2sub(smi_files)
#print(subtitles)
p.printing(subtitles)