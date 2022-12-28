class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        temp_list = list()

        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00

        temp_list.append(Kelvin)
        temp_list.append(Fahrenheit)

        return temp_list
    
    # TC:O(1) & SC:O(1)
        
        