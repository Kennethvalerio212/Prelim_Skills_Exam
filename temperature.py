class Temperature:
    def __init__(self,kelvin=None, celsius=None, fahrenheit=None):
        values= [x for x in [kelvin celsius,fahrenheit] if x]

        if len(values) <1:
            raise ValueError ('Need Argument')
        
        if len(values) >1:
            raise ValueError('Only one argument')
        
        if celsius is not None:
            self.kelvin = celcius + 273.15
        
        elif fahrenheit is not None:
            self.kelvin = (fahrenheit-32 *5 / 9 + 273.15)
        
        else:
            self.kelvin=kelvin
        
        if self.kelvin <0:
            raise ValueError('Temperature in kelvin cannot be negative')
        
    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'
        