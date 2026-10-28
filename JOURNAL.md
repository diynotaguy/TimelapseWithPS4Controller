# Title: PS4 controller timelapse tool
# Author: DiyNotAGuy (@diynotaguy)
# Description: Software that allows you to take and save a picture on your laptop with your phone camera when the triangle button on your connected PS4 controller is pressed. There is also a Bambu Lab A-series attachment that allows you to specifically take 3D printing timelapses.
# Created_at: 2026-07-16

### July 16th: Used CAD & 3D printing to attach the controller to the 3D printer

I downloaded and modified files from 3D farmers (video here:https://youtu.be/cq9vJKatgys?si=HSvmMYZ_uBGQMxtR, print files here: https://makerworld.com/en/models/1419289-farmtools-timelapse-upgrade-for-a1-and-a1-mini#profileId-1474340). I reused their model geometry for the parts that attach to the 3D printer, but modified the the button presser location and overhauled the controller holder part to allow them to work for the PS4 controller.

I decided that the 3D printer would press the triangle button on the controller, because the triangle button would trigger a photo on the open camera app (link to that here: https://opencamera.org.uk/). 

The first design (Lapse links 1&2) had 5 issues:
- The dimensions were too far off for the controller to sit in the correct place
- Printing the whole length of the design was wasting filament because the controller didn't need that much contact to be fully supported by it
- I hadn't added a chamfer above part of the section that attached to the 3D printer, so it broke off because it was too thin
- I couldn't put the controller in bluetooth mode or plug in a usb cable because I hadn't accounted for that in my design, and so the bluetooth mode buttons and the charging port were covered by the holder
- The button presser on the 3D printer toolhead wasn't in line with the triangle button on the controller


In my second design (Lapse link 3) I rectified the issues by cutting off around half of the holder in CAD. This had the added benefit of leaving spaces for me to press the bluetooth mode buttons or plug in a usb cable. I also added the chamfer, modified some of the PS4 holder dimensions, and changed the location of the button presser relative to the part that attaches to the 3D printer toolhead

**Total time spent: 2h**
**Lapse link 1:** https://lapse.hackclub.com/timelapse/DfeewfCisA9P 
**Lapse link 2:** https://lapse.hackclub.com/timelapse/ta7twcQvVr0Y 
**Lapse link 3:** https://lapse.hackclub.com/timelapse/EQLFz6jcyf7O 