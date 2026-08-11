---
source_id: "SRC-robotics-528"
title: "onshape-to-robot issue 206 retrieve-convert config behavior"
source_type: "user_issue"
publisher: "Rhoban/onshape-to-robot contributor"
source_date: "2026-08-09"
url: "https://github.com/Rhoban/onshape-to-robot/issues/206"
evidence_grade: "B"
capture_method: "defuddle"
captured_at: "2026-08-10T15:46:26+00:00"
tags:
  - raw/source
  - source-type/user-issue
  - evidence/b
aliases:
  - SRC-robotics-528
---
# onshape-to-robot issue 206 retrieve-convert config behavior

I designed a robot in Onshape. I wanted to retrieve the model from Onshape and then play around with the *config.json* to see how to best configure an actuator. But it looks like the *robot.pkl* bakes in the `joint_properties` defined in the *config.json* when the file retrieval happens. When I change the *config.json* and call the processors to convert the pickle file into mujoco xml the changes I made to the *config.json* (specifically the `joint_properties`) is not consumed.

Here is the pickle file I retrieved from Onshape (using `onshape-to-robot --retrieve monowheel`) and the *config.json*:  
[robot.pkl.zip](https://github.com/user-attachments/files/30880649/robot.pkl.zip)

```json
{
    "url": "https://cad.onshape.com/documents/95bfab4fd6020a0d0f88e088/w/4bf666f2ea442254abcd4d9b/e/6618905851064b92dd34a583",
    "output_format": "mujoco"
}
```

I converted this pkl to mujoco xml (using `onshape-to-robot --convert monowheel`), and here is the actuator part from the generated robot.xml file:

```
<actuator>
    <position class="monowheel" name="wheel_legs" joint="wheel_legs"/> # default type is "position", so this is correct
  </actuator>
```

Now, I added a `joint_property` to *config.json* and re-generated the *robot.xml* (after deleting the old ones), but I get the same code stub as before:

```json
{
    "url": "https://cad.onshape.com/documents/95bfab4fd6020a0d0f88e088/w/4bf666f2ea442254abcd4d9b/e/6618905851064b92dd34a583",
    "output_format": "mujoco",
    "joint_properties": {
        "wheel_legs": {
            "type": "velocity",
            "range": false,
	    "kv": 5
        }
    }
}
```
```
<actuator>
    <position class="monowheel" name="wheel_legs" joint="wheel_legs"/> # no change (should be velocity type)
  </actuator>
```

To confirm my hypothesis, I deleted the pickle file and other generated files and did a retrieve again (this time with the `joint_properties` defined in *config.json*). Now after conversion the *robot.xml* file has the velocity type as the actuator.

```
<actuator>
    <velocity class="monowheel" name="wheel_legs" joint="wheel_legs" kv="5"/>
  </actuator>
```

Next, I removed the `joint_properties` and re-generated the *robot.xml* but the actuator retains the velocity type.

This lead me to conclude that the pickle file bakes in the `joint_properties` of the config.json when the assembly is fetched from OnShape.

Is there a workaround this problem?
