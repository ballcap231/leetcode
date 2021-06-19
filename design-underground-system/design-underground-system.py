# O(E + V) space where E is the number possible station routes and V is number of possible stations
class UndergroundSystem:
    #O(1) time and space
    def __init__(self):
        self.station_means = {}
        self.check_ins = {}
    
    # O(1) time and space
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = [stationName, t]
    # O(1) time and space
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, in_time = self.check_ins.pop(id)
        station_map = (in_station, stationName)
        current_time = t - in_time
        if station_map not in self.station_means:
            self.station_means[station_map] = [current_time,1]
        else:
            time_sum,time_count = self.station_means[station_map]
            self.station_means[station_map] = time_sum + current_time, time_count + 1
    # O(1) time and space
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time_sum, time_count = self.station_means[(startStation, endStation)]
        time_mean = time_sum / time_count
        return time_mean
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)