"""
Problem statement:
	* Base class having two objects in it
	* constructor and destructor 
	* 1. Execution: test execution has to take command line arguments and 
	execute those test scenarios
	* 2. Comparision: has to take what type of comparion it need 
	and according that it has to take further arguments 
"""

"""
Factory design pattern 
"""

class comparison(self, *args, **kwargs):
	#Result compare
	def compare_log(self, *args, **kwargs):
		#log compare
		self.
	def compare_golden_ref(self, *args, **kwargs):
		#compare golden refernce
	def compare_hw_trace(self, *args, **kwargs):
		#compare hw trace
	def compare_crash_dump(self, *args, **kwargs):
		#compare crash dump 

class nnpi_util_test: 
	"""
	"""
	def __init__(self, utility, args, timeout, outputfile):
		self.utility = utility
		self.args = args
		self.timeout = timeout
		self.outfile = outfile
		#Utility init
		super(self).__init__(self, utility, args, timeout, outputfile)

	def __del__(self, *args, **kwargs):
		#Utility del
		super(self).__init__(*args, **kwargs)

	def execution(self, *args, **kwargs): #excution string
		#Execution procedure
		#execution(utility, cmd_arg, outformat, outfile, timeout, returnval)
		#serilaization module input this.serilize
		#
	#self.serialize()
	comparison m_comparsion

class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

#How to push the data to output file ??
# pop up the commands 

# Base class
# derive class from factory mentod
#per class serializer 

#in the compare comare with 

var = nnpi_util_test()

var.execution(cmd)
var.m_comparsion.log_cmp()



nnpi_ctl list -a
version < 4
nnpi_bios_updae /image/path 
nnpi_ctl list -a

PCI DEV ID :90990
VEnd ID:9032
version :12354