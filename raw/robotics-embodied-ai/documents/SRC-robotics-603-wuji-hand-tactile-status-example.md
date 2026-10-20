---
source_id: "SRC-robotics-603"
title: "Wuji Hand tactile status example"
source_type: "code_repository"
publisher: "Wuji Technology"
source_date: "待验证"
url: "https://github.com/wuji-technology/wuji-sdk/blob/main/examples/python/wuji_hand/3.tactile_status.py"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-20T05:41:11+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-603
---
# Wuji Hand tactile status example

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

101

102

103

104

105

106

107

108

109

110

111

112

113

114

115

116

117

118

119

120

#!/usr/bin/env python3

"""

Tactile example - Wuji Hand.

Auto-detect and connect to a Wuji Hand, check tactile glove status, and print a

small pressure summary when frames are available.

The tactile glove pairs at connect time only — plug it in before running; after

a re-plug, disconnect and reconnect the hand.

Usage: python 3.tactile\_status.py

"""

from \_\_future\_\_ import annotations

import math

import time

from wuji\_sdk import DeviceType, SdkManager, TactileGloveFrame, TactileGloveStatus, WujiHand

REPORT\_SECONDS = 0.5

POLL\_SLEEP\_SECONDS = 0.02

def pressure\_summary(frame: TactileGloveFrame) -> str:

pressure = \[v for v in frame.pressure if math.isfinite(v)\]

if not pressure:

return f"seq={frame.sequence} pressure=\[\]"

sample = pressure\[:8\]

mean\_pressure = sum(pressure) / len(pressure)

return (

f"seq={frame.sequence} "

f"max={max(pressure):.3f} "

f"mean={mean\_pressure:.3f} "

f"first8={\[f'{v:.3f}' for v in sample\]}"

)

def main():

manager = SdkManager.instance()

all\_devices = manager.scan()

for dev in all\_devices:

print(f" SN={dev.sn}, Type={dev.device\_type}, Address={dev.address}")

devices = \[dev for dev in all\_devices if dev.device\_type == DeviceType.WujiHand\]

if not devices:

print("No Wuji Hand devices found")

return 1

hand: WujiHand = manager.connect(sn=devices\[0\].sn, device\_name="wuji\_hand")

initial\_status: TactileGloveStatus | None = None

attached = False

deadline = time.monotonic() + 1.0

while time.monotonic() < deadline:

initial\_status = status\_sub.recv()

if initial\_status is not None:

attached = initial\_status.state == 1

break

time.sleep(POLL\_SLEEP\_SECONDS)

print(

f"Connected: {hand.serial\_number} "

f"({hand.handedness\_name()}, tactile\_attached={attached})"

)

if not attached:

\# Pairing happens at connect time only: plugging the glove in later

\# will NOT attach it mid-session — disconnect and reconnect instead.

print("No tactile glove is attached. Plug it in, then disconnect and reconnect.")

status\_sub.close()

manager.disconnect\_all()

return 0

latest: TactileGloveStatus | None = initial\_status

latest\_frame: TactileGloveFrame | None = None

frame\_sub = None

try:

frame\_sub = hand.tactile.subscribe\_pressure\_frame()

print("Subscribed to tactile\_status and tactile pressure frames. Ctrl+C to stop.\\n")

next\_report = time.monotonic()

while True:

status: TactileGloveStatus | None = status\_sub.recv()

if status is not None:

latest = status

frame = frame\_sub.recv()

if frame is not None:

latest\_frame = frame

now = time.monotonic()

if latest is not None and now >= next\_report:

attached = latest.state == 1

if latest\_frame is not None:

print(

f"\[{hand.device\_name}\]\[Tactile\] "

f"attached={attached} {pressure\_summary(latest\_frame)}"

)

else:

print(f"\[{hand.device\_name}\]\[Tactile\] attached={attached}")

next\_report = now + REPORT\_SECONDS

if status is None and frame is None:

time.sleep(POLL\_SLEEP\_SECONDS)

except KeyboardInterrupt:

pass

finally:

status\_sub.close()

if frame\_sub is not None:

frame\_sub.close()

manager.disconnect\_all()

return 0

if \_\_name\_\_ == "\_\_main\_\_":

raise SystemExit(main())
