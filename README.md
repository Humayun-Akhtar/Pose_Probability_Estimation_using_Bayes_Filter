Probelm Statement: A robot moves in one-dimension discrete that is 100 meters long. At each time step the robot position is discrete and can change only by 1 meter. The robot moves 1 meter at each time step. Because of slip and friction 10% of the time it moves 2 meters; 5% it does not move 5% of the time it moves backwards by 1m and 80% it moves 1 meter.
It has a GPS that gives the location. The sensor measures the correct location for 90% of the time and 10% of the time it gives the wrong location.

Solution: Bayes filter is used to estimate the position of the robot in the corridor with the following defined prediction model and measurement model:
CONTROL MODEL: 𝑷(𝒑𝒐𝒔′𝒕=𝒙+𝟏|𝒖𝒕 ,𝒑𝒐𝒔′𝒕−𝟏=𝒙)=𝟎.𝟖 𝑷(𝒑𝒐𝒔′𝒕=𝒙+𝟐|𝒖𝒕 ,𝒑𝒐𝒔′𝒕−𝟏=𝒙)=𝟎.𝟏 𝑷(𝒑𝒐𝒔′𝒕=𝒙|𝒖𝒕 ,𝒑𝒐𝒔′𝒕−𝟏=𝒙)=𝟎.𝟎𝟓 𝑷(𝒑𝒐𝒔′𝒕=𝒙−𝟏|𝒖𝒕 ,𝒑𝒐𝒔′𝒕−𝟏=𝒙)=𝟎.𝟎𝟓
MEASUREMENT MODEL: 𝑷(𝑴𝒆𝒂𝒔𝒖𝒓𝒆𝒅𝑳𝒐𝒄𝒂𝒕𝒊𝒐𝒏𝒕=𝒙| 𝒑𝒐𝒔′𝒕=𝒙)=𝟎.𝟗 𝑷(𝑴𝒆𝒂𝒔𝒖𝒓𝒆𝒅𝑳𝒐𝒄𝒂𝒕𝒊𝒐𝒏𝒕≠𝒙|,𝒑𝒐𝒔′𝒕=𝒙)=𝟎.𝟏

