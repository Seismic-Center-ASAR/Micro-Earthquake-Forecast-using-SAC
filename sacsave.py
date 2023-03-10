from obspy import UTCDateTime
from obspy.clients.seedlink import Client

client = Client("geofon.gfz-potsdam.de", 18000)
buffer_size = 60  # in seconds
endtime = UTCDateTime.now()
starttime = endtime - buffer_size

# Continuously get and print the waveform data
while True:
    st = client.get_waveforms("RO", "VRI", "", "EHZ", starttime, endtime)
    trace = st[0]
    data = trace.data
    print("Minimum value: ", min(data), "Maximum value: ", max(data))
    
    # Write data to SAC file
    trace.write("data.sac", format="SAC")
    
    # Update the start and end times for the next iteration
    endtime = UTCDateTime.now()
    starttime = endtime - buffer_size

