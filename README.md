# Audacity Timestamp Converter

Audacity exports timestamps in seconds which is hard to use in real-life scenarios
This app helps with converting the start time seconds to a more user-friendly time format (HH:MM:SS.ss)

## Usage
Open "app" folder in the command line and run ```python main.py input.txt output.txt```

__Note__: Change *"input.txt"* and *"output.txt"* to your own preference

##### input.txt
> 13.040000	13.040000	1. The Essentialist  
2528.080000	2528.080000	2. CHOOSE: The Invincible Power of Choice  
3150.690000	3150.690000	3. DISCERN: The Unimportance of Practically Everything  
3781.870000	3781.870000	4. TRADE-OFF: Which Problem Do I Want?

After the program is ran the output file is created or if it already exists it is overridden
##### output.txt
> 0:00:13.04 	 1. The Essentialist  
0:42:08.08 	 2. CHOOSE: The Invincible Power of Choice  
0:52:30.69 	 3. DISCERN: The Unimportance of Practically Everything  
1:03:01.87 	 4. TRADE-OFF: Which Problem Do I Want?
